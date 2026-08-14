from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('api/login/', views.login, name='api_login'),

    # CRUD 1: Proyectos
    path('api/proyectos/', views.proyectos_api, name='proyectos_list'),
    path('api/proyectos/<int:pk>/', views.proyectos_api, name='proyectos_detail'),

    # CRUD 2: Contacto
    path('api/contacto/', views.contacto_api, name='contacto_list'),
    path('api/contacto/<int:pk>/', views.contacto_api, name='contacto_detail'),

    # CRUD 3: Tools
    path('api/tools/', views.tools_api, name='tools_list'),
    path('api/tools/<int:pk>/', views.tools_api, name='tools_detail'),

    # Categorías
    path('api/categorias/', views.categorias_api, name='categorias_list'),
]


