from django.contrib import admin

from equipos.models import Club, Equipo, GrupoClub, GrupoEquipo

# Register your models here.
admin.site.register(Club)
admin.site.register(Equipo)
admin.site.register(GrupoEquipo)
admin.site.register(GrupoClub)


