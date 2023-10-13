from django.db import models

from jugadores.models import Jugador

# Create your models here.
class Equipo(models.Model):
    codigo= models.CharField(max_length=3, verbose_name="Código")
    nombre= models.CharField(max_length=45, verbose_name="Nombre")
    def __str__(self):
        return self.nombre
class Club(models.Model):
    codigo= models.CharField(max_length=3, verbose_name="Código")
    nombre= models.CharField(max_length=45, verbose_name="Nombre")

class GrupoEquipo(models.Model):
    equipo=models.ForeignKey(Equipo,verbose_name="Equipo", on_delete=models.CASCADE)
    jugador=models.ForeignKey(Jugador,verbose_name="Juagador", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.equipo.codigo} {self.jugador.primer_apellido}"
class GrupoClub(models.Model):
    club=models.ForeignKey(Club,verbose_name="Equipo", on_delete=models.CASCADE)
    jugador=models.ForeignKey(Jugador,verbose_name="Juagador", on_delete=models.CASCADE)