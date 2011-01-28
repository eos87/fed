# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from models import *

class OrganizacionAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return Organizacion.objects.all()
        return Organizacion.objects.filter(user=request.user)

    def get_form(self, request, obj=None, ** kwargs):
        if request.user.is_superuser:
            form = super(OrganizacionAdmin, self).get_form(self, request, ** kwargs)
        else:
            form = super(OrganizacionAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
        return form

    list_filter = ['user']
    list_display = ['nombre_corto', 'user', 'correo', 'telefono', 'contacto']
    search_fields = ['nombre_corto', 'user__username', 'telefono', 'contacto']

class ProyectoAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return Proyecto.objects.all()
        return Proyecto.objects.filter(user=request.user)

    def get_form(self, request, obj=None, ** kwargs):
        if request.user.is_superuser:
            form = super(ProyectoAdmin, self).get_form(self, request, ** kwargs)
        else:
            form = super(ProyectoAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
        return form

    list_filter = ['user']
    list_display = ['nombre', 'user', 'organizacion']
    search_fields = ['nombre', 'user__username', 'organizacion__nombre', 'organizacion__nombre_corto']

admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Indicador)
#admin.site.register(AccionEfectuadaMedio)
#admin.site.register(AccionEfectuadaRegion)
#admin.site.register(AccionEfectuadaDocumento)
#admin.site.register(ParticipacionComisionDecision)
#admin.site.register(ParticipacionComisionAgenda)
#admin.site.register(DenunciaSocialRealizada)
#admin.site.register(DenunciaSocialEfectiva)
#admin.site.register(DenunciaJuridica)
#admin.site.register(AccionRealizadaReflexion)
#admin.site.register(InvolucramientoPobMeta)
#admin.site.register(AtencionSalud)
#admin.site.register(AccionRelizadaReflexionPersona)
#admin.site.register(AccionImpulsadaOrg)
#admin.site.register(AccionImpulsadaGrupo)
#admin.site.register(AtencionVictima)
#admin.site.register(DenunciaViolencia)
#admin.site.register(AtencionVictimaAlbergue)
#admin.site.register(ReferenciaContraRef)
#admin.site.register(AccionPromuevenIntercambio)
#admin.site.register(AccionFortaleceCapacidad)
#admin.site.register(EstadoCapacidadAdmitiva)
#admin.site.register(AccionFortaleceCapAdmitiva)
admin.site.register(Resultado)
#admin.site.register(ResultadoTrabajado)



class AccionEfectuadaMedioInline(admin.TabularInline):
    model = AccionEfectuadaMedio
    verbose_name_plural = 'Acciones efectuadas para fomentar la existencia y aplicación efectiva de políticas públicas para posicionar el tema de equidad e igualdad.'
    verbose_name = 'acción efectuada'
    extra = 1

class AccionEfectuadaRegionInline(admin.TabularInline):
    model = AccionEfectuadaRegion
    verbose_name_plural = 'Ambiente de acciones impulsadas.'
    verbose_name = 'ambiente de acción impulsada'
    extra = 1

class AccionEfectuadaDocumentoInline(admin.TabularInline):
    model = AccionEfectuadaDocumento
    verbose_name_plural = 'Acciones promovidas, aprobadas e implementadas para posicionar los diferentes temas.'
    verbose_name = 'acción promovida, aprobada e impulsada'
    extra = 1

class ParticipacionComisionDecisionInline(admin.TabularInline):
    model = ParticipacionComisionDecision
    verbose_name_plural = 'Participación en comisiones o instancias para coincidir sobre toma de decisiones sobre DDSSRR y equidad.'
    verbose_name = 'participación en comisión o instancia'
    extra = 1

#ESTA TABLA LA VAMOS A HACER MIERDA
"""class ParticipacionComisionAgendaInline(admin.TabularInline):
    model = ParticipacionComisionAgenda
    extra = 1"""

class AccionObservatorioInline(admin.TabularInline):
    model = AccionObservatorio
    verbose_name_plural = 'Acciones para observatorios para la vigilancia de la restitución, creación y aplicación de leyes, políticas, acciones y servicios en torno a los DDSSRR'
    verbose_name = 'acción para observatorio'
    extra = 1

class DenunciaSocialRealizadaInline(admin.TabularInline):
    model = DenunciaSocialRealizada
    verbose_name_plural = 'Acciones públicas y ante instancias del Estado de denuncia en contra de la discriminación.'
    verbose_name = 'acción pública y ante instancias'
    extra = 1

"""class DenunciaSocialEfectivaInline(admin.TabularInline):
    model = DenunciaSocialEfectiva
    extra = 1"""

class DenunciaJuridicaInline(admin.TabularInline):
    model = DenunciaJuridica
    verbose_name_plural = 'Acciones de denuncias efectivas en contra de la discriminación.'
    verbose_name = 'acción de denuncia efectiva'
    extra = 1

class InvolucramientoPobMetaInline(admin.TabularInline):
    model = InvolucramientoPobMeta
    verbose_name_plural = 'Población meta que recibe información que les permite tomar decisiones sexuales y reproductivas de manera autónoma y bien informada.'
    verbose_name = 'acción para reflexión de población meta'
    extra = 1

class AccionRealizadaReflexionInline(admin.TabularInline):
    model = AccionRealizadaReflexion
    verbose_name_plural = 'Personas que participaron en las acciones realizadas para reflexionar sobre los derechos sexuales y reproductivos.'
    verbose_name = 'acción'
    extra = 1

#eliminada esta tabla
"""
class AccionRelizadaReflexionPersonaInline(admin.TabularInline):
    model = AccionRelizadaReflexionPersona
    extra = 1"""

class AccionImpulsadaOrgInline(admin.TabularInline):
    model = AccionImpulsadaOrg
    verbose_name_plural = 'Acciones impulsadas por las organizaciones para la prevención de violencia basada en género.'
    verbose_name = 'acción impulsada'
    extra = 1

class AccionImpulsadaGrupoInline(admin.TabularInline):
    model = AccionImpulsadaGrupo
    verbose_name_plural = 'Acciones impulsadas por las organizaciones para la prevención de violencia basada en género con los grupos prioritarios.'
    verbose_name = 'acción impulsada'
    extra = 1

class AtencionSaludInline(admin.TabularInline):
    model = AtencionSalud
    verbose_name_plural = 'Casos atendidos por las organizaciones contrapartes de FED a través de los servicios de atención en salud.'
    verbose_name = 'Caso de atención'
    extra = 1

class AtencionVictimaInline(admin.TabularInline):
    model = AtencionVictima
    verbose_name_plural = 'Atención de casos de víctimas de violencia de género.'
    verbose_name = 'Caso de atención'
    extra = 1

class DenunciaViolenciaInline(admin.TabularInline):
    model = DenunciaViolencia
    verbose_name_plural = 'Denuncias interpuestas por las víctimas de violencia en las instancias que administran justicia'
    verbose_name = 'denuncia interpuesta'
    extra = 1

class AtencionVictimaAlbergueInline(admin.TabularInline):
    model = AtencionVictimaAlbergue
    verbose_name_plural = 'Atención de casos de víctimas de violencia de género en los albergues'
    verbose_name = 'atencion en albergues'
    extra = 1

class ReferenciaContraRefInline(admin.TabularInline):
    model = ReferenciaContraRef
    verbose_name_plural = 'Referencias y contra-referencias con instituciones públicas'
    verbose_name = 'referencia y contrareferencia'
    extra = 1

class AccionPromuevenIntercambioInline(admin.TabularInline):
    model = AccionPromuevenIntercambio
    extra = 1

class AccionFortaleceCapacidadInline(admin.TabularInline):
    model = AccionFortaleceCapacidad
    extra = 1

class EstadoCapacidadAdmitivaInline(admin.TabularInline):
    model = EstadoCapacidadAdmitiva
    max_num = 1

class AccionFortaleceCapAdmitivaInline(admin.TabularInline):
    model = AccionFortaleceCapAdmitiva
    extra = 1

class ResultadoTrabajadoInline(admin.TabularInline):
    model = ResultadoTrabajado
    filter_horizontal = ('municipio', )
    extra = 1

class DatoInformeOb3Inline(admin.StackedInline):
    class Media:
        css = {
            "all": ("/files/css/aux.css", )
        }
        
    model = DatoInformeOb3    
    filter_horizontal = ('organizacion', )
    verbose_name_plural = 'Actividades'
    verbose_name = 'Actividad'
    fieldsets = [
        (None, {'fields': ['tipo_accion', ('meta', 'fecha'), 'organizacion']}),
        ('Número de participantes', {'fields': [('hombres', 'mujeres')]}),
    ]
    extra = 1

class EncuestaAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/aux.css", )
        }
        #js = ('/files/js/jquery.min.js',
        #      '/files/js/filter.js')

    def queryset(self, request):
        grupos = request.user.groups.all()
        fed = Group.objects.get(name='FED')
        if request.user.is_superuser or fed in grupos:
            return Encuesta.objects.all()
        return Encuesta.objects.filter(user=request.user)

    def get_form(self, request, obj=None, ** kwargs):
        if request.user.is_superuser:
            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
        else:
            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
        return form
        
    save_on_top = True
    actions_on_top = True
    list_filter = ['organizacion', 'proyecto']
    list_display = ['organizacion', 'proyecto', 'periodo', 'anio', 'user']
    search_fields = ['organizacion__nombre', 'organizacion__nombre_corto', 'proyecto__nombre', 'proyecto__codigo', 'user__username']    
    inlines = [
        ResultadoTrabajadoInline,
        AccionEfectuadaMedioInline,
        AccionEfectuadaRegionInline,
        AccionEfectuadaDocumentoInline,
        ParticipacionComisionDecisionInline,
        #ParticipacionComisionAgendaInline,
        AccionObservatorioInline,
        DenunciaSocialRealizadaInline,
        #DenunciaSocialEfectivaInline,
        DenunciaJuridicaInline, 
        InvolucramientoPobMetaInline,
        AccionRealizadaReflexionInline, 
        #AccionRelizadaReflexionPersonaInline,
        AccionImpulsadaOrgInline,
        AccionImpulsadaGrupoInline,
        AtencionSaludInline,
        AtencionVictimaInline,
        DenunciaViolenciaInline,
        AtencionVictimaAlbergueInline,
        ReferenciaContraRefInline,
        #AccionPromuevenIntercambioInline,
        #AccionFortaleceCapacidadInline,
        #EstadoCapacidadAdmitivaInline,
        #AccionFortaleceCapAdmitivaInline,
        ]

class InformeAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True    
    list_filter = ['periodo', 'anio']
    inlines = [DatoInformeOb3Inline,]

admin.site.register(TipoAccion)
admin.site.register(Meta)

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(InformeObjetivo3, InformeAdmin)
