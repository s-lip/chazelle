# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Round'
        db.create_table('rounds_round', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('rounds', ['Round'])

        # Adding model 'Puzzle'
        db.create_table('rounds_puzzle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rounds.Round'])),
            ('is_meta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_roundsolution', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('rounds', ['Puzzle'])


    def backwards(self, orm):
        # Deleting model 'Round'
        db.delete_table('rounds_round')

        # Deleting model 'Puzzle'
        db.delete_table('rounds_puzzle')


    models = {
        'rounds.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_meta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_roundsolution': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rounds.Round']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'rounds.round': {
            'Meta': {'object_name': 'Round'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['rounds']