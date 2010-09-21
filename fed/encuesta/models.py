# -*- coding: UTF-8 -*-

from django.db import models
from fed.lugar.models import Municipio, Departamento

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
    descripcion = models.TextField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Proyectos'

class Encuesta(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    proyecto = models.ForeignKey(Proyecto)
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio del período de informe')
    fecha_fin = models.DateField(verbose_name='Fecha final del período de informe')

class Resultado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Resultados'

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
    accion = models.CharField(max_length=100, choices=CHOICE_MEDIO)
    cantidad = models.IntegerField(VERBOSE_CANTIDAD)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción efectuada según medio'
        verbose_name_plural = 'Acciones efectuadas según medio'

class AccionEfectuadaRegion(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REGION)
    cantidad = models.IntegerField(VERBOSE_CANTIDAD)
    participantes = models.IntegerField(VERBOSE_PARTICIPAN)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción efectuada por región afectada'
        verbose_name_plural = 'Acciones efectuadas por regiones afectadas'

class AccionEfectuadaDocumento(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_DOCS)
    cantidad = models.IntegerField('Número de iniciativas promovidas para posicionar el tema de la equidad e igualdad')
    participantes = models.IntegerField('Numero de iniciativas aprobadas e implementadas para posicionar el tema de la equidad e igualdad')
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción realizada para reflexión de pob'
        verbose_name_plural = 'Acciones realizadas para reflexión de pob'
        
PERSONAS_REFLEXION = (('personas_participaron', 'No. de participantes acciones derechos sexuales'),
                      ('personas_participaron_toman_decision', 'No. participantes toman decisiones sex.'), )

class AccionRelizadaReflexionPersona(models.Model):
    accion = models.CharField(max_length=100, choices=PERSONAS_REFLEXION)
    mujeres = models.IntegerField('Las mujeres')
    hombres = models.IntegerField('Los hombres')
    jovenes = models.IntegerField('Los y las jóvenes')
    div_sexual = models.IntegerField('Las personas de la diversidad sexual')
    vih = models.IntegerField('Las personas con VIH y SIDA')
    etnica = models.IntegerField('Las personas de población étnica e indigena')
    discapacidad = models.IntegerField('Las personas con discapacidad')
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

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
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción impulsada por grupos'
        verbose_name_plural = 'Acciones impulsadas por grupos'

CHOICE_VICTIMAS = (('casos_atendidos', 'No. casos de victimas de violencia de género atendidos'),
                   ('casos_resueltos', 'No. casos resueltos con resultados y diagnósticos favorables'),)

class AtencionVictima(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_VICTIMAS)
    servicio_salud = models.IntegerField('A través de los servicios de atención en salud')
    servicio_psicologia = models.IntegerField('A través de los servicios de atención en psicología')
    sevicio_legal = models.IntegerField('A través de los servicios de atención legal')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Atención de victimas x/violencia'
        verbose_name_plural = 'Atenciones de victimas x/violencia'

CHOICE_DENUNCIAS = (('denuncias_interpuestas', 'No. denuncias interpuestas a instancias de justicia '),
                    ('denuncias_recibidas', 'No. denuncias que han sido recibidas y atendidas'),
                    ('denuncias_sancion', 'No. casos que concluyen con sanción penal'),)

class DenunciaViolencia(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_DENUNCIAS)
    comisariato = models.IntegerField('Comisariato Policía')
    fiscalia = models.IntegerField('Fiscalía')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Denuncia por violencia de género'
        verbose_name_plural = 'Denuncias por violencia de género'

CHOICE_ALBERGUES = (('vitimas_atendidas', 'No. victimas de violencia de género atendidas'),
                    ('casos_logrados', 'No. de casos quienes logran nuevos proyectos de vida'), )

class AtencionVictimaAlbergue(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_ALBERGUES)
    mujeres = models.IntegerField()
    jovenes = models.IntegerField('Jóvenes')
    ninos_ninas = models.IntegerField('Niños y Niñas')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Atención de casos en Albergues'
        verbose_name_plural = 'Atenciones de casos en Albergues'

CHOICE_REF = (('referencia_realiza', 'Número de referencias y contra-referencias'),
              ('contra_ref_atendidas', 'Número de contra-referencias atendidas'), )

class ReferenciaContraRef(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE_REF)
    mujeres = models.IntegerField()
    jovenes = models.IntegerField('Jóvenes')
    ninos_ninas = models.IntegerField('Niños y Niñas')
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
           ('visitas', 'Visitas de seguimiento'), )

