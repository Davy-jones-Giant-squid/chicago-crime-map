# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Crime_spot'
        db.delete_table(u'scrape_crime_crime_spot')

        # Adding model 'CrimeSpot'
        db.create_table(u'scrape_crime_crimespot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coordinates', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Coordinates'], null=True, blank=True)),
            ('community_area', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('community_area_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
        ))
        db.send_create_signal(u'scrape_crime', ['CrimeSpot'])


        # Changing field 'Crime.crime_spot'
        db.alter_column(u'scrape_crime_crime', 'crime_spot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.CrimeSpot'], null=True))

    def backwards(self, orm):
        # Adding model 'Crime_spot'
        db.create_table(u'scrape_crime_crime_spot', (
            ('coordinates', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Coordinates'], null=True, blank=True)),
            ('community_area_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
            ('community_area', self.gf('django.db.models.fields.IntegerField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
        ))
        db.send_create_signal(u'scrape_crime', ['Crime_spot'])

        # Deleting model 'CrimeSpot'
        db.delete_table(u'scrape_crime_crimespot')


        # Changing field 'Crime.crime_spot'
        db.alter_column(u'scrape_crime_crime', 'crime_spot_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Crime_spot'], null=True))

    models = {
        u'scrape_crime.coordinates': {
            'Meta': {'object_name': 'Coordinates'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'scrape_crime.crime': {
            'Meta': {'ordering': "['description']", 'object_name': 'Crime'},
            'arrest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beat': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'case_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'crime_spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scrape_crime.CrimeSpot']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'domestic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fbi_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iucr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'primary_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': "''"}),
            'updated_on': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'ward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"})
        },
        u'scrape_crime.crimespot': {
            'Meta': {'object_name': 'CrimeSpot'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'community_area': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'community_area_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'coordinates': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scrape_crime.Coordinates']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['scrape_crime']