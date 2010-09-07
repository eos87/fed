# -*- coding: UTF-8 -*-

from django.db import models
from fed.lugar.models import *

CHOICE_MEDIO = (('estudios', 'Estudios'),
                ('foros', 'Foros'),
                ('cabildos', 'Cabildeos'),
                ('campania_tv', 'Campañas en televisión'),
                ('campania_radio', 'Campañas en radio'),
                ('talleres', 'Talleres de formación'),
                ('manifestaciones', 'Manifestaciones'),
                ('reuniones', 'Reuniones'),)

CHOICE_REGION = (('comunitario', 'A nivel comunitario'),
                 ('municipal', 'A nivel municipal'),
                 ('departamental', 'A nivel departamental'),
                 ('regional', 'A nivel regional'),
                 ('nacional', 'A nivel nacional'), )
                 
CHOICE_DOCS = (('leyes', 'Leyes'),
               ('codigos', 'Códigos'),
               ('reglamentos', 'Reglamentos'),
               ('normativas', 'Normativas'),
               ('ordenanzas', 'Ordenanzas'),
               ('acuerdos', 'Acuerdos'),)

VERBOSE_CANTIDAD = 'Número de acciones efectuadas para fomentar la existencia y aplicación efectiva de políticas públicas para posicionar el tema de la equidad e igualdad'
VERBOSE_PARTICIPAN = 'Participantes en las acciones'

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

class AccionEfectuadaMedio(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO)
    cantidad = models.IntegerField(VERBOSE_CANTIDAD)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción efectuada según medio'
        verbose_name_plural = 'Acciones efectuadas según medio'

class AccionEfectuadaRegion(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION)
    cantidad = models.IntegerField(VERBOSE_CANTIDAD)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción efectuada por región afectada'
        verbose_name_plural = 'Acciones efectuadas por regiones afectadas'

class AccionEfectuadaDocumento(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_DOCS)
    cantidad = models.IntegerField('Número de iniciativas promovidas para posicionar el tema de la equidad e igualdad')
    participantes = models.IntegerField('Numero de iniciativas aprobadas e implementadas para posicionar el tema de la equidad e igualdad')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción efectuada por tipo de documento'
        verbose_name_plural = 'Acciones efectuadas por tipos de documentos'

class ParticipacionComisionDecision(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION)
    cantidad_instancias = models.IntegerField('Número de instancias donde participan para mejorar la toma de decisiones sobre DDSSRR y equidad')
    cantidad_acciones_promovidas = models.IntegerField('Número de acciones promovidas para mejorar la toma de decisiones sobre DDSSRR y equidad')
    cantidad_acciones_efectivas = models.IntegerField('Número de acciones efectivas para mejorar la toma de decisiones sobre DDSSRR y equidad generando cambios')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Parti en comision para decisiones'
        verbose_name_plural = 'Parti en comisión para decisiones'

class ParticipacionComisionAgenda(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION)
    cantidad_instancias = models.IntegerField('Número de instancias donde ' \
                                              'participan para mantener en la agenda pública la defensa DDSSRR', db_column='cat_instancias')
    cantidad_acciones_prom = models.IntegerField('Número de acciones promovidas ' \
                                                 'para mantener en la agenda pública la defensa DDSSRR', db_column='cant_acc_prom')
    cantidad_acciones_efec = models.IntegerField('Número de acciones efectivas para mantener ' \
                                                 'en la agenda pública la defensa DDSSRR y generar cambios', db_column='cant_acc_efec')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Participación en comisiones para agenda'
        verbose_name_plural = 'Participaciones en comisiones para agenda'

class AccionObservatorio(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION)
    cantidad_observatorios = models.IntegerField('Número de observatorios funcionando para la vigilancia de la restitución, creación y aplicación de leyes, políticas, acciones y servicios en torno a los DDSSRR')
    cantidad_acciones_realiz = models.IntegerField('Número de acciones realizadas en marco de los observatorios')
    cantidad_acciones_web = models.IntegerField('Número de acciones visibilizadas, divulgadas y colocadas en la página web de FED')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción para observatorio'
        verbose_name_plural = 'Acciones para observatorios'

ver_sexual = 'En contra de la discriminación a personas de la diversidad sexual'
ver_discapacidad = 'En contra de la discriminación a personas con discapacidad'
ver_vih_sida = 'En contra de la discriminación a personas que viven con VIH y SIDA'
ver_racial = 'En contra de la discriminación a personas de población étnica e indigena'
ver_joven = 'En contra de la discriminación a personas de juventud'

class DenunciaSocialRealizada(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO)
    persona_div_sexual = models.IntegerField(ver_sexual)
    persona_discapacidad = models.IntegerField(ver_discapacidad)
    persona_vih = models.IntegerField(ver_vih_sida)
    persona_racial = models.IntegerField(ver_racial)
    persona_joven = models.IntegerField(ver_joven)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia social realizada'
        verbose_name_plural = 'Denuncias sociales realizadas'

class DenunciaSocialEfectiva(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO)
    persona_div_sexual = models.IntegerField(ver_sexual)
    persona_discapacidad = models.IntegerField(ver_discapacidad)
    persona_vih = models.IntegerField(ver_vih_sida)
    persona_racial = models.IntegerField(ver_racial)
    persona_joven = models.IntegerField(ver_joven)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia social efectivas'
        verbose_name_plural = 'Denuncias sociales efectivas'

CHOICE_JURIDICA = (('denuncia_juridica_realizada', 'Número de acciones de denuncias jurídicas realizadas'),
                   ('denuncia_juridica_atendida', 'Número de denuncias jurídicas atendidas'), )

class DenunciaJuridica(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_JURIDICA)
    persona_div_sexual = models.IntegerField(ver_sexual)
    persona_discapacidad = models.IntegerField(ver_discapacidad)
    persona_vih = models.IntegerField(ver_vih_sida)
    persona_racial = models.IntegerField(ver_racial)
    persona_joven = models.IntegerField(ver_joven)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia jurídica'
        verbose_name_plural = 'Denuncias jurídicas'