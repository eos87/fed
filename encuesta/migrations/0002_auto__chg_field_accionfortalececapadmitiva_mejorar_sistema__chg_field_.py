# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AccionFortaleceCapAdmitiva.mejorar_sistema'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'mejorar_sistema', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionFortaleceCapAdmitiva.accion'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionFortaleceCapAdmitiva.mejorar_plan'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'mejorar_plan', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionFortaleceCapAdmitiva.mejorar_apoyo'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'mejorar_apoyo', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionObservatorio.accion'
        db.alter_column('encuesta_accionobservatorio', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionObservatorio.cantidad_acciones_web'
        db.alter_column('encuesta_accionobservatorio', 'cantidad_acciones_web', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionObservatorio.cantidad_acciones_realiz'
        db.alter_column('encuesta_accionobservatorio', 'cantidad_acciones_realiz', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionObservatorio.cantidad_observatorios'
        db.alter_column('encuesta_accionobservatorio', 'cantidad_observatorios', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionFortaleceCapacidad.accion'
        db.alter_column('encuesta_accionfortalececapacidad', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionFortaleceCapacidad.participantes'
        db.alter_column('encuesta_accionfortalececapacidad', 'participantes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionFortaleceCapacidad.acciones_efectivas'
        db.alter_column('encuesta_accionfortalececapacidad', 'acciones_efectivas', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionFortaleceCapacidad.acciones'
        db.alter_column('encuesta_accionfortalececapacidad', 'acciones', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.discapacidad'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'discapacidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.accion'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionRelizadaReflexionPersona.mujeres'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'mujeres', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.hombres'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'hombres', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.vih'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'vih', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.jovenes'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'jovenes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.etnica'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'etnica', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRelizadaReflexionPersona.div_sexual'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'div_sexual', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaViolencia.comisariato'
        db.alter_column('encuesta_denunciaviolencia', 'comisariato', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaViolencia.fiscalia'
        db.alter_column('encuesta_denunciaviolencia', 'fiscalia', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaViolencia.accion'
        db.alter_column('encuesta_denunciaviolencia', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionPromuevenIntercambio.acciones_org_part'
        db.alter_column('encuesta_accionpromuevenintercambio', 'acciones_org_part', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionPromuevenIntercambio.accion'
        db.alter_column('encuesta_accionpromuevenintercambio', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionPromuevenIntercambio.participantes'
        db.alter_column('encuesta_accionpromuevenintercambio', 'participantes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionPromuevenIntercambio.acciones_efectivas'
        db.alter_column('encuesta_accionpromuevenintercambio', 'acciones_efectivas', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialEfectiva.persona_racial'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_racial', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialEfectiva.accion'
        db.alter_column('encuesta_denunciasocialefectiva', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'DenunciaSocialEfectiva.persona_div_sexual'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_div_sexual', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialEfectiva.persona_joven'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_joven', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialEfectiva.persona_vih'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_vih', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialEfectiva.persona_discapacidad'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_discapacidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.discapacidad'
        db.alter_column('encuesta_accionrealizadareflexion', 'discapacidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.accion'
        db.alter_column('encuesta_accionrealizadareflexion', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionRealizadaReflexion.mujeres'
        db.alter_column('encuesta_accionrealizadareflexion', 'mujeres', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.hombres'
        db.alter_column('encuesta_accionrealizadareflexion', 'hombres', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.vih'
        db.alter_column('encuesta_accionrealizadareflexion', 'vih', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.jovenes'
        db.alter_column('encuesta_accionrealizadareflexion', 'jovenes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.etnica'
        db.alter_column('encuesta_accionrealizadareflexion', 'etnica', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionRealizadaReflexion.div_sexual'
        db.alter_column('encuesta_accionrealizadareflexion', 'div_sexual', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Organizacion.correo'
        db.alter_column('encuesta_organizacion', 'correo', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # Changing field 'Organizacion.contacto'
        db.alter_column('encuesta_organizacion', 'contacto', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Organizacion.telefono'
        db.alter_column('encuesta_organizacion', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'AtencionVictima.accion'
        db.alter_column('encuesta_atencionvictima', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AtencionVictima.servicio_legal'
        db.alter_column('encuesta_atencionvictima', 'servicio_legal', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AtencionVictima.servicio_salud'
        db.alter_column('encuesta_atencionvictima', 'servicio_salud', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AtencionVictima.servicio_psicologia'
        db.alter_column('encuesta_atencionvictima', 'servicio_psicologia', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AtencionVictimaAlbergue.accion'
        db.alter_column('encuesta_atencionvictimaalbergue', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AtencionVictimaAlbergue.mujeres'
        db.alter_column('encuesta_atencionvictimaalbergue', 'mujeres', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AtencionVictimaAlbergue.jovenes'
        db.alter_column('encuesta_atencionvictimaalbergue', 'jovenes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AtencionVictimaAlbergue.ninos_ninas'
        db.alter_column('encuesta_atencionvictimaalbergue', 'ninos_ninas', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaRegion.cantidad'
        db.alter_column('encuesta_accionefectuadaregion', 'cantidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaRegion.participantes'
        db.alter_column('encuesta_accionefectuadaregion', 'participantes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaRegion.accion'
        db.alter_column('encuesta_accionefectuadaregion', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionImpulsadaOrg.accion'
        db.alter_column('encuesta_accionimpulsadaorg', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionImpulsadaOrg.acciones_emprendidas'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_emprendidas', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaOrg.acciones_cambios_masculinidad'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_cambios_masculinidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaOrg.acciones_impulsadas_masculinidad'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_impulsadas_masculinidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaOrg.acciones_cambios_actitud'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_cambios_actitud', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaDocumento.cantidad'
        db.alter_column('encuesta_accionefectuadadocumento', 'cantidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaDocumento.participantes'
        db.alter_column('encuesta_accionefectuadadocumento', 'participantes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaDocumento.accion'
        db.alter_column('encuesta_accionefectuadadocumento', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ParticipacionComisionAgenda.accion'
        db.alter_column('encuesta_participacioncomisionagenda', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ParticipacionComisionAgenda.cantidad_acciones_efec'
        db.alter_column('encuesta_participacioncomisionagenda', 'cant_acc_efec', self.gf('django.db.models.fields.IntegerField')(db_column='cant_acc_efec'))

        # Changing field 'ParticipacionComisionAgenda.cantidad_instancias'
        db.alter_column('encuesta_participacioncomisionagenda', 'cat_instancias', self.gf('django.db.models.fields.IntegerField')(db_column='cat_instancias'))

        # Changing field 'ParticipacionComisionAgenda.cantidad_acciones_prom'
        db.alter_column('encuesta_participacioncomisionagenda', 'cant_acc_prom', self.gf('django.db.models.fields.IntegerField')(db_column='cant_acc_prom'))

        # Changing field 'DenunciaSocialRealizada.persona_racial'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_racial', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialRealizada.accion'
        db.alter_column('encuesta_denunciasocialrealizada', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'DenunciaSocialRealizada.persona_div_sexual'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_div_sexual', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialRealizada.persona_joven'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_joven', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialRealizada.persona_vih'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_vih', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaSocialRealizada.persona_discapacidad'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_discapacidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaJuridica.persona_racial'
        db.alter_column('encuesta_denunciajuridica', 'persona_racial', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaJuridica.accion'
        db.alter_column('encuesta_denunciajuridica', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'DenunciaJuridica.persona_div_sexual'
        db.alter_column('encuesta_denunciajuridica', 'persona_div_sexual', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaJuridica.persona_joven'
        db.alter_column('encuesta_denunciajuridica', 'persona_joven', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaJuridica.persona_vih'
        db.alter_column('encuesta_denunciajuridica', 'persona_vih', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DenunciaJuridica.persona_discapacidad'
        db.alter_column('encuesta_denunciajuridica', 'persona_discapacidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ReferenciaContraRef.accion'
        db.alter_column('encuesta_referenciacontraref', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ReferenciaContraRef.mujeres'
        db.alter_column('encuesta_referenciacontraref', 'mujeres', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ReferenciaContraRef.jovenes'
        db.alter_column('encuesta_referenciacontraref', 'jovenes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ReferenciaContraRef.ninos_ninas'
        db.alter_column('encuesta_referenciacontraref', 'ninos_ninas', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaMedio.cantidad'
        db.alter_column('encuesta_accionefectuadamedio', 'cantidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionEfectuadaMedio.participantes'
        db.alter_column('encuesta_accionefectuadamedio', 'participantes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.accion'
        db.alter_column('encuesta_accionimpulsadagrupo', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_discapa'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_discapa', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_etnia'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_etnia', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_etnia'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_etnia', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_discapa'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_discapa', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_sex'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_sex', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_sex'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_sex', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_jovenes'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_jovenes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_jovenes'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_jovenes', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ParticipacionComisionDecision.cantidad_acciones_promovidas'
        db.alter_column('encuesta_participacioncomisiondecision', 'cantidad_acciones_promovidas', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ParticipacionComisionDecision.accion'
        db.alter_column('encuesta_participacioncomisiondecision', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ParticipacionComisionDecision.cantidad_instancias'
        db.alter_column('encuesta_participacioncomisiondecision', 'cantidad_instancias', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ParticipacionComisionDecision.cantidad_acciones_efectivas'
        db.alter_column('encuesta_participacioncomisiondecision', 'cantidad_acciones_efectivas', self.gf('django.db.models.fields.IntegerField')())


    def backwards(self, orm):
        
        # Changing field 'AccionFortaleceCapAdmitiva.mejorar_sistema'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'mejorar_sistema', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionFortaleceCapAdmitiva.accion'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionFortaleceCapAdmitiva.mejorar_plan'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'mejorar_plan', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionFortaleceCapAdmitiva.mejorar_apoyo'
        db.alter_column('encuesta_accionfortalececapadmitiva', 'mejorar_apoyo', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionObservatorio.accion'
        db.alter_column('encuesta_accionobservatorio', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionObservatorio.cantidad_acciones_web'
        db.alter_column('encuesta_accionobservatorio', 'cantidad_acciones_web', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionObservatorio.cantidad_acciones_realiz'
        db.alter_column('encuesta_accionobservatorio', 'cantidad_acciones_realiz', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionObservatorio.cantidad_observatorios'
        db.alter_column('encuesta_accionobservatorio', 'cantidad_observatorios', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionFortaleceCapacidad.accion'
        db.alter_column('encuesta_accionfortalececapacidad', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionFortaleceCapacidad.participantes'
        db.alter_column('encuesta_accionfortalececapacidad', 'participantes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionFortaleceCapacidad.acciones_efectivas'
        db.alter_column('encuesta_accionfortalececapacidad', 'acciones_efectivas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionFortaleceCapacidad.acciones'
        db.alter_column('encuesta_accionfortalececapacidad', 'acciones', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.discapacidad'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'discapacidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.accion'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionRelizadaReflexionPersona.mujeres'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.hombres'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'hombres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.vih'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'vih', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.jovenes'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'jovenes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.etnica'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'etnica', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRelizadaReflexionPersona.div_sexual'
        db.alter_column('encuesta_accionrelizadareflexionpersona', 'div_sexual', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaViolencia.comisariato'
        db.alter_column('encuesta_denunciaviolencia', 'comisariato', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaViolencia.fiscalia'
        db.alter_column('encuesta_denunciaviolencia', 'fiscalia', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaViolencia.accion'
        db.alter_column('encuesta_denunciaviolencia', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionPromuevenIntercambio.acciones_org_part'
        db.alter_column('encuesta_accionpromuevenintercambio', 'acciones_org_part', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionPromuevenIntercambio.accion'
        db.alter_column('encuesta_accionpromuevenintercambio', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionPromuevenIntercambio.participantes'
        db.alter_column('encuesta_accionpromuevenintercambio', 'participantes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionPromuevenIntercambio.acciones_efectivas'
        db.alter_column('encuesta_accionpromuevenintercambio', 'acciones_efectivas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialEfectiva.persona_racial'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_racial', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialEfectiva.accion'
        db.alter_column('encuesta_denunciasocialefectiva', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'DenunciaSocialEfectiva.persona_div_sexual'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_div_sexual', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialEfectiva.persona_joven'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_joven', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialEfectiva.persona_vih'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_vih', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialEfectiva.persona_discapacidad'
        db.alter_column('encuesta_denunciasocialefectiva', 'persona_discapacidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.discapacidad'
        db.alter_column('encuesta_accionrealizadareflexion', 'discapacidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.accion'
        db.alter_column('encuesta_accionrealizadareflexion', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionRealizadaReflexion.mujeres'
        db.alter_column('encuesta_accionrealizadareflexion', 'mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.hombres'
        db.alter_column('encuesta_accionrealizadareflexion', 'hombres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.vih'
        db.alter_column('encuesta_accionrealizadareflexion', 'vih', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.jovenes'
        db.alter_column('encuesta_accionrealizadareflexion', 'jovenes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.etnica'
        db.alter_column('encuesta_accionrealizadareflexion', 'etnica', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionRealizadaReflexion.div_sexual'
        db.alter_column('encuesta_accionrealizadareflexion', 'div_sexual', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Organizacion.correo'
        db.alter_column('encuesta_organizacion', 'correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'Organizacion.contacto'
        db.alter_column('encuesta_organizacion', 'contacto', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Organizacion.telefono'
        db.alter_column('encuesta_organizacion', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'AtencionVictima.accion'
        db.alter_column('encuesta_atencionvictima', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AtencionVictima.servicio_legal'
        db.alter_column('encuesta_atencionvictima', 'servicio_legal', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AtencionVictima.servicio_salud'
        db.alter_column('encuesta_atencionvictima', 'servicio_salud', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AtencionVictima.servicio_psicologia'
        db.alter_column('encuesta_atencionvictima', 'servicio_psicologia', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AtencionVictimaAlbergue.accion'
        db.alter_column('encuesta_atencionvictimaalbergue', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AtencionVictimaAlbergue.mujeres'
        db.alter_column('encuesta_atencionvictimaalbergue', 'mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AtencionVictimaAlbergue.jovenes'
        db.alter_column('encuesta_atencionvictimaalbergue', 'jovenes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AtencionVictimaAlbergue.ninos_ninas'
        db.alter_column('encuesta_atencionvictimaalbergue', 'ninos_ninas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaRegion.cantidad'
        db.alter_column('encuesta_accionefectuadaregion', 'cantidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaRegion.participantes'
        db.alter_column('encuesta_accionefectuadaregion', 'participantes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaRegion.accion'
        db.alter_column('encuesta_accionefectuadaregion', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionImpulsadaOrg.accion'
        db.alter_column('encuesta_accionimpulsadaorg', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionImpulsadaOrg.acciones_emprendidas'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_emprendidas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaOrg.acciones_cambios_masculinidad'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_cambios_masculinidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaOrg.acciones_impulsadas_masculinidad'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_impulsadas_masculinidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaOrg.acciones_cambios_actitud'
        db.alter_column('encuesta_accionimpulsadaorg', 'acciones_cambios_actitud', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaDocumento.cantidad'
        db.alter_column('encuesta_accionefectuadadocumento', 'cantidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaDocumento.participantes'
        db.alter_column('encuesta_accionefectuadadocumento', 'participantes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaDocumento.accion'
        db.alter_column('encuesta_accionefectuadadocumento', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'ParticipacionComisionAgenda.accion'
        db.alter_column('encuesta_participacioncomisionagenda', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'ParticipacionComisionAgenda.cantidad_acciones_efec'
        db.alter_column('encuesta_participacioncomisionagenda', 'cant_acc_efec', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='cant_acc_efec'))

        # Changing field 'ParticipacionComisionAgenda.cantidad_instancias'
        db.alter_column('encuesta_participacioncomisionagenda', 'cat_instancias', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='cat_instancias'))

        # Changing field 'ParticipacionComisionAgenda.cantidad_acciones_prom'
        db.alter_column('encuesta_participacioncomisionagenda', 'cant_acc_prom', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='cant_acc_prom'))

        # Changing field 'DenunciaSocialRealizada.persona_racial'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_racial', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialRealizada.accion'
        db.alter_column('encuesta_denunciasocialrealizada', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'DenunciaSocialRealizada.persona_div_sexual'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_div_sexual', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialRealizada.persona_joven'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_joven', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialRealizada.persona_vih'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_vih', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaSocialRealizada.persona_discapacidad'
        db.alter_column('encuesta_denunciasocialrealizada', 'persona_discapacidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaJuridica.persona_racial'
        db.alter_column('encuesta_denunciajuridica', 'persona_racial', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaJuridica.accion'
        db.alter_column('encuesta_denunciajuridica', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'DenunciaJuridica.persona_div_sexual'
        db.alter_column('encuesta_denunciajuridica', 'persona_div_sexual', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaJuridica.persona_joven'
        db.alter_column('encuesta_denunciajuridica', 'persona_joven', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaJuridica.persona_vih'
        db.alter_column('encuesta_denunciajuridica', 'persona_vih', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DenunciaJuridica.persona_discapacidad'
        db.alter_column('encuesta_denunciajuridica', 'persona_discapacidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ReferenciaContraRef.accion'
        db.alter_column('encuesta_referenciacontraref', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'ReferenciaContraRef.mujeres'
        db.alter_column('encuesta_referenciacontraref', 'mujeres', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ReferenciaContraRef.jovenes'
        db.alter_column('encuesta_referenciacontraref', 'jovenes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ReferenciaContraRef.ninos_ninas'
        db.alter_column('encuesta_referenciacontraref', 'ninos_ninas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaMedio.cantidad'
        db.alter_column('encuesta_accionefectuadamedio', 'cantidad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionEfectuadaMedio.participantes'
        db.alter_column('encuesta_accionefectuadamedio', 'participantes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.accion'
        db.alter_column('encuesta_accionimpulsadagrupo', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_discapa'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_discapa', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_etnia'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_etnia', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_etnia'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_etnia', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_discapa'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_discapa', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_sex'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_sex', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_sex'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_sex', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_emprendidas_jovenes'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_emprendidas_jovenes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AccionImpulsadaGrupo.acciones_cambio_jovenes'
        db.alter_column('encuesta_accionimpulsadagrupo', 'acciones_cambio_jovenes', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ParticipacionComisionDecision.cantidad_acciones_promovidas'
        db.alter_column('encuesta_participacioncomisiondecision', 'cantidad_acciones_promovidas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ParticipacionComisionDecision.accion'
        db.alter_column('encuesta_participacioncomisiondecision', 'accion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'ParticipacionComisionDecision.cantidad_instancias'
        db.alter_column('encuesta_participacioncomisiondecision', 'cantidad_instancias', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ParticipacionComisionDecision.cantidad_acciones_efectivas'
        db.alter_column('encuesta_participacioncomisiondecision', 'cantidad_acciones_efectivas', self.gf('django.db.models.fields.IntegerField')(null=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accionefectuadadocumento': {
            'Meta': {'object_name': 'AccionEfectuadaDocumento'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionefectuadamedio': {
            'Meta': {'object_name': 'AccionEfectuadaMedio'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionefectuadaregion': {
            'Meta': {'object_name': 'AccionEfectuadaRegion'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionfortalececapacidad': {
            'Meta': {'object_name': 'AccionFortaleceCapacidad'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'acciones': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_efectivas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionfortalececapadmitiva': {
            'Meta': {'object_name': 'AccionFortaleceCapAdmitiva'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejorar_apoyo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mejorar_plan': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mejorar_sistema': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionimpulsadagrupo': {
            'Meta': {'object_name': 'AccionImpulsadaGrupo'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'acciones_cambio_discapa': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_cambio_etnia': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_cambio_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_cambio_sex': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_emprendidas_discapa': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_emprendidas_etnia': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_emprendidas_jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_emprendidas_sex': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.accionimpulsadaorg': {
            'Meta': {'object_name': 'AccionImpulsadaOrg'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'acciones_cambios_actitud': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_cambios_masculinidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_emprendidas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_impulsadas_masculinidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.accionobservatorio': {
            'Meta': {'object_name': 'AccionObservatorio'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad_acciones_realiz': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cantidad_acciones_web': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cantidad_observatorios': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.accionpromuevenintercambio': {
            'Meta': {'object_name': 'AccionPromuevenIntercambio'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'acciones_efectivas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'acciones_org_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionrealizadareflexion': {
            'Meta': {'object_name': 'AccionRealizadaReflexion'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'discapacidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'etnica': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionrelizadareflexionpersona': {
            'Meta': {'object_name': 'AccionRelizadaReflexionPersona'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'discapacidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'etnica': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.atencionvictima': {
            'Meta': {'object_name': 'AtencionVictima'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio_legal': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'servicio_psicologia': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'servicio_salud': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.atencionvictimaalbergue': {
            'Meta': {'object_name': 'AtencionVictimaAlbergue'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ninos_ninas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.denunciajuridica': {
            'Meta': {'object_name': 'DenunciaJuridica'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona_discapacidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_joven': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_racial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.denunciasocialefectiva': {
            'Meta': {'object_name': 'DenunciaSocialEfectiva'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona_discapacidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_joven': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_racial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.denunciasocialrealizada': {
            'Meta': {'object_name': 'DenunciaSocialRealizada'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona_discapacidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_joven': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_racial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'persona_vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.denunciaviolencia': {
            'Meta': {'object_name': 'DenunciaViolencia'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'comisariato': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'fiscalia': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"}),
            'periodo': ('django.db.models.fields.IntegerField', [], {}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Proyecto']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuesta.estadocapacidadadmitiva': {
            'Meta': {'object_name': 'EstadoCapacidadAdmitiva'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizaciones': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'plan': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'sistema': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'})
        },
        'encuesta.indicador': {
            'Meta': {'object_name': 'Indicador'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resultado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Resultado']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'encuesta.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'antecedentes': ('django.db.models.fields.TextField', [], {}),
            'contacto': ('django.db.models.fields.CharField', [], {'default': "'Ninguno'", 'max_length': '200', 'blank': 'True'}),
            'correo': ('django.db.models.fields.EmailField', [], {'default': "'example@example.com'", 'max_length': '75', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'Ninguno'", 'max_length': '200', 'blank': 'True'})
        },
        'encuesta.participacioncomisionagenda': {
            'Meta': {'object_name': 'ParticipacionComisionAgenda'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad_acciones_efec': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'cant_acc_efec'", 'blank': 'True'}),
            'cantidad_acciones_prom': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'cant_acc_prom'", 'blank': 'True'}),
            'cantidad_instancias': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'cat_instancias'", 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.participacioncomisiondecision': {
            'Meta': {'object_name': 'ParticipacionComisionDecision'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad_acciones_efectivas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cantidad_acciones_promovidas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cantidad_instancias': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'cobertura': ('django.db.models.fields.TextField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'monto2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"})
        },
        'encuesta.referenciacontraref': {
            'Meta': {'object_name': 'ReferenciaContraRef'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ninos_ninas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.resultado': {
            'Meta': {'object_name': 'Resultado'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.resultadotrabajado': {
            'Meta': {'object_name': 'ResultadoTrabajado'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lugar.Municipio']", 'symmetrical': 'False'}),
            'resultado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Resultado']"})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['encuesta']
