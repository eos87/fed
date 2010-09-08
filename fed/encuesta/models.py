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

MEDIOS_REFLEXION = (('taller_formacion', 'Talleres de formación'),
                    ('foros', 'Foros'),
                    ('intercambio_xp', 'Intercambio de experiencias'),
                    ('visitas_grupales', 'Visitas grupales'),
                    ('visitas_indiv', 'Visitas individuales'),
                    ('teatros', 'Teatros'),
                    ('circulo_estudio', 'Círculos de estudio'),
                    ('actos_cultura', 'Actos culturales'),
                    ('reunion_comunitaria', 'Reuniones comunitarias'), )

class AccionRealizadaReflexion(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS_REFLEXION)
    mujeres = models.IntegerField('Con las mujeres')
    hombres = models.IntegerField('Con los hombres')
    jovenes = models.IntegerField('Con los y las jóvenes')
    div_sexual = models.IntegerField('Con las personas de la diversidad sexual')
    vih = models.IntegerField('Con las personas con VIH y SIDA')
    etnica = models.IntegerField('Con las personas de población étnica e indigena')
    discapacidad = models.IntegerField('Con las personas con discapacidad')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción realizada para reflexión de pob'
        verbose_name_plural = 'Acciones realizadas para reflexión de pob'
        
PERSONAS_REFLEXION = (('personas_participaron', 'Número de personas que participaron en las acciones realizadas para reflexionar sobre derechos sexuales y reproductivos'),
                      ('personas_participaron_toman_decision', 'Número de personas que participaron y que actualmente pueden tomar decisiones sexuales y reproductivas de manera autonoma y bien informada'), )

class AccionRelizadaReflexionPersona(models.Model):
    accion = models.CharField(max_length=100, choices=PERSONAS_REFLEXION)
    mujeres = models.IntegerField('Las mujeres')
    hombres = models.IntegerField('Los hombres')
    jovenes = models.IntegerField('Los y las jóvenes')
    div_sexual = models.IntegerField('Las personas de la diversidad sexual')
    vih = models.IntegerField('Las personas con VIH y SIDA')
    etnica = models.IntegerField('Las personas de población étnica e indigena')
    discapacidad = models.IntegerField('Las personas con discapacidad')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción realizada para reflexion Cant'
        verbose_name_plural = 'Acciones realizadas p/reflexión Cant'

MEDIOS2 = (('tv', 'Campañas por Televisión'),
           ('radio', 'Campañas radiales'),
           ('periodico', 'Artículos en periódicos'),
           ('talleres', 'Talleres de formación'),
           ('foros', 'Foros'),
           ('intercambio_xp', 'Intercambio de experiencias'),
           ('visitas', 'Visitas grupales o individuales'),
           ('teatros_actos', 'Teatros y actos culturales'),
           ('circulo_estudio', 'Círculos de estudio'),
           ('reunion_comu', 'Reuniones comunitarias'),
           ('material_educativo', 'Materiales educativos'),
           ('reunion_autorid', 'Reuniones con autoridades'),
           ('consejeria', 'Consejería y promotoría social'), )

class AccionImpulsadaOrg(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS2)
    acciones_emprendidas = models.IntegerField('Número de acciones emprendidas por las Org. para la prevención de la violencia basada en género')
    acciones_cambios_actitud = models.IntegerField('Número de acciones que lograron cambios de actitud de los grupos metas para la prevención de violencia basada en género')
    acciones_impulsadas_masculinidad = models.IntegerField('Numero y tipo de acciones impulsadas por las Org. para promover masculinidad libre de prejuicios y violencia')
    acciones_cambios_masculinidad = models.IntegerField('Numero de acciones que lograron cambio de actitud de los grupos metas hacia la masculinidad libre de prejuicios y violencia')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impul. x/Org p/prev violencia '
        verbose_name_plural = 'Acciones impul. x/Org. p/prev violencia'

class AccionImpulsadaGrupo(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS2)
    acciones_emprendidas_sex = models.IntegerField('Número y tipo de acciones emprendidas por los grupos de diversidad sexual, para prev de violencia basada en género')
    acciones_cambio_sex = models.IntegerField('Numero de acciones que lograron cambio de actitud en grupo de diversidad sexual')
    acciones_emprendidas_discapa = models.IntegerField('Número y tipo de acciones emprendidas por los grupos de personas con discapacidad para prev de violencia basada en género')
    acciones_cambio_discapa = models.IntegerField('Número de acciones que lograron cambio de actitud en grupo de personas con discapacidad')
    acciones_emprendidas_etnia = models.IntegerField('Número de acciones emprendidas por los grupos étnicos y pueblos indígenas para la prevención de la violencia basada en género')
    acciones_cambio_etnia = models.IntegerField('Número de acciones que lograron cambio de actitud en grupos étnicos y pueblos indígenas')
    acciones_emprendidas_jovenes = models.IntegerField('Número de acciones emprendidas por los y las jóvenes para la prevención de la violencia basada en género')
    acciones_cambio_jovenes = models.IntegerField('Número de acciones que lograron cambio de actitud en los y las jóvenes ')

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impulsada por grupos'
        verbose_name_plural = 'Acciones impulsadas por grupos'

    