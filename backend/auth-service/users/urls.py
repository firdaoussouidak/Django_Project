from django.urls import path
from .views import LoginView, SignupView, UpdateUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', UpdateUserView.as_view(), name='profile'),
]
