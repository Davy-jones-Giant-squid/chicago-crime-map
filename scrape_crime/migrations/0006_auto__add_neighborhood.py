# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Neighborhood'
        db.create_table(u'scrape_crime_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank='')),
        ))
        db.send_create_signal(u'scrape_crime', ['Neighborhood'])

        # Adding M2M table for field coordinates on 'Neighborhood'
        m2m_table_name = db.shorten_name(u'scrape_crime_neighborhood_coordinates')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('neighborhood', models.ForeignKey(orm[u'scrape_crime.neighborhood'], null=False)),
            ('coordinates', models.ForeignKey(orm[u'scrape_crime.coordinates'], null=False))
        ))
        db.create_unique(m2m_table_name, ['neighborhood_id', 'coordinates_id'])


    def backwards(self, orm):
        # Deleting model 'Neighborhood'
        db.delete_table(u'scrape_crime_neighborhood')

        # Removing M2M table for field coordinates on 'Neighborhood'
        db.delete_table(db.shorten_name(u'scrape_crime_neighborhood_coordinates'))


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
            'case_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': "''"}),
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
        },
        u'scrape_crime.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'coordinates': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['scrape_crime.Coordinates']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': "''"})
        }
    }

    complete_apps = ['scrape_crime']