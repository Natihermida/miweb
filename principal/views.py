# filepath: c:\python\django\miweb\principal\views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Proyecto
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

def proyectos(request):
    # Obtener todos los proyectos
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto_list.html', {'proyectos': proyectos})

def contacto_view(request):
    # Cuando se recibe el formulario de contacto, enviar correo a mi correo
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        # Llamar a la función para enviar el correo
        send_email(nombre, email, mensaje)

        messages.success(request, "¡Tu mensaje ha sido enviado con éxito!")
        return redirect('principal:contacto')  # Asegúrate de que esta URL exista en `urls.py`

    return render(request, "contacto.html")

def welcome_view(request):
    return render(request, 'principal/welcome.html')


def send_email(nombre, email, mensaje):
    sender_email = "itcode1992@gmail.com"
    receiver_email = "itcode1992@gmail.com"
    password = "rftk qoak aijl tkuw"

    # Crear el mensaje de correo
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Nuevo mensaje de {nombre}"

    # Cuerpo del mensaje
    body = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Establecer seguridad TLS
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")








