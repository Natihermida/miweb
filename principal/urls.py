from django.urls import path
from .views import ProyectoListView, ProyectoDetailView, ProyectoCreateView, ProyectoUpdateView, ProyectoDeleteView

urlpatterns = [
    path('', views.home_view, name='home'),  # Ruta asociada a la vista 'home_view'
    path('proyectos/', ProyectoListView.as_view(), name='proyecto-lista'),
    path('proyectos/<int:pk>/', ProyectoDetailView.as_view(), name='proyecto-detalle'),
    path('proyectos/nuevo/', ProyectoCreateView.as_view(), name='proyecto-nuevo'),
    path('proyectos/editar/<int:pk>/', ProyectoUpdateView.as_view(), name='proyecto-editar'),
    path('proyectos/eliminar/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto-eliminar'),
]

