from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='auth_register'),
    path('login', RegisterView.as_view(), name='auth_login'),
]