# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Knight'
        db.create_table('southut_knight', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('of_the_round_table', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dances_whenever_able', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vegetarian', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('southut', ['Knight'])


    def backwards(self, orm):
        
        # Deleting model 'Knight'
        db.delete_table('southut_knight')


    models = {
        'southut.knight': {
            'Meta': {'object_name': 'Knight'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['southut']
