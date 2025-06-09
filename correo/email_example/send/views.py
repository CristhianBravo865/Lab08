from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail (
        'Asunto del correo',
        'Este es el cuerpo del correo.',
        'cbravoa@unsa.edu.pe',['jedovi3063@linacit.com'], 
        fail_silently=False,)
    return render(request, 'send/index.html')
