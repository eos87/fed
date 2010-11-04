# -*- coding: UTF-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from fed.lugar.models import Departamento
from fed.lugar.models import Municipio


CHOICE_MEDIO = (('estudios', 'Estudios'),
                ('foros', 'Foros'),
                ('cabildos', 'Cabildeos'),
                ('campania_tv', 'Campañas en televisión'),
                ('campania_radio', 'Campañas en radio'),
                ('talleres', 'Talleres de formación'),
                ('manifestaciones', 'Manifestaciones'),
                ('reuniones', 'Reuniones'), )

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

VERBOSE_CANTIDAD = 'Número de acciones efectuadas para fomentar la existencia y aplicación efectiva de políticas públicas para posicionar el tema de la equidad e igualdad'
VERBOSE_PARTICIPAN = 'Participantes en las acciones'

class Organizacion(models.Model):
    nombre = models.TextField()
    nombre_corto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    correo = models.EmailField(blank=True, default='example@example.com')
    contacto = models.CharField(max_length=200, blank=True, default='Ninguno')
    telefono = models.CharField(max_length=200, blank=True, default='Ninguno')
    antecedentes = models.TextField()

    def __unicode__(self):
        return self.nombre_corto

    class Meta:
        verbose_name_plural = 'Organizaciones'

class Proyecto(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    nombre = models.TextField()
    codigo = models.CharField(max_length=150, null=True, blank=True)    
    cobertura = models.TextField(verbose_name='Area de cobertura')
    duracion = models.CharField(max_length=30)
    monto = models.CharField('Monto solicitado a FED', null=True, blank=True, max_length=100)
    monto2 = models.CharField('Monto de contrapartida', null=True, blank=True, max_length=100)


    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Proyectos'

CHOICE_PERIODO = ((0, 'Primer trimestre'),
                  (1, 'Segundo trimestre'),
                  (2, 'Tercer trimestre'),
                  (3, 'Cuarto trimestre'))
                  
CHOICE_ANIO = (('2010', '2010'), ('2011', '2011'), ('2012', '2012'))

class Encuesta(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    proyecto = models.ForeignKey(Proyecto)
    periodo = models.IntegerField(choices=CHOICE_PERIODO, verbose_name='Período de informe')
    anio = models.CharField(choices=CHOICE_ANIO, verbose_name='Año', max_length=100)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '%s | %s | %s | %s' % (self.organizacion.nombre, self.proyecto.nombre, CHOICE_PERIODO[int(self.periodo)][1], self.anio)

    def get_periodo(self):
        return CHOICE_PERIODO[self.periodo][1]

    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'

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

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Indicador, self).save(force_insert, force_update)

class ResultadoTrabajado(models.Model):
    resultado = models.ForeignKey(Resultado)    
    municipio = models.ManyToManyField(Municipio)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.resultado.nombre

    class Meta:
        verbose_name = 'Resultado trabajado'
        verbose_name_plural = 'Resultados trabajados'

class AccionEfectuadaMedio(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO, blank=True, default='no-responde')
    cantidad = models.IntegerField(VERBOSE_CANTIDAD, blank=True, default=0)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acciones impulsadas: Tipo de accion'
        verbose_name_plural = 'Acciones impulsadas: Tipo de acciones'

class AccionEfectuadaRegion(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION, blank=True, default='no-responde')
    cantidad = models.IntegerField(VERBOSE_CANTIDAD, blank=True, default=0)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN, blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acciones impulsadas: Ambiente de accion'
        verbose_name_plural = 'Acciones impulsadas: Ambiente de acciones'

class AccionEfectuadaDocumento(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_DOCS, blank=True, default='no-responde')
    cantidad = models.IntegerField('Número de iniciativas promovidas para posicionar el tema de la equidad e igualdad', blank=True, default=0)
    participantes = models.IntegerField('Numero de iniciativas aprobadas e implementadas para posicionar el tema de la equidad e igualdad', blank=True, default=0)
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

class ParticipacionComisionAgenda(models.Model):
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
        verbose_name_plural = 'Defensa de los DDSSRR: Participación y efectividad'

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

ver_sexual = 'En contra de la discriminación a personas de la diversidad sexual'
ver_discapacidad = 'En contra de la discriminación a personas con discapacidad'
ver_vih_sida = 'En contra de la discriminación a personas que viven con VIH y SIDA'
ver_racial = 'En contra de la discriminación a personas de población étnica e indigena'
ver_joven = 'En contra de la discriminación a personas de juventud'

class DenunciaSocialRealizada(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO, blank=True, default='no-responde')
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

class DenunciaSocialEfectiva(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO, blank=True, default='no-responde')
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
        verbose_name_plural = 'Denuncias públicas efectivas'

CHOICE_JURIDICA = (('denuncia_juridica_realizada', 'Número de acciones de denuncias jurídicas realizadas'),
                   ('denuncia_juridica_atendida', 'Número de denuncias jurídicas atendidas'),)

class DenunciaJuridica(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_JURIDICA, blank=True, default='no-responde')
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
                    ('reunion_comunitaria', 'Reuniones comunitarias'),)

