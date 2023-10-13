from django.urls import path

from equipos.views import grupo_equipo_listar

urlpatterns=[
    path('grupo-equipo/', grupo_equipo_listar, name='ge-listar')
]