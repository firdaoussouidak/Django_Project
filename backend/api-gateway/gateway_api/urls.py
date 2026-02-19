from django.urls import re_path
from .views import AuthserviceView, PostserviceView, PostserviceMediaView

urlpatterns = [
    re_path(r'^auth/(?P<endpoint>.*)$', AuthserviceView.as_view(), name='auth_service'),
    re_path(r'^post/(?P<endpoint>.*)$', PostserviceView.as_view(), name='post_service'),
    re_path(r'^media/(?P<endpoint>.*)$', PostserviceMediaView.as_view(), name='post_media'),
]