from django.shortcuts import render

from Apps.solicitud.models import Solicitud


def solicitudes(request):
    lista_solicitudes = Solicitud.objects.all()
    return render(request, 'solicitud/listado.html', {"solicitudes": lista_solicitudes})
