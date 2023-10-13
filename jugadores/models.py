from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Jugador(models.Model):
    primer_nombre= models.CharField(max_length=45,verbose_name="Primer Nombre")
    segundo_nombre= models.CharField(max_length=45,blank=True,null=True,verbose_name="Segundo Nombre")
    
    primer_apellido= models.CharField(max_length=45,verbose_name="Primer Apellido")
    segundo_apellido= models.CharField(max_length=45,verbose_name="Segundo Apellido")
    
    fecha_nacimiento= models.DateField(verbose_name="Fecha de Nacimiento")
    class RH(models.TextChoices):
        OP='OP',_("O+")
        ON='ON',_("O-")
        AP='AP',_("A+")
        AN='AN',_("A-")
        BP='BP',_("B+")
        BN='BN',_("B-")
        ABP='ABP',_("AB+")
        ABN='ABN',_("AB-")
        
    rh= models.CharField(max_length=3,choices=RH.choices,verbose_name="Factor RH")
    class Posicion(models.TextChoices):
        PORTERO = 'PT', _('Portero')
        DEFENSA_CENTRAL = 'DC', _('Defensa Central')
        DEFENSA_LATERAL = 'DL', _('Defensa Lateral')
        DEFENSA_LIBRE = 'DLI', _('Defensa Libre')
        CENTROCAMPISTA = 'CC', _('Centrocampista')
        CENTROCAMPISTA_DEFENSIVO = 'CCD', _('Centrocampista Defensivo')
        CENTROCAMPISTA_OFENSIVO = 'CCO', _('Centrocampista Ofensivo')
        EXTREMO = 'EXT', _('Extremo')
        DELANTERO = 'DEL', _('Delantero')

    posicion=models.CharField(max_length=3,choices=Posicion.choices,verbose_name="Posicion")
    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"