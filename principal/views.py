# filepath: c:\python\django\miweb\principal\views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Proyecto
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    # Lógica de la vista
    return render(request, 'home.html')

class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyecto_list.html'

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto_detail.html'

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    template_name = 'proyecto_form.html'
    fields = ['nombre', 'descripcion', 'tecnologias', 'imagen', 'enlace']
    login_url = 'login'  # Redirigir a la página de inicio de sesión si no está autenticado

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'proyecto_form.html'
    fields = ['nombre', 'descripcion', 'tecnologias', 'imagen', 'enlace']
    login_url = 'login'

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('principal:proyecto-lista')
    login_url = 'login'

def contacto_view(request):
    return render(request, 'contacto.html')

login_required
def welcome_view(request):
    return render(request, 'principal/welcome.html')








