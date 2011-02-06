# -*- coding: UTF-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from fed.lugar.models import Departamento
from fed.lugar.models import Municipio
from fed.utils import *


CHOICE_MEDIO = (('estudios', 'Estudios'),
                ('foros', 'Foros'),
                ('cabildos', 'Cabildeos'),
                ('campania_tv', 'Campañas en televisión'),
                ('campania_radio', 'Campañas en radio'),
                ('talleres', 'Talleres de formación'),
                ('manifestaciones', 'Manifestaciones'),
                ('reuniones', 'Reuniones'),
                ('encuentros', 'Encuentros'))

CHOICE_REGION = (('comunitario', 'A nivel comunitario'),
                 ('municipal', 'A nivel municipal'),
                 ('departamental', 'A nivel departamental'),
                 ('regional', 'A nivel regional'),
                 ('nacional', 'A nivel nacional'),)
                 
CHOICE_DOCS = (('leyes', 'Leyes'),
               ('codigos', 'Códigos'),
               ('reglamentos', 'Reglamentos'),
               ('normativas', 'Normativas'),
               ('ordenanzas', 'Ordenanzas'),
               ('acuerdos', 'Acuerdos'), )

TIPO_CHOICE = ((0, 'Apoyo programático'),
               (1, 'Convocatoria pública'),
               (2, 'Pequeños proyectos'),
               (3, 'Actividades puntuales'),
               (4, 'Acciones de emergencia'),
               (5, 'Estrategias con grupos priorizados'))

CHOICE1 = (('si_hay', 'Si hay'), ('hay_pero', 'Hay un sistema pero no es eficiente'), ('no_hay', 'No hay'), )
CHOICE2 = (('si_hay', 'Si hay'), ('hay_pero', 'Hay un plan estratégico, pero no se utiliza'), ('no_hay', 'No hay'),)
CHOICE3 = (('ninguna', 'Ninguna'), ('proceso', 'En proceso'), ('logrado', 'Logrado'), )

class Organizacion(models.Model):
    nombre = models.TextField()
    nombre_corto = models.CharField(max_length=100)
    #tipo = models.IntegerField(choices=TIPO_CHOICE, verbose_name='Modalidad de apoyo')
    direccion = models.CharField(max_length=150)
    correo = models.EmailField(blank=True, default='example@example.com')
    contacto = models.CharField(max_length=200, blank=True, default='Ninguno')
    telefono = models.CharField(max_length=200, blank=True, default='Ninguno')
    antecedentes = models.TextField()
    user = models.ForeignKey(User, verbose_name='Usuario')
    #campos agregados a organizacion
    sistema = models.CharField(max_length=100, choices=CHOICE1, verbose_name='Cuenta con un sistema admitivo contable', blank=True, default='no-responde')
    plan = models.CharField(max_length=100, choices=CHOICE2, verbose_name='Utilizan su plan estratégico para mejorar sus capacidades de gestión en desarrollo de proyectos, consecusión y ejecución de recursos, comunicación', blank=True, default='no-responde')
    organizaciones = models.CharField(max_length=100, choices=CHOICE3, verbose_name='Apoyan a alguna org. de la diversidad sexual a tener personería', blank=True, default='no-responde')

    def __unicode__(self):
        return self.nombre_corto

    class Meta:
        verbose_name_plural = 'Organizaciones'
        ordering = ['nombre_corto']    

