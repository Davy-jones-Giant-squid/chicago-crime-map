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
            ('case_number', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('domestic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('arrest', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Location'])),
            ('location_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('primary_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('beat', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('ward', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('iucr', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('fbi_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('scrape_crime', ['Crime'])

        # Adding model 'Location'
        db.create_table('scrape_crime_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=14)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=14)),
            ('needs_recoding', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('community_area', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
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
            'beat': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'case_number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'domestic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fbi_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iucr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape_crime.Location']"}),
            'location_description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'primary_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {}),
            'ward': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        'scrape_crime.location': {
            'Meta': {'object_name': 'Location'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'community_area': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '14'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '14'}),
            'needs_recoding': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['scrape_crime']