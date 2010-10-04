# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Municipio.extension'
        db.add_column('lugar_municipio', 'extension', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True), keep_default=False)

        # Changing field 'Municipio.id'
        db.alter_column('lugar_municipio', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

        # Adding field 'Departamento.extension'
        db.add_column('lugar_departamento', 'extension', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2), keep_default=False)

        # Changing field 'Departamento.id'
        db.alter_column('lugar_departamento', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))


    def backwards(self, orm):
        
        # Deleting field 'Municipio.extension'
        db.delete_column('lugar_municipio', 'extension')

        # Changing field 'Municipio.id'
        db.alter_column('lugar_municipio', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

        # Deleting field 'Departamento.extension'
        db.delete_column('lugar_departamento', 'extension')

        # Changing field 'Departamento.id'
        db.alter_column('lugar_departamento', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))


    models = {
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

    complete_apps = ['lugar']
