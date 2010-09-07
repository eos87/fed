from django.db import models
from fed.lugar.models import *

class Organizacion(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Organizaciones'

class Proyecto(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=150)
    municipio = models.ManyToManyField(Municipio)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Proyectos'

