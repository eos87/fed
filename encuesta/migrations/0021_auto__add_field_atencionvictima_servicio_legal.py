# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'AtencionVictima.servicio_legal'
        db.add_column('encuesta_atencionvictima', 'servicio_legal', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'AtencionVictima.servicio_legal'
        db.delete_column('encuesta_atencionvictima', 'servicio_legal')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accionefectuadadocumento': {
            'Meta': {'object_name': 'AccionEfectuadaDocumento'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_aprob': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'equidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masc_aprob': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'masculinidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr_aprob': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_aprob': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_sida': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'viol_aprob': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionefectuadamedio': {
            'Meta': {'object_name': 'AccionEfectuadaMedio'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'equidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masc_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'masculinidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_sida': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_sida_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'viol_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.accionefectuadaregion': {
            'Meta': {'object_name': 'AccionEfectuadaRegion'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'equidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masc_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'masculinidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_sida': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_sida_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'viol_part': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
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
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.atencionsalud': {
            'Meta': {'object_name': 'AtencionSalud'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'discapacidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'etnica': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.atencionvictima': {
            'Meta': {'object_name': 'AtencionVictima'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio_legal': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'servicio_psicologia': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
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
        'encuesta.datoinformeob3': {
            'Meta': {'object_name': 'DatoInformeOb3'},
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.InformeObjetivo3']"}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Meta']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Organizacion']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Tema']"}),
            'tipo_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.TipoAccion']"})
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
            'informe': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        'encuesta.informeobjetivo3': {
            'Meta': {'object_name': 'InformeObjetivo3'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.involucramientopobmeta': {
            'Meta': {'object_name': 'InvolucramientoPobMeta'},
            'accion': ('django.db.models.fields.CharField', [], {'default': "'no-responde'", 'max_length': '100', 'blank': 'True'}),
            'div_sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'equidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masculinidad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'prev_vio': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ssr': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vih_sida': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.meta': {
            'Meta': {'object_name': 'Meta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'Ninguno'", 'max_length': '200', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
        'encuesta.tema': {
            'Meta': {'object_name': 'Tema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.tipoaccion': {
            'Meta': {'object_name': 'TipoAccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'object_name': 'Municipio'},
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
