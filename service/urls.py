from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('api/login/', views.login, name='api_login'),
]

