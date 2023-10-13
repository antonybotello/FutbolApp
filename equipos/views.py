from django.shortcuts import render

from equipos.models import GrupoEquipo

# Create your views here.
def grupo_equipo_listar(request):
    titulo="Grupo"
    grupo_equipos= GrupoEquipo.objects.all()
    context={
        "titulo":titulo,
        "grupo":grupo_equipos
    }
    return render(request,"grupo-equipos.html",context)