class AccionRealizadaReflexion(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS_REFLEXION, blank=True, default='no-responde')
    mujeres = models.IntegerField('Con las mujeres', blank=True, default=0)
    hombres = models.IntegerField('Con los hombres', blank=True, default=0)
    jovenes = models.IntegerField('Con los y las jóvenes', blank=True, default=0)
    div_sexual = models.IntegerField('Con las personas de la diversidad sexual', blank=True, default=0)
    vih = models.IntegerField('Con las personas con VIH y SIDA', blank=True, default=0)
    etnica = models.IntegerField('Con las personas de población étnica e indigena', blank=True, default=0)
    discapacidad = models.IntegerField('Con las personas con discapacidad', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción realizada para reflexión de poblabión meta'
        verbose_name_plural = 'Acciones realizadas para reflexión de poblabiones meta'
        
PERSONAS_REFLEXION = (('personas_participaron', 'No. de participantes acciones derechos sexuales'),
                      ('personas_participaron_toman_decision', 'No. participantes toman decisiones sex.'),)

class AccionRelizadaReflexionPersona(models.Model):
    accion = models.CharField(max_length=100, choices=PERSONAS_REFLEXION, blank=True, default='no-responde')
    mujeres = models.IntegerField('Las mujeres', blank=True, default=0)
    hombres = models.IntegerField('Los hombres', blank=True, default=0)
    jovenes = models.IntegerField('Los y las jóvenes', blank=True, default=0)
    div_sexual = models.IntegerField('Las personas de la diversidad sexual', blank=True, default=0)
    vih = models.IntegerField('Las personas con VIH y SIDA', blank=True, default=0)
    etnica = models.IntegerField('Las personas de población étnica e indigena', blank=True, default=0)
    discapacidad = models.IntegerField('Las personas con discapacidad', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Cambio en la población meta'
        verbose_name_plural = 'Cambios en las poblaciones metas'

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
    accion = models.CharField(max_length=100, choices=MEDIOS2, blank=True, default='no-responde')
    acciones_emprendidas = models.IntegerField('Número de acciones emprendidas por las Org. para la prevención de la violencia basada en género', blank=True, default=0)
    acciones_cambios_actitud = models.IntegerField('Número de acciones que lograron cambios de actitud de los grupos metas para la prevención de violencia basada en género', blank=True, default=0)
    acciones_impulsadas_masculinidad = models.IntegerField('Numero y tipo de acciones impulsadas por las Org. para promover masculinidad libre de prejuicios y violencia', blank=True, default=0)
    acciones_cambios_masculinidad = models.IntegerField('Numero de acciones que lograron cambio de actitud de los grupos metas hacia la masculinidad libre de prejuicios y violencia', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impulsada por organización para prev. de violencia '
        verbose_name_plural = 'Acciones impulsadas por organizaciones para prev. de violencia'

class AccionImpulsadaGrupo(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS2, blank=True, default='no-responde')
    acciones_emprendidas_sex = models.IntegerField('Número y tipo de acciones emprendidas por los grupos de diversidad sexual, para prev de violencia basada en género', blank=True, default=0)
    acciones_cambio_sex = models.IntegerField('Numero de acciones que lograron cambio de actitud en grupo de diversidad sexual', blank=True, default=0)
    acciones_emprendidas_discapa = models.IntegerField('Número y tipo de acciones emprendidas por los grupos de personas con discapacidad para prev de violencia basada en género', blank=True, default=0)
    acciones_cambio_discapa = models.IntegerField('Número de acciones que lograron cambio de actitud en grupo de personas con discapacidad', blank=True, default=0)
    acciones_emprendidas_etnia = models.IntegerField('Número de acciones emprendidas por los grupos étnicos y pueblos indígenas para la prevención de la violencia basada en género', blank=True, default=0)
    acciones_cambio_etnia = models.IntegerField('Número de acciones que lograron cambio de actitud en grupos étnicos y pueblos indígenas', blank=True, default=0)
    acciones_emprendidas_jovenes = models.IntegerField('Número de acciones emprendidas por los y las jóvenes para la prevención de la violencia basada en género', blank=True, default=0)
    acciones_cambio_jovenes = models.IntegerField('Número de acciones que lograron cambio de actitud en los y las jóvenes ', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impulsada por grupos para prev. de violencia'
        verbose_name_plural = 'Acciones impulsadas por grupos para prev. de violencia'

CHOICE_VICTIMAS = (('casos_atendidos', 'No. casos de victimas de violencia de género atendidos'),
                   ('casos_resueltos', 'No. casos resueltos con resultados y diagnósticos favorables'), )

class AtencionVictima(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_VICTIMAS, blank=True, default='no-responde')
    servicio_salud = models.IntegerField('A través de los servicios de atención en salud', blank=True, default=0)
    servicio_psicologia = models.IntegerField('A través de los servicios de atención en psicología', blank=True, default=0)
    servicio_legal = models.IntegerField('A través de los servicios de atención legal', blank=True, default=0)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Atención victimas de violencia'
        verbose_name_plural = 'Atenciones a victimas de violencia'

CHOICE_DENUNCIAS = (('denuncias_interpuestas', 'No. denuncias interpuestas a instancias de justicia '),
                    ('denuncias_recibidas', 'No. denuncias que han sido recibidas y atendidas'),
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

CHOICE1 = (('si_hay', 'Si hay'), ('hay_pero', 'Hay un sistema pero no es eficiente'), ('no_hay', 'No hay'), )
CHOICE2 = (('si_hay', 'Si hay'), ('hay_pero', 'Hay un plan estratégico, pero no se utiliza'), ('no_hay', 'No hay'),)
CHOICE3 = (('ninguna', 'Ninguna'), ('proceso', 'En proceso'), ('logrado', 'Logrado'), )

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



    

