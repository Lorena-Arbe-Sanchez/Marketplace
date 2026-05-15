from django.shortcuts import render


# Vista de la página de login
def login(request):
    return render(request, 'usuario/login.html')
