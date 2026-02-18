import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GatewayView(APIView):

    def forward_request(self, request, service_url, endpoint):
        # Ensure endpoint starts with /
        if endpoint and not endpoint.startswith('/'):
            endpoint = '/' + endpoint

        full_url = f"{service_url}{endpoint}"

        headers = {
            'Content-Type': 'application/json',
        }

        auth_header = request.headers.get('Authorization')
        if auth_header:
            headers['Authorization'] = auth_header

        data = request.data if request.data else None

        try:
            if request.method == 'GET':
                response = requests.get(full_url, headers=headers, params=request.GET)
            elif request.method == 'POST':
                response = requests.post(full_url, headers=headers, json=data)
            elif request.method == 'PUT':
                response = requests.put(full_url, headers=headers, json=data)
            elif request.method == 'DELETE':
                response = requests.delete(full_url, headers=headers, json=data)
            else:
                return Response(
                    {'error': f'Méthode {request.method} non supportée'},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED
                )

            try:
                response_data = response.json()
            except:
                response_data = response.text

            return Response(response_data, status=response.status_code, headers=dict(response.headers))

        except requests.exceptions.ConnectionError:
            return Response(
                {'error': f'Service indisponible: {service_url}'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        except Exception as e:
            return Response(
                {'error': f'Erreur du gateway: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AuthserviceView(GatewayView):

    def get(self, request, endpoint=''):
        return self.forward_request(request, settings.AUTH_SERVICE_URL, endpoint)

    def post(self, request, endpoint=''):
        return self.forward_request(request, settings.AUTH_SERVICE_URL, endpoint)

    def put(self, request, endpoint=''):
        return self.forward_request(request, settings.AUTH_SERVICE_URL, endpoint)

    def delete(self, request, endpoint=''):
        return self.forward_request(request, settings.AUTH_SERVICE_URL, endpoint)


class PostserviceView(GatewayView):

    def get(self, request, endpoint=''):
        return self.forward_request(request, settings.POST_SERVICE_URL, endpoint)

    def post(self, request, endpoint=''):
        return self.forward_request(request, settings.POST_SERVICE_URL, endpoint)

    def put(self, request, endpoint=''):
        return self.forward_request(request, settings.POST_SERVICE_URL, endpoint)

    def delete(self, request, endpoint=''):
        return self.forward_request(request, settings.POST_SERVICE_URL, endpoint)