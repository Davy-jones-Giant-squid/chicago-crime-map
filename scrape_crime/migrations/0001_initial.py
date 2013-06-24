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
            ('location_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scrape_crime', ['Crime'])

    def backwards(self, orm):
        # Deleting model 'Crime'
        db.delete_table('scrape_crime_crime')

    models = {
        'scrape_crime.crime': {
            'Meta': {'object_name': 'Crime'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_description': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['scrape_crime']