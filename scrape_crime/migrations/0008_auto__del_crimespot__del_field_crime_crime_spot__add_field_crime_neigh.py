# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CrimeSpot'
        db.delete_table(u'scrape_crime_crimespot')

        # Deleting field 'Crime.crime_spot'
        db.delete_column(u'scrape_crime_crime', 'crime_spot_id')

        # Adding field 'Crime.neighborhood'
        db.add_column(u'scrape_crime_crime', 'neighborhood',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Neighborhood'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crime.crime_coordinates'
        db.add_column(u'scrape_crime_crime', 'crime_coordinates',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Coordinates'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crime.block'
        db.add_column(u'scrape_crime_crime', 'block',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=''),
                      keep_default=False)

        # Adding field 'Neighborhood.area_number'
        db.add_column(u'scrape_crime_neighborhood', 'area_number',
                      self.gf('django.db.models.fields.IntegerField')(default=False),
                      keep_default=False)


        # Changing field 'Neighborhood.name'
        db.alter_column(u'scrape_crime_neighborhood', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255))

    def backwards(self, orm):
        # Adding model 'CrimeSpot'
        db.create_table(u'scrape_crime_crimespot', (
            ('coordinates', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.Coordinates'], null=True, blank=True)),
            ('community_area_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
            ('community_area', self.gf('django.db.models.fields.IntegerField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
        ))
        db.send_create_signal(u'scrape_crime', ['CrimeSpot'])

        # Adding field 'Crime.crime_spot'
        db.add_column(u'scrape_crime_crime', 'crime_spot',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape_crime.CrimeSpot'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Crime.neighborhood'
        db.delete_column(u'scrape_crime_crime', 'neighborhood_id')

        # Deleting field 'Crime.crime_coordinates'
        db.delete_column(u'scrape_crime_crime', 'crime_coordinates_id')

        # Deleting field 'Crime.block'
        db.delete_column(u'scrape_crime_crime', 'block')

        # Deleting field 'Neighborhood.area_number'
        db.delete_column(u'scrape_crime_neighborhood', 'area_number')


        # Changing field 'Neighborhood.name'
        db.alter_column(u'scrape_crime_neighborhood', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, null=True))

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
            'block': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'case_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': "''"}),
            'crime_coordinates': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scrape_crime.Coordinates']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'domestic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fbi_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iucr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scrape_crime.Neighborhood']", 'null': 'True', 'blank': 'True'}),
            'primary_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': "''"}),
            'updated_on': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"}),
            'ward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"})
        },
        u'scrape_crime.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'area_number': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'coordinates': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['scrape_crime.Coordinates']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['scrape_crime']