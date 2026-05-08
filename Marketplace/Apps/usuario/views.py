from django.shortcuts import render


# Create your views here.

# Vista de la página de login
def login(request):
    return render(request, 'usuario/login.html')
