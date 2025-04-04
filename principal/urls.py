from django.urls import path
from . import views


from .views import ProyectoListView, ProyectoDetailView # Importar las vistas necesarias



app_name = 'principal'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto_detail'),
    
    path('contacto/', views.contacto_view, name='contacto'),  
     path('welcome/', views.welcome_view, name='welcome'),  # Nueva ruta para la vista de bienvenida
] 


