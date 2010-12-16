# -*- coding: UTF-8 -*-

from django.contrib import admin
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
admin.site.register(AccionEfectuadaMedio)
admin.site.register(AccionEfectuadaRegion)
admin.site.register(AccionEfectuadaDocumento)
admin.site.register(ParticipacionComisionDecision)
admin.site.register(ParticipacionComisionAgenda)
admin.site.register(DenunciaSocialRealizada)
admin.site.register(DenunciaSocialEfectiva)
admin.site.register(DenunciaJuridica)
admin.site.register(AccionRealizadaReflexion)
admin.site.register(InvolucramientoPobMeta)
admin.site.register(AtencionSalud)
admin.site.register(AccionRelizadaReflexionPersona)
admin.site.register(AccionImpulsadaOrg)
admin.site.register(AccionImpulsadaGrupo)
admin.site.register(AtencionVictima)
admin.site.register(DenunciaViolencia)
admin.site.register(AtencionVictimaAlbergue)
admin.site.register(ReferenciaContraRef)
admin.site.register(AccionPromuevenIntercambio)
admin.site.register(AccionFortaleceCapacidad)
admin.site.register(EstadoCapacidadAdmitiva)
admin.site.register(AccionFortaleceCapAdmitiva)
admin.site.register(Resultado)
admin.site.register(ResultadoTrabajado)



class AccionEfectuadaMedioInline(admin.TabularInline):
    model = AccionEfectuadaMedio
    extra = 1

class AccionEfectuadaRegionInline(admin.TabularInline):
    model = AccionEfectuadaRegion
    extra = 1

class AccionEfectuadaDocumentoInline(admin.TabularInline):
    model = AccionEfectuadaDocumento
    extra = 1

class ParticipacionComisionDecisionInline(admin.TabularInline):
    model = ParticipacionComisionDecision
    extra = 1

class ParticipacionComisionAgendaInline(admin.TabularInline):
    model = ParticipacionComisionAgenda
    extra = 1

class AccionObservatorioInline(admin.TabularInline):
    model = AccionObservatorio
    extra = 1

class DenunciaSocialRealizadaInline(admin.TabularInline):
    model = DenunciaSocialRealizada
    extra = 1

class DenunciaSocialEfectivaInline(admin.TabularInline):
    model = DenunciaSocialEfectiva
    extra = 1

class DenunciaJuridicaInline(admin.TabularInline):
    model = DenunciaJuridica
    extra = 1

class AccionRealizadaReflexionInline(admin.TabularInline):
    model = AccionRealizadaReflexion
    extra = 1

class InvolucramientoPobMetaInline(admin.TabularInline):
    model = InvolucramientoPobMeta
    extra = 1

class AtencionSaludInline(admin.TabularInline):
    model = AtencionSalud
    extra = 1

class AccionRelizadaReflexionPersonaInline(admin.TabularInline):
    model = AccionRelizadaReflexionPersona
    extra = 1

class AccionImpulsadaOrgInline(admin.TabularInline):
    model = AccionImpulsadaOrg
    extra = 1

class AccionImpulsadaGrupoInline(admin.TabularInline):
    model = AccionImpulsadaGrupo
    extra = 1

class AtencionVictimaInline(admin.TabularInline):
    model = AtencionVictima
    extra = 1

class DenunciaViolenciaInline(admin.TabularInline):
    model = DenunciaViolencia
    extra = 1

class AtencionVictimaAlbergueInline(admin.TabularInline):
    model = AtencionVictimaAlbergue
    extra = 1

class ReferenciaContraRefInline(admin.TabularInline):
    model = ReferenciaContraRef
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
    filter_horizontal = ('municipio',)
    extra = 1

class EncuestaAdmin(admin.ModelAdmin):
    #class Media:
        #css = {
        #    "all": ("/files/css/.css",)
        #}
        #js = ('/files/js/jquery.min.js',
        #      '/files/js/filter.js')

    def queryset(self, request):
        if request.user.is_superuser:
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
        ParticipacionComisionAgendaInline,
        AccionObservatorioInline,
        DenunciaSocialRealizadaInline,
        DenunciaSocialEfectivaInline,
        DenunciaJuridicaInline,
        AccionRealizadaReflexionInline,
        InvolucramientoPobMetaInline,
        AtencionSaludInline,
        AccionRelizadaReflexionPersonaInline,
        AccionImpulsadaOrgInline,
        AccionImpulsadaGrupoInline,
        AtencionVictimaInline,
        DenunciaViolenciaInline,
        AtencionVictimaAlbergueInline,
        ReferenciaContraRefInline,
        AccionPromuevenIntercambioInline,
        AccionFortaleceCapacidadInline,
        EstadoCapacidadAdmitivaInline,
        AccionFortaleceCapAdmitivaInline,
        ]

admin.site.register(Encuesta, EncuestaAdmin)
