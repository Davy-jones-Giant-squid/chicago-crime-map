# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crime'
        db.create_table('scrape_crime_crime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case_number', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank='')),
            ('domestic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('arrest', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank='')),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Location'], null=True, blank=True)),
            ('location_description', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank='')),
            ('primary_type', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank='')),
            ('beat', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('ward', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('iucr', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank='')),
            ('updated_on', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank='')),
            ('fbi_code', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal('scrape_crime', ['Crime'])

        # Adding model 'Location'
        db.create_table('scrape_crime_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=14, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=14, blank=True)),
            ('needs_recoding', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('community_area', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
        ))
        db.send_create_signal('scrape_crime', ['Location'])

    def backwards(self, orm):
        # Deleting model 'Crime'
        db.delete_table('scrape_crime_crime')

        # Deleting model 'Location'
        db.delete_table('scrape_crime_location')

    models = {
        'scrape_crime.crime': {
            'Meta': {'ordering': "['description']", 'object_name': 'Crime'},
            'arrest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beat': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': "''"}),
            'case_number': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': "''"}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': "''"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': "''"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': "''"}),
            'domestic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fbi_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iucr': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': "''"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape_crime.Location']", 'null': 'True', 'blank': 'True'}),
            'location_description': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': "''"}),
            'primary_type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': "''"}),
            'updated_on': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': "''"}),
            'ward': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': "''"})
        },
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