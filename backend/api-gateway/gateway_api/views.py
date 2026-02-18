import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

class GatewayView(APIView):
    def forward_request(self, request, service_url, endpoint):
        if endpoint and not endpoint.startswith('/'):
            endpoint = '/' + endpoint
        full_url = f"{service_url}{endpoint}"
        headers = {}
        auth_header = request.headers.get('Authorization')
        if auth_header:
            headers['Authorization'] = auth_header

        try:
            if request.method == 'GET':
                response = requests.get(full_url, headers=headers, params=request.GET)
            elif request.method == 'POST':
                if request.FILES:
                    data = request.POST.dict()
                    files = {}
                    for key, file in request.FILES.items():
                        files[key] = (file.name, file.read(), file.content_type)
                    response = requests.post(full_url, headers=headers, data=data, files=files)
                else:
                    response = requests.post(full_url, headers=headers, json=request.data)
            elif request.method == 'PUT':
                if request.FILES:
                    data = request.POST.dict()
                    files = {}
                    for key, file in request.FILES.items():
                        files[key] = (file.name, file.read(), file.content_type)
                    response = requests.put(full_url, headers=headers, data=data, files=files)
                else:
                    response = requests.put(full_url, headers=headers, json=request.data)
            elif request.method == 'DELETE':
                response = requests.delete(full_url, headers=headers, json=request.data)
            else:
                return Response({'error': f'Méthode {request.method} non supportée'}, status=405)

            try:
                response_data = response.json()
            except:
                response_data = response.text
            return Response(response_data, status=response.status_code, headers=dict(response.headers))

        except requests.exceptions.ConnectionError:
            return Response({'error': f'Service indisponible: {service_url}'}, status=503)
        except Exception as e:
            return Response({'error': f'Erreur du gateway: {str(e)}'}, status=500)

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