from django.contrib import admin
from models import *


admin.site.register(Organizacion)
admin.site.register(Proyecto)
admin.site.register(AccionEfectuadaMedio)
admin.site.register(AccionEfectuadaRegion)
admin.site.register(AccionEfectuadaDocumento)
admin.site.register(ParticipacionComisionDecision)
admin.site.register(ParticipacionComisionAgenda)
admin.site.register(DenunciaSocialRealizada)
admin.site.register(DenunciaSocialEfectiva)



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

#a partir de aqui los que no estan registrados en el admin
class DenunciaSocialRealizadaInline(admin.TabularInline):
    model = DenunciaSocialRealizada
    extra = 1

class DenunciaSocialEfectivaInline(admin.TabularInline):
    model = DenunciaSocialEfectiva
    extra = 1

class DenunciaJuridicaInline(admin.TabularInline):
    model = DenunciaJuridica
    extra = 1

admin.site.register(DenunciaJuridica)

class AccionRealizadaReflexionInline(admin.TabularInline):
    model = AccionRealizadaReflexion
    extra = 1

admin.site.register(AccionRealizadaReflexion)

class AccionRelizadaReflexionPersonaInline(admin.TabularInline):
    model = AccionRelizadaReflexionPersona
    extra = 1

admin.site.register(AccionRelizadaReflexionPersona)

class AccionImpulsadaOrgInline(admin.TabularInline):
    model = AccionImpulsadaOrg
    extra = 1

admin.site.register(AccionImpulsadaOrg)

class AccionImpulsadaGrupoInline(admin.TabularInline):
    model = AccionImpulsadaGrupo
    extra = 1

admin.site.register(AccionImpulsadaGrupo)

class AtencionVictimaInline(admin.TabularInline):
    model = AtencionVictima
    extra = 1

admin.site.register(AtencionVictima)

class DenunciaViolenciaInline(admin.TabularInline):
    model = DenunciaViolencia
    extra = 1

admin.site.register(DenunciaViolencia)

class AtencionVictimaAlbergueInline(admin.TabularInline):
    model = AtencionVictimaAlbergue
    extra = 1

admin.site.register(AtencionVictimaAlbergue)

class ReferenciaContraRefInline(admin.TabularInline):
    model = ReferenciaContraRef
    extra = 1

admin.site.register(ReferenciaContraRef)

class AccionPromuevenIntercambioInline(admin.TabularInline):
    model = AccionPromuevenIntercambio
    extra = 1

admin.site.register(AccionPromuevenIntercambio)

class AccionFortaleceCapacidadInline(admin.TabularInline):
    model = AccionFortaleceCapacidad
    extra = 1

admin.site.register(AccionFortaleceCapacidad)

class EstadoCapacidadAdmitivaInline(admin.TabularInline):
    model = EstadoCapacidadAdmitiva
    max_num = 1

admin.site.register(EstadoCapacidadAdmitiva)

class AccionFortaleceCapAdmitivaInline(admin.TabularInline):
    model = AccionFortaleceCapAdmitiva
    extra = 1

admin.site.register(AccionFortaleceCapAdmitiva)

class EncuestaAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [AccionEfectuadaMedioInline,
        AccionEfectuadaRegionInline,
        AccionEfectuadaDocumentoInline,
        ParticipacionComisionDecisionInline,
        ParticipacionComisionAgendaInline,
        AccionObservatorioInline,
        DenunciaSocialRealizadaInline,
        DenunciaSocialEfectivaInline,
        DenunciaJuridicaInline,
        AccionRealizadaReflexionInline,
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