class AccionPromuevenIntercambio(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS3)
    acciones_org_part = models.IntegerField('Número de acciones donde la organización participó para promover el intercambio y gestión de conocimientos entre OSC')
    participantes = models.IntegerField('Número de participantes por parte de la organización en las acciones del intercambio y gestión d conocimiento entre las OSC')
    acciones_efectivas = models.IntegerField('Número de acciones que fueron efectivas para promover el intercambio y la gestión de conocimiento entre las OSC')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción que promueve el intercambio'
        verbose_name_plural = 'Acciones que promueven el intercambio'

class AccionFortaleceCapacidad(models.Model):
    accion = models.CharField(max_length=100, choices=MEDIOS3)
    acciones = models.IntegerField('Número de acciones para fortalecer las capacidades de las organizaciones para medir y reportar los indicadores propuestos')
    participantes = models.IntegerField('Número de participantes de la organización en las acciones para fortalecer las capacidades para medir y reportar los indicadores propuestos')
    acciones_efectivas = models.IntegerField('Número de acciones que fueron efectivas para fortalecer las capacidades de las organizaciones para medir y repotar los indicadores propuestos')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción p/fortalecer capacidad'
        verbose_name_plural = 'Acciones p/fortalecer capacidades'

CHOICE1 = (('si_hay', 'Si hay'), ('hay_pero', 'Hay un sistema pero no es eficiente'), ('no_hay', 'No hay'),)
CHOICE2 = (('si_hay', 'Si hay'), ('hay_pero', 'Hay un plan estratégico, pero no se utiliza'), ('no_hay', 'No hay'), )
CHOICE3 = (('ninguna', 'Ninguna'), ('proceso', 'En proceso'), ('logrado', 'Logrado'),)

class EstadoCapacidadAdmitiva(models.Model):
    sistema = models.CharField(max_length=100, choices=CHOICE1, verbose_name='Cuenta con un sistema admitivo contable')
    plan = models.CharField(max_length=100, choices=CHOICE2, verbose_name='Utilizan su plan estratégico para mejorar sus capacidades de gestión en desarrollo de proyectos, consecusión y ejecución de recursos, comunicación')
    organizaciones = models.CharField(max_length=100, choices=CHOICE3, verbose_name='Organizaciones de la diversidad sexual han obtenido la personería jurídica por el apoyo de la organización')
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = 'Estado capacidad admitiva'
        verbose_name_plural = 'Estado capacidad admitiva'

CHOICE4 = (('talleres', 'Talleres'),
           ('intercambio_xp', 'Intercambio de experiencias'),
           ('asesoria', 'Asesoría especializada'),
           ('pasantia', 'Pasantía'),
           ('visitas', 'Visitas de seguimiento'),)

class AccionFortaleceCapAdmitiva(models.Model):
    accion = models.CharField(max_length=100, choices=CHOICE4)
    mejorar_sistema = models.IntegerField('Para mejorar el sistema administratico contable')
    mejorar_plan = models.IntegerField('Para mejorar el plan estratégico y gestión de proyectos a partir del plan estratégico')
    mejorar_apoyo = models.IntegerField('Para apoyar la obtención de personería jurídica de las organizaciones de la diversidad sexual')
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.accion

    class Meta:
        verbose_name = 'Acción para fortalecer capacidad'
        verbose_name_plural = 'Acciones p/fortalecer capacidad'



    