class Proyecto(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    nombre = models.TextField()
    codigo = models.CharField(max_length=150, null=True, blank=True)
    tipo = models.IntegerField(choices=TIPO_CHOICE, verbose_name='Modalidad de apoyo')
    cobertura = models.TextField(verbose_name='Area de cobertura')
    duracion = models.CharField(max_length=30)
    monto = models.CharField('Monto solicitado a FED', null=True, blank=True, max_length=100)
    monto2 = models.CharField('Monto de contrapartida', null=True, blank=True, max_length=100)
    user = models.ForeignKey(User, verbose_name='Usuario')

    def __unicode__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name_plural = 'Proyectos'
        ordering = ['organizacion']

CHOICE_PERIODO = ((0, 'Enero - Febrero'),
                  (1, 'Marzo - Abril'),
                  (2, 'Mayo - Junio'),
                  (3, 'Julio - Agosto'),
                  (4, 'Septiembre - Octubre'),
                  (5, 'Noviembre - Diciembre'))
                  
CHOICE_ANIO = (('2010', '2010'), ('2011', '2011'), ('2012', '2012'))

class Encuesta(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    proyecto = models.ForeignKey(Proyecto)
    periodo = models.IntegerField(choices=CHOICE_PERIODO, verbose_name='Período de informe')
    anio = models.CharField(choices=CHOICE_ANIO, verbose_name='Año', max_length=100)
    informe = models.FileField(upload_to=get_file_path, blank=True, null=True, help_text='Formatos adecuados: .doc, .pdf')
    user = models.ForeignKey(User)
    
    fileDir = 'informes/'

    def __unicode__(self):
        return '%s | %s | %s | %s' % (self.organizacion.nombre, self.proyecto.nombre, CHOICE_PERIODO[int(self.periodo)][1], self.anio)

    def get_periodo(self):
        return CHOICE_PERIODO[self.periodo][1]

    class Meta:
        verbose_name = 'Informe Contraparte'
        verbose_name_plural = 'Informes Contraparte'
        ordering = ['organizacion']

class InformeObjetivo3(models.Model):
    periodo = models.IntegerField(choices=CHOICE_PERIODO, verbose_name='Período de informe')
    anio = models.CharField(choices=CHOICE_ANIO, verbose_name='Año', max_length=100)

    def __unicode__(self):
        return '%s | %s ' % (CHOICE_PERIODO[int(self.periodo)][1], self.anio)

    class Meta:
        verbose_name = 'Informe Equipo Técnico'
        verbose_name_plural = 'Informes Equipo Técnico'

class TipoAccion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre acción')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipo Acciones'

class Meta(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, editable=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Metas'

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Meta, self).save(force_insert, force_update)

class DatoInformeOb3(models.Model):
    tipo_accion = models.ForeignKey(TipoAccion)
    meta = models.ForeignKey(Meta)
    fecha = models.DateField(help_text='Fecha de actividad')
    organizacion = models.ManyToManyField(Organizacion, verbose_name=u'Organizaciónes')
    hombres = models.IntegerField(default=0)
    mujeres = models.IntegerField(default=0)
    informe = models.ForeignKey(InformeObjetivo3)

    def __unicode__(self):
        return 'Dato %s' % self.id

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

class Resultado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Resultados'

class Indicador(models.Model):
    resultado = models.ForeignKey(Resultado)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    slug = models.SlugField(unique=True, null=True, editable=False)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Indicadores'
        ordering = ['id']

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Indicador, self).save(force_insert, force_update)

class ResultadoTrabajado(models.Model):
    resultado = models.ForeignKey(Resultado)    
    municipio = models.ManyToManyField(Municipio, verbose_name='Municipios')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.resultado.nombre

    class Meta:
        verbose_name = 'Resultado trabajado'
        verbose_name_plural = 'Resultados trabajados'


#VERBOSE_CANTIDAD = 'Número de acciones efectuadas para fomentar la existencia y aplicación efectiva de políticas públicas para posicionar el tema de la equidad e igualdad'
VERBOSE_CANTIDAD = 'Prevención de violencia'
VERBOSE_PARTICIPAN = 'Participantes'

class AccionEfectuadaMedio(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO, blank=True, default='no-responde', verbose_name='Tipo')
    cantidad = models.IntegerField(VERBOSE_CANTIDAD, blank=True, default=0)
    viol_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    ssr = models.IntegerField('Salud sexual y reproductiva', blank=True, default=0)
    ssr_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    vih_sida = models.IntegerField('VIH-SIDA', blank=True, default=0)
    vih_sida_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    masculinidad = models.IntegerField('Masculinidad', blank=True, default=0)
    masc_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    div_sexual = models.IntegerField('Diversidad sexual', blank=True, default=0)
    div_sexual_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    equidad = models.IntegerField('Equidad de género', blank=True, default=0)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acciones impulsadas: Tipo de accion'
        verbose_name_plural = 'Acciones impulsadas: Tipo de acciones'

class AccionEfectuadaRegion(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION, blank=True, default='no-responde', verbose_name='Ambiente')
    cantidad = models.IntegerField(VERBOSE_CANTIDAD, blank=True, default=0)
    viol_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    ssr = models.IntegerField('Salud sexual y repro.', blank=True, default=0)
    ssr_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    vih_sida = models.IntegerField('VIH-SIDA', blank=True, default=0)
    vih_sida_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    masculinidad = models.IntegerField('Masculinidad', blank=True, default=0)
    masc_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    div_sexual = models.IntegerField('Div. sexual', blank=True, default=0)
    div_sexual_part = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    equidad = models.IntegerField('Equidad de género', blank=True, default=0)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acciones impulsadas: Ambiente de accion'
        verbose_name_plural = 'Acciones impulsadas: Ambiente de acciones'

class AccionEfectuadaDocumento(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_DOCS, blank=True, default='no-responde')
    cantidad = models.IntegerField(VERBOSE_CANTIDAD, blank=True, default=0)
    viol_aprob = models.IntegerField('Aprobadas', blank=True, default=0)
    ssr = models.IntegerField('Salud sexual y repro.', blank=True, default=0)
    ssr_aprob = models.IntegerField('Aprobadas', blank=True, default=0)
    vih_sida = models.IntegerField('VIH-SIDA', blank=True, default=0)
    vih_aprob = models.IntegerField('Aprobadas', blank=True, default=0)
    masculinidad = models.IntegerField('Masculinidad', blank=True, default=0)
    masc_aprob = models.IntegerField('Aprobadas', blank=True, default=0)
    div_sexual = models.IntegerField('Div. sexual', blank=True, default=0)
    div_aprob = models.IntegerField('Aprobadas', blank=True, default=0)
    equidad = models.IntegerField('Equidad de género', blank=True, default=0)
    participantes = models.IntegerField('Aprobadas', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acciones impulsadas: Efectividad de accion'
        verbose_name_plural = 'Acciones impulsadas: Efectividad de acciones'

class ParticipacionComisionDecision(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION, blank=True, default='no-responde')
    cantidad_instancias = models.IntegerField('Número de instancias donde participan para mejorar la toma de decisiones sobre DDSSRR y equidad', blank=True, default=0)
    cantidad_acciones_promovidas = models.IntegerField('Número de acciones promovidas para mejorar la toma de decisiones sobre DDSSRR y equidad', blank=True, default=0)
    cantidad_acciones_efectivas = models.IntegerField('Número de acciones efectivas para mejorar la toma de decisiones sobre DDSSRR y equidad generando cambios', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Participacion en instancias: Participacion y Efectividad'
        verbose_name_plural = 'Participacion en instancias: Participacion y Efectividad'

#TABLA MARCADA PARA SER HECHA MIERDA
""""class ParticipacionComisionAgenda(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION, blank=True, default='no-responde')
    cantidad_instancias = models.IntegerField('Número de instancias donde ' \
                                              'participan para mantener en la agenda pública la defensa DDSSRR', db_column='cat_instancias', blank=True, default=0)
    cantidad_acciones_prom = models.IntegerField('Número de acciones promovidas ' \
                                                 'para mantener en la agenda pública la defensa DDSSRR', db_column='cant_acc_prom', blank=True, default=0)
    cantidad_acciones_efec = models.IntegerField('Número de acciones efectivas para mantener ' \
                                                 'en la agenda pública la defensa DDSSRR y generar cambios', db_column='cant_acc_efec', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Defensa de los DDSSRR: Participación y efectividad'
        verbose_name_plural = 'Defensa de los DDSSRR: Participación y efectividad'"""

class AccionObservatorio(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION, blank=True, default='no-responde')
    cantidad_observatorios = models.IntegerField('Número de observatorios funcionando para la vigilancia de la restitución, creación y aplicación de leyes, políticas, acciones y servicios en torno a los DDSSRR', blank=True, default=0)
    cantidad_acciones_realiz = models.IntegerField('Número de acciones realizadas en marco de los observatorios', blank=True, default=0)
    cantidad_acciones_web = models.IntegerField('Número de acciones visibilizadas, divulgadas y colocadas en la página web de FED', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Observatorio para vigilancia'
        verbose_name_plural = 'Observatorios para vigilancia'

ver_vif = 'En contra de la violencia intrafamiliar'
ver_sexual = 'En contra de la discriminación a personas de la diversidad sexual'
ver_discapacidad = 'En contra de la discriminación a personas con discapacidad'
ver_vih_sida = 'En contra de la discriminación a personas que viven con VIH y SIDA'
ver_racial = 'En contra de la discriminación a personas de población étnica e indigena'
ver_joven = 'En contra de la discriminación de jóvenes'

CHOICE_MEDIO_1 = (('foros', 'Foros'),
                ('campania_tv', 'Campañas en televisión'),
                ('campania_radio', 'Campañas en radio'),
                ('marchas', 'Marchas'))


class DenunciaSocialRealizada(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO_1, blank=True, default='no-responde', verbose_name='Número de acciones públicas realizadas')
    #campo eliminado a peticion de FED
    #persona_violencia_if = models.IntegerField(ver_vif, blank=True, default=0)
    persona_div_sexual = models.IntegerField(ver_sexual, blank=True, default=0)
    persona_discapacidad = models.IntegerField(ver_discapacidad, blank=True, default=0)
    persona_vih = models.IntegerField(ver_vih_sida, blank=True, default=0)
    persona_racial = models.IntegerField(ver_racial, blank=True, default=0)
    persona_joven = models.IntegerField(ver_joven, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia pública realizada'
        verbose_name_plural = 'Denuncias públicas realizadas'

"""class DenunciaSocialEfectiva(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO, blank=True, default='no-responde')
    persona_violencia_if = models.IntegerField(ver_vif, blank=True, default=0)
    persona_div_sexual = models.IntegerField(ver_sexual, blank=True, default=0)
    persona_discapacidad = models.IntegerField(ver_discapacidad, blank=True, default=0)
    persona_vih = models.IntegerField(ver_vih_sida, blank=True, default=0)
    persona_racial = models.IntegerField(ver_racial, blank=True, default=0)
    persona_joven = models.IntegerField(ver_joven, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia pública efectiva'
        verbose_name_plural = 'Denuncias públicas efectivas'"""

CHOICE_JURIDICA = (('denuncia_juridica_realizada', 'Denuncias jurídicas realizadas ante instancias'),
                   ('denuncia_juridica_atendida', 'Denuncias jurídicas atendidas'),)

class DenunciaJuridica(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_JURIDICA, blank=True, default='no-responde', verbose_name='Número de acciones de denuncias efectivas impulsadas por las organizaciones')
    #eliminar por disposición de fe
    #violencia_if = models.IntegerField(ver_vif, blank=True, default=0)
    persona_div_sexual = models.IntegerField(ver_sexual, blank=True, default=0)
    persona_discapacidad = models.IntegerField(ver_discapacidad, blank=True, default=0)
    persona_vih = models.IntegerField(ver_vih_sida, blank=True, default=0)
    persona_racial = models.IntegerField(ver_racial, blank=True, default=0)
    persona_joven = models.IntegerField(ver_joven, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

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
                    ('reunion_comunitaria', 'Reuniones comunitarias'),
                    ('feria_informativa', 'Feria informativa'),
                    ('cine_foros_videos', 'Cineforos / Videos reflexivos'),
                    ('murales', 'Murales'),
                    ('liga_saber', 'Liga del saber'),
                    ('vinetas_espacios', 'Viñetas y espacios radiales'),
                    ('campanas_mantas', 'Campañas / Mantas'),
                    ('cabildeo', 'Cabildeo'),
                    ('boletines', 'Boletines'))

class InvolucramientoPobMeta(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS_REFLEXION, blank=True, default='no-responde', verbose_name='Acciones realizadas para que las poblaciones meta reflexionen sobre los derechos sexuales y reproductivos')
    prev_vio = models.IntegerField('Prevención de violencia', blank=True, default=0)
    ssr = models.IntegerField('Salud sexual y salud reproductiva', blank=True, default=0)
    vih_sida = models.IntegerField('VIH-SIDA', blank=True, default=0)
    masculinidad = models.IntegerField('Masculinidad', blank=True, default=0)
    div_sexual = models.IntegerField('Diversidad sexual', blank=True, default=0)
    equidad = models.IntegerField('Equidad de género', blank=True, default=0)
    total = models.IntegerField('Global', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Involucramiento de pob. meta'
        verbose_name_plural = 'Involucramiento de pob. metas'

class AccionRealizadaReflexion(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS_REFLEXION, blank=True, default='no-responde')
    mujeres = models.IntegerField('Mujeres', blank=True, default=0)
    hombres = models.IntegerField('Hombres', blank=True, default=0)
    jovenes = models.IntegerField('Los y las jóvenes', blank=True, default=0)
    div_sexual = models.IntegerField('Personas de la diversidad sexual', blank=True, default=0)
    vih = models.IntegerField('Personas con VIH y SIDA', blank=True, default=0)
    etnica = models.IntegerField('Personas de población étnica e indigena', blank=True, default=0)
    discapacidad = models.IntegerField('Personas con discapacidad', blank=True, default=0)
    total = models.IntegerField('Global', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción realizada para reflexión de poblabión meta'
        verbose_name_plural = 'Acciones realizadas para reflexión de poblabiones meta'


PERSONAS_REFLEXION = (('personas_participaron', 'No. de participantes acciones derechos sexuales'),
                      ('personas_participaron_toman_decision', 'No. participantes toman decisiones sex.'),)

"""
class AccionRelizadaReflexionPersona(models.Model):
    accion = models.CharField(max_length=100, choices=PERSONAS_REFLEXION, blank=True, default='no-responde')
    mujeres = models.IntegerField('Las mujeres', blank=True, default=0)
    hombres = models.IntegerField('Los hombres', blank=True, default=0)
    jovenes = models.IntegerField('Los y las jóvenes', blank=True, default=0)
    div_sexual = models.IntegerField('Las personas de la diversidad sexual', blank=True, default=0)
    vih = models.IntegerField('Las personas con VIH y SIDA', blank=True, default=0)
    etnica = models.IntegerField('Las personas de población étnica e indigena', blank=True, default=0)
    discapacidad = models.IntegerField('Las personas con discapacidad', blank=True, default=0)
    total = models.IntegerField('Global', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Cambio en la población meta'
        verbose_name_plural = 'Cambios en las poblaciones metas'"""

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
           ('consejeria', 'Consejería y promotoría social'),)

class AccionImpulsadaOrg(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS2, blank=True, default='no-responde', verbose_name='Tipo de acciones')
    acciones_emprendidas = models.IntegerField('Número de acciones emprendidas por las organizaciones para la prevención de la violencia basada en género', blank=True, default=0)
    #eliminada a solicitud de FED
    #acciones_cambios_actitud = models.IntegerField('Número de acciones que lograron cambios de actitud de los grupos metas para la prevención de violencia basada en género', blank=True, default=0)
    acciones_impulsadas_masculinidad = models.IntegerField('Numero y tipo de acciones impulsadas por las Org. para promover masculinidad libre de prejuicios y violencia', blank=True, default=0)
    #eliminada a solicitud de FED
    #acciones_cambios_masculinidad = models.IntegerField('Numero de acciones que lograron cambio de actitud de los grupos metas hacia la masculinidad libre de prejuicios y violencia', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impulsada por organización para prev. de violencia '
        verbose_name_plural = 'Acciones impulsadas por organizaciones para prev. de violencia'

class AccionImpulsadaGrupo(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS2, blank=True, default='no-responde', verbose_name='Tipo de acciones')
    acciones_emprendidas_sex = models.IntegerField('Número y tipo de acciones emprendidas por los grupos de diversidad sexual, para prevención de violencia basada en género', blank=True, default=0)
    #acciones_cambio_sex = models.IntegerField('Numero de acciones que lograron cambio de actitud en grupo de diversidad sexual', blank=True, default=0)
    acciones_emprendidas_discapa = models.IntegerField('Número y tipo de acciones emprendidas por los grupos de personas con discapacidad para prevención de violencia basada en género', blank=True, default=0)
    #acciones_cambio_discapa = models.IntegerField('Número de acciones que lograron cambio de actitud en grupo de personas con discapacidad', blank=True, default=0)
    acciones_emprendidas_etnia = models.IntegerField('Número de acciones emprendidas por los grupos étnicos y pueblos indígenas para la prevención de la violencia basada en género', blank=True, default=0)
    #acciones_cambio_etnia = models.IntegerField('Número de acciones que lograron cambio de actitud en grupos étnicos y pueblos indígenas', blank=True, default=0)
    acciones_emprendidas_jovenes = models.IntegerField('Número de acciones emprendidas por los y las jóvenes para la prevención de la violencia basada en género', blank=True, default=0)
    #acciones_cambio_jovenes = models.IntegerField('Número de acciones que lograron cambio de actitud en los y las jóvenes ', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impulsada por grupos para prev. de violencia'
        verbose_name_plural = 'Acciones impulsadas por grupos para prev. de violencia'

ATENCION_SALUD = (('general', 'Atención general'),
                  ('especializada', 'Atención especializada'))
                  

class AtencionSalud(models.Model):
    accion = models.CharField(max_length=100, choices=ATENCION_SALUD, blank=True, default='no-responde', verbose_name='Atención a la Salud Sexual y Reproductiva')
    mujeres = models.IntegerField('Mujeres', blank=True, default=0)
    hombres = models.IntegerField('Hombres', blank=True, default=0)
    jovenes = models.IntegerField('Los y las jóvenes', blank=True, default=0)
    div_sexual = models.IntegerField('Personas de la diversidad sexual', blank=True, default=0)
    vih = models.IntegerField('Personas con VIH y SIDA', blank=True, default=0)
    etnica = models.IntegerField('Personas de población étnica e indigena', blank=True, default=0)
    discapacidad = models.IntegerField('Personas con discapacidad', blank=True, default=0)
    total = models.IntegerField('Global', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Atención a la salud sexual y reprod'
        verbose_name_plural = 'Atenciones a la salud sexual y reprod'

CHOICE_VICTIMAS = (('casos_atendidos', 'No. casos de victimas de violencia de género atendidos'),
                   ('casos_resueltos', 'No. casos resueltos con resultados y diagnósticos favorables'), )

class AtencionVictima(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_VICTIMAS, blank=True, default='no-responde', verbose_name='Acciones')
    #servicio_salud = models.IntegerField('A través de los servicios de salud general', blank=True, default=0)
    #servicio_salud_especial = models.IntegerField('A través de los servicios de salud especializada', blank=True, default=0)
    servicio_psicologia = models.IntegerField('A través de los servicios de atención en psicología', blank=True, default=0)
    servicio_legal = models.IntegerField('A través de los servicios de atención legal', blank=True, default=0)
    #atencion_social = models.IntegerField('Atención social', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Atención victimas de violencia'
        verbose_name_plural = 'Atenciones a victimas de violencia'

CHOICE_DENUNCIAS = (('denuncias_interpuestas', 'No. denuncias interpuestas por las víctimas a instancias de justicia'),
                    ('denuncias_recibidas', 'No. denuncias interpuestas por las victimas que han sido recibidas y atendidas'),
                    ('denuncias_sancion', 'No. de casos que concluyen con sanción penal'), )

class DenunciaViolencia(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_DENUNCIAS, blank=True, default='no-responde')
    comisariato = models.IntegerField('Comisaría de la Mujer', blank=True, default=0)
    fiscalia = models.IntegerField('Fiscalía', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia interpuesta'
        verbose_name_plural = 'Denuncias interpuestas'

CHOICE_ALBERGUES = (('vitimas_atendidas', 'No. victimas de violencia de género atendidas'),
                    ('casos_logrados', 'No. de casos quienes logran nuevos proyectos de vida'),)

class AtencionVictimaAlbergue(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_ALBERGUES, blank=True, default='no-responde')
    mujeres = models.IntegerField(blank=True, default=0)
    jovenes = models.IntegerField('Jóvenes', blank=True, default=0)
    ninos_ninas = models.IntegerField('Niños y Niñas', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Atención de victima en Albergue'
        verbose_name_plural = 'Atención de victimas en Albergues'

CHOICE_REF = (('referencia_realiza', 'Número de referencias y contra-referencias'),
              ('contra_ref_atendidas', 'Número de contra-referencias atendidas'),)

class ReferenciaContraRef(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REF, blank=True, default='no-responde')
    mujeres = models.IntegerField(blank=True, default=0)
    jovenes = models.IntegerField('Jóvenes', blank=True, default=0)
    ninos_ninas = models.IntegerField('Niños y Niñas', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Referencia y contra-referencia'
        verbose_name_plural = 'Referencias y contra-referencias'

#AQUI EMPIEZA EL NUEVO OBJETIVO

MEDIOS3 = (('talleres', 'Talleres'),
           ('foros', 'Foros'),
           ('intercambio_xp', 'Intercambio de experiencias'),
           ('asesoria', 'Asesoría especializada'),
           ('estudios', 'Estudios colectivos'),
           ('visitas', 'Visitas de seguimiento'),)

class AccionPromuevenIntercambio(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS3, blank=True, default='no-responde')
    acciones_org_part = models.IntegerField('Número de acciones donde la organización participó para promover el intercambio y gestión de conocimientos entre OSC', blank=True, default=0)
    participantes = models.IntegerField('Número de participantes por parte de la organización en las acciones del intercambio y gestión d conocimiento entre las OSC', blank=True, default=0)
    acciones_efectivas = models.IntegerField('Número de acciones que fueron efectivas para promover el intercambio y la gestión de conocimiento entre las OSC', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Intercambio teorico y metodológico'
        verbose_name_plural = 'Intercambios teoricos y metodológicos'

class AccionFortaleceCapacidad(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS3, blank=True, default='no-responde')
    acciones = models.IntegerField('Número de acciones para fortalecer las capacidades de las organizaciones para medir y reportar los indicadores propuestos', blank=True, default=0)
    participantes = models.IntegerField('Número de participantes de la organización en las acciones para fortalecer las capacidades para medir y reportar los indicadores propuestos', blank=True, default=0)
    acciones_efectivas = models.IntegerField('Número de acciones que fueron efectivas para fortalecer las capacidades de las organizaciones para medir y repotar los indicadores propuestos', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Medir y reportar indicador'
        verbose_name_plural = 'Medir y reportar indicadores'

class EstadoCapacidadAdmitiva(models.Model):
    sistema = models.CharField(max_length=100, choices=CHOICE1, verbose_name='Cuenta con un sistema admitivo contable', blank=True, default='no-responde')
    plan = models.CharField(max_length=100, choices=CHOICE2, verbose_name='Utilizan su plan estratégico para mejorar sus capacidades de gestión en desarrollo de proyectos, consecusión y ejecución de recursos, comunicación', blank=True, default='no-responde')
    organizaciones = models.CharField(max_length=100, choices=CHOICE3, verbose_name='Organizaciones de la diversidad sexual han obtenido la personería jurídica por el apoyo de la organización', blank=True, default='no-responde')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.sistema
    
    class Meta:
        verbose_name = 'Organizacion con sistema administrativo'
        verbose_name_plural = 'Organizaciones con sistema administrativo'

CHOICE4 = (('talleres', 'Talleres'),
           ('intercambio_xp', 'Intercambio de experiencias'),
           ('asesoria', 'Asesoría especializada'),
           ('pasantia', 'Pasantía'),
           ('visitas', 'Visitas de seguimiento'), )

class AccionFortaleceCapAdmitiva(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE4, blank=True, default='no-responde')
    mejorar_sistema = models.IntegerField('Para mejorar el sistema administratico contable', blank=True, default=0)
    mejorar_plan = models.IntegerField('Para mejorar el plan estratégico y gestión de proyectos a partir del plan estratégico', blank=True, default=0)
    mejorar_apoyo = models.IntegerField('Para apoyar la obtención de personería jurídica de las organizaciones de la diversidad sexual', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción para mejorar la gestión'
        verbose_name_plural = 'Acciones para mejorar la gestión'



    

