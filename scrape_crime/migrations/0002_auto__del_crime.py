# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Crime'
        db.delete_table('scrape_crime_crime')

    def backwards(self, orm):
        # Adding model 'Crime'
        db.create_table('scrape_crime_crime', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank='')),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank='')),
            ('beat', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('domestic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('iucr', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank='')),
            ('arrest', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location_description', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank='')),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Location'], null=True, blank=True)),
            ('case_number', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
            ('updated_on', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('ward', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('fbi_code', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank='')),
        ))
        db.send_create_signal('scrape_crime', ['Crime'])

    models = {
        'scrape_crime.location': {
            'Meta': {'object_name': 'Location'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'community_area': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '14', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '14', 'blank': 'True'}),
            'needs_recoding': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['scrape_crime']