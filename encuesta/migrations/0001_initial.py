# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Organizacion'
        db.create_table('encuesta_organizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('encuesta', ['Organizacion'])

        # Adding model 'Proyecto'
        db.create_table('encuesta_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Organizacion'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('encuesta', ['Proyecto'])

        # Adding M2M table for field municipio on 'Proyecto'
        db.create_table('encuesta_proyecto_municipio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['encuesta.proyecto'], null=False)),
            ('municipio', models.ForeignKey(orm['lugar.municipio'], null=False))
        ))
        db.create_unique('encuesta_proyecto_municipio', ['proyecto_id', 'municipio_id'])

        # Adding model 'Encuesta'
        db.create_table('encuesta_encuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Organizacion'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Proyecto'])),
            ('periodo', self.gf('django.db.models.fields.IntegerField')()),
            ('anio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('encuesta', ['Encuesta'])

        # Adding model 'Resultado'
        db.create_table('encuesta_resultado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('encuesta', ['Resultado'])

        # Adding model 'Indicador'
        db.create_table('encuesta_indicador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resultado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Resultado'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, db_index=True)),
        ))
        db.send_create_signal('encuesta', ['Indicador'])

        # Adding model 'ResultadoTrabajado'
        db.create_table('encuesta_resultadotrabajado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resultado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Resultado'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['ResultadoTrabajado'])

        # Adding M2M table for field municipio on 'ResultadoTrabajado'
        db.create_table('encuesta_resultadotrabajado_municipio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resultadotrabajado', models.ForeignKey(orm['encuesta.resultadotrabajado'], null=False)),
            ('municipio', models.ForeignKey(orm['lugar.municipio'], null=False))
        ))
        db.create_unique('encuesta_resultadotrabajado_municipio', ['resultadotrabajado_id', 'municipio_id'])

        # Adding model 'AccionEfectuadaMedio'
        db.create_table('encuesta_accionefectuadamedio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('participantes', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionEfectuadaMedio'])

        # Adding model 'AccionEfectuadaRegion'
        db.create_table('encuesta_accionefectuadaregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('participantes', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionEfectuadaRegion'])

        # Adding model 'AccionEfectuadaDocumento'
        db.create_table('encuesta_accionefectuadadocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('participantes', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionEfectuadaDocumento'])

        # Adding model 'ParticipacionComisionDecision'
        db.create_table('encuesta_participacioncomisiondecision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cantidad_instancias', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_acciones_promovidas', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_acciones_efectivas', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['ParticipacionComisionDecision'])

        # Adding model 'ParticipacionComisionAgenda'
        db.create_table('encuesta_participacioncomisionagenda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cantidad_instancias', self.gf('django.db.models.fields.IntegerField')(db_column='cat_instancias')),
            ('cantidad_acciones_prom', self.gf('django.db.models.fields.IntegerField')(db_column='cant_acc_prom')),
            ('cantidad_acciones_efec', self.gf('django.db.models.fields.IntegerField')(db_column='cant_acc_efec')),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['ParticipacionComisionAgenda'])

        # Adding model 'AccionObservatorio'
        db.create_table('encuesta_accionobservatorio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cantidad_observatorios', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_acciones_realiz', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_acciones_web', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionObservatorio'])

        # Adding model 'DenunciaSocialRealizada'
        db.create_table('encuesta_denunciasocialrealizada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('persona_div_sexual', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_discapacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_vih', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_racial', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_joven', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['DenunciaSocialRealizada'])

        # Adding model 'DenunciaSocialEfectiva'
        db.create_table('encuesta_denunciasocialefectiva', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('persona_div_sexual', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_discapacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_vih', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_racial', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_joven', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['DenunciaSocialEfectiva'])

        # Adding model 'DenunciaJuridica'
        db.create_table('encuesta_denunciajuridica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('persona_div_sexual', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_discapacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_vih', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_racial', self.gf('django.db.models.fields.IntegerField')()),
            ('persona_joven', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['DenunciaJuridica'])

        # Adding model 'AccionRealizadaReflexion'
        db.create_table('encuesta_accionrealizadareflexion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('jovenes', self.gf('django.db.models.fields.IntegerField')()),
            ('div_sexual', self.gf('django.db.models.fields.IntegerField')()),
            ('vih', self.gf('django.db.models.fields.IntegerField')()),
            ('etnica', self.gf('django.db.models.fields.IntegerField')()),
            ('discapacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionRealizadaReflexion'])

        # Adding model 'AccionRelizadaReflexionPersona'
        db.create_table('encuesta_accionrelizadareflexionpersona', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('jovenes', self.gf('django.db.models.fields.IntegerField')()),
            ('div_sexual', self.gf('django.db.models.fields.IntegerField')()),
            ('vih', self.gf('django.db.models.fields.IntegerField')()),
            ('etnica', self.gf('django.db.models.fields.IntegerField')()),
            ('discapacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionRelizadaReflexionPersona'])

        # Adding model 'AccionImpulsadaOrg'
        db.create_table('encuesta_accionimpulsadaorg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('acciones_emprendidas', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_cambios_actitud', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_impulsadas_masculinidad', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_cambios_masculinidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionImpulsadaOrg'])

        # Adding model 'AccionImpulsadaGrupo'
        db.create_table('encuesta_accionimpulsadagrupo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('acciones_emprendidas_sex', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_cambio_sex', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_emprendidas_discapa', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_cambio_discapa', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_emprendidas_etnia', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_cambio_etnia', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_emprendidas_jovenes', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_cambio_jovenes', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionImpulsadaGrupo'])

        # Adding model 'AtencionVictima'
        db.create_table('encuesta_atencionvictima', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('servicio_salud', self.gf('django.db.models.fields.IntegerField')()),
            ('servicio_psicologia', self.gf('django.db.models.fields.IntegerField')()),
            ('servicio_legal', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AtencionVictima'])

        # Adding model 'DenunciaViolencia'
        db.create_table('encuesta_denunciaviolencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comisariato', self.gf('django.db.models.fields.IntegerField')()),
            ('fiscalia', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['DenunciaViolencia'])

        # Adding model 'AtencionVictimaAlbergue'
        db.create_table('encuesta_atencionvictimaalbergue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('jovenes', self.gf('django.db.models.fields.IntegerField')()),
            ('ninos_ninas', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AtencionVictimaAlbergue'])

        # Adding model 'ReferenciaContraRef'
        db.create_table('encuesta_referenciacontraref', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('jovenes', self.gf('django.db.models.fields.IntegerField')()),
            ('ninos_ninas', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['ReferenciaContraRef'])

        # Adding model 'AccionPromuevenIntercambio'
        db.create_table('encuesta_accionpromuevenintercambio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('acciones_org_part', self.gf('django.db.models.fields.IntegerField')()),
            ('participantes', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_efectivas', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionPromuevenIntercambio'])

        # Adding model 'AccionFortaleceCapacidad'
        db.create_table('encuesta_accionfortalececapacidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('acciones', self.gf('django.db.models.fields.IntegerField')()),
            ('participantes', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones_efectivas', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionFortaleceCapacidad'])

        # Adding model 'EstadoCapacidadAdmitiva'
        db.create_table('encuesta_estadocapacidadadmitiva', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sistema', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('plan', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('organizaciones', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['EstadoCapacidadAdmitiva'])

        # Adding model 'AccionFortaleceCapAdmitiva'
        db.create_table('encuesta_accionfortalececapadmitiva', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mejorar_sistema', self.gf('django.db.models.fields.IntegerField')()),
            ('mejorar_plan', self.gf('django.db.models.fields.IntegerField')()),
            ('mejorar_apoyo', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('encuesta', ['AccionFortaleceCapAdmitiva'])


    def backwards(self, orm):
        
        # Deleting model 'Organizacion'
        db.delete_table('encuesta_organizacion')

        # Deleting model 'Proyecto'
        db.delete_table('encuesta_proyecto')

        # Removing M2M table for field municipio on 'Proyecto'
        db.delete_table('encuesta_proyecto_municipio')

        # Deleting model 'Encuesta'
        db.delete_table('encuesta_encuesta')

        # Deleting model 'Resultado'
        db.delete_table('encuesta_resultado')

        # Deleting model 'Indicador'
        db.delete_table('encuesta_indicador')

        # Deleting model 'ResultadoTrabajado'
        db.delete_table('encuesta_resultadotrabajado')

        # Removing M2M table for field municipio on 'ResultadoTrabajado'
        db.delete_table('encuesta_resultadotrabajado_municipio')

        # Deleting model 'AccionEfectuadaMedio'
        db.delete_table('encuesta_accionefectuadamedio')

        # Deleting model 'AccionEfectuadaRegion'
        db.delete_table('encuesta_accionefectuadaregion')

        # Deleting model 'AccionEfectuadaDocumento'
        db.delete_table('encuesta_accionefectuadadocumento')

        # Deleting model 'ParticipacionComisionDecision'
        db.delete_table('encuesta_participacioncomisiondecision')

        # Deleting model 'ParticipacionComisionAgenda'
        db.delete_table('encuesta_participacioncomisionagenda')

        # Deleting model 'AccionObservatorio'
        db.delete_table('encuesta_accionobservatorio')

        # Deleting model 'DenunciaSocialRealizada'
        db.delete_table('encuesta_denunciasocialrealizada')

        # Deleting model 'DenunciaSocialEfectiva'
        db.delete_table('encuesta_denunciasocialefectiva')

        # Deleting model 'DenunciaJuridica'
        db.delete_table('encuesta_denunciajuridica')

        # Deleting model 'AccionRealizadaReflexion'
        db.delete_table('encuesta_accionrealizadareflexion')

        # Deleting model 'AccionRelizadaReflexionPersona'
        db.delete_table('encuesta_accionrelizadareflexionpersona')

        # Deleting model 'AccionImpulsadaOrg'
        db.delete_table('encuesta_accionimpulsadaorg')

        # Deleting model 'AccionImpulsadaGrupo'
        db.delete_table('encuesta_accionimpulsadagrupo')

        # Deleting model 'AtencionVictima'
        db.delete_table('encuesta_atencionvictima')

        # Deleting model 'DenunciaViolencia'
        db.delete_table('encuesta_denunciaviolencia')

        # Deleting model 'AtencionVictimaAlbergue'
        db.delete_table('encuesta_atencionvictimaalbergue')

        # Deleting model 'ReferenciaContraRef'
        db.delete_table('encuesta_referenciacontraref')

        # Deleting model 'AccionPromuevenIntercambio'
        db.delete_table('encuesta_accionpromuevenintercambio')

        # Deleting model 'AccionFortaleceCapacidad'
        db.delete_table('encuesta_accionfortalececapacidad')

        # Deleting model 'EstadoCapacidadAdmitiva'
        db.delete_table('encuesta_estadocapacidadadmitiva')

        # Deleting model 'AccionFortaleceCapAdmitiva'
        db.delete_table('encuesta_accionfortalececapadmitiva')


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
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionefectuadamedio': {
            'Meta': {'object_name': 'AccionEfectuadaMedio'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionefectuadaregion': {
            'Meta': {'object_name': 'AccionEfectuadaRegion'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionfortalececapacidad': {
            'Meta': {'object_name': 'AccionFortaleceCapacidad'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'acciones': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_efectivas': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionfortalececapadmitiva': {
            'Meta': {'object_name': 'AccionFortaleceCapAdmitiva'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejorar_apoyo': ('django.db.models.fields.IntegerField', [], {}),
            'mejorar_plan': ('django.db.models.fields.IntegerField', [], {}),
            'mejorar_sistema': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionimpulsadagrupo': {
            'Meta': {'object_name': 'AccionImpulsadaGrupo'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'acciones_cambio_discapa': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_cambio_etnia': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_cambio_jovenes': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_cambio_sex': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_emprendidas_discapa': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_emprendidas_etnia': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_emprendidas_jovenes': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_emprendidas_sex': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.accionimpulsadaorg': {
            'Meta': {'object_name': 'AccionImpulsadaOrg'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'acciones_cambios_actitud': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_cambios_masculinidad': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_emprendidas': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_impulsadas_masculinidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.accionobservatorio': {
            'Meta': {'object_name': 'AccionObservatorio'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantidad_acciones_realiz': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_acciones_web': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_observatorios': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.accionpromuevenintercambio': {
            'Meta': {'object_name': 'AccionPromuevenIntercambio'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'acciones_efectivas': ('django.db.models.fields.IntegerField', [], {}),
            'acciones_org_part': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionrealizadareflexion': {
            'Meta': {'object_name': 'AccionRealizadaReflexion'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discapacidad': ('django.db.models.fields.IntegerField', [], {}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'etnica': ('django.db.models.fields.IntegerField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'vih': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionrelizadareflexionpersona': {
            'Meta': {'object_name': 'AccionRelizadaReflexionPersona'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discapacidad': ('django.db.models.fields.IntegerField', [], {}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'etnica': ('django.db.models.fields.IntegerField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'vih': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.atencionvictima': {
            'Meta': {'object_name': 'AtencionVictima'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio_legal': ('django.db.models.fields.IntegerField', [], {}),
            'servicio_psicologia': ('django.db.models.fields.IntegerField', [], {}),
            'servicio_salud': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.atencionvictimaalbergue': {
            'Meta': {'object_name': 'AtencionVictimaAlbergue'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'ninos_ninas': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.denunciajuridica': {
            'Meta': {'object_name': 'DenunciaJuridica'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona_discapacidad': ('django.db.models.fields.IntegerField', [], {}),
            'persona_div_sexual': ('django.db.models.fields.IntegerField', [], {}),
            'persona_joven': ('django.db.models.fields.IntegerField', [], {}),
            'persona_racial': ('django.db.models.fields.IntegerField', [], {}),
            'persona_vih': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.denunciasocialefectiva': {
            'Meta': {'object_name': 'DenunciaSocialEfectiva'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona_discapacidad': ('django.db.models.fields.IntegerField', [], {}),
            'persona_div_sexual': ('django.db.models.fields.IntegerField', [], {}),
            'persona_joven': ('django.db.models.fields.IntegerField', [], {}),
            'persona_racial': ('django.db.models.fields.IntegerField', [], {}),
            'persona_vih': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.denunciasocialrealizada': {
            'Meta': {'object_name': 'DenunciaSocialRealizada'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona_discapacidad': ('django.db.models.fields.IntegerField', [], {}),
            'persona_div_sexual': ('django.db.models.fields.IntegerField', [], {}),
            'persona_joven': ('django.db.models.fields.IntegerField', [], {}),
            'persona_racial': ('django.db.models.fields.IntegerField', [], {}),
            'persona_vih': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.denunciaviolencia': {
            'Meta': {'object_name': 'DenunciaViolencia'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comisariato': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'fiscalia': ('django.db.models.fields.IntegerField', [], {}),
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
            'organizaciones': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plan': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sistema': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'encuesta.participacioncomisionagenda': {
            'Meta': {'object_name': 'ParticipacionComisionAgenda'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantidad_acciones_efec': ('django.db.models.fields.IntegerField', [], {'db_column': "'cant_acc_efec'"}),
            'cantidad_acciones_prom': ('django.db.models.fields.IntegerField', [], {'db_column': "'cant_acc_prom'"}),
            'cantidad_instancias': ('django.db.models.fields.IntegerField', [], {'db_column': "'cat_instancias'"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.participacioncomisiondecision': {
            'Meta': {'object_name': 'ParticipacionComisionDecision'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantidad_acciones_efectivas': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_acciones_promovidas': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_instancias': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'encuesta.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lugar.Municipio']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"})
        },
        'encuesta.referenciacontraref': {
            'Meta': {'object_name': 'ReferenciaContraRef'},
            'accion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'ninos_ninas': ('django.db.models.fields.IntegerField', [], {})
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
