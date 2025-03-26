# filepath: c:\python\django\miweb\principal\views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Proyecto
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



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
    # Cuando se recibe el formulario de contacto, enviar correo a mi correo
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        send_email(nombre,email,mensaje)
        
        return redirect('principal:contacto') # Asegúrate de que esta URL exista en `urls.py`

    return render(request, "contacto.html")
login_required
def welcome_view(request):
    return render(request, 'principal/welcome.html')



def send_email(nombre,email,mensaje):
    sender_email = "itcode1992@gmail.com"
    receiver_email = "itcode1992@gmail.com"
    password = "rftk qoak aijl tkuw"

    message = MIMEMultipart()
    # Construir el mensaje
    subject = f"Nuevo mensaje de {nombre}"
    message = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"
    from_email = "itcode1992@gmail.com" #settings.EMAIL_HOST_USER  
    recipient_list =["itcode1992@gmail.com"] #[settings.EMAIL_HOST_USER]

    

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Establecer seguridad TLS
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")









