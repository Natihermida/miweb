from django.urls import path
from . import views

from .views import ProyectoListView, ProyectoDetailView, ProyectoCreateView, ProyectoUpdateView, ProyectoDeleteView



app_name = 'principal'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto-lista'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto-detalle'),
    path('proyectos/nuevo/', views.ProyectoCreateView.as_view(), name='proyecto-nuevo'),
    path('proyectos/editar/<int:pk>/', views.ProyectoUpdateView.as_view(), name='proyecto-editar'),
    path('proyectos/eliminar/<int:pk>/', views.ProyectoDeleteView.as_view(), name='proyecto-eliminar'),
    path('contacto/', views.contacto_view, name='contacto'),  
     path('welcome/', views.welcome_view, name='welcome'),  # Nueva ruta para la vista de bienvenida
]


