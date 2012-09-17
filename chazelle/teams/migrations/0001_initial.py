# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('teams_team', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('extra_credit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_unlock', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 1, 0, 0))),
        ))
        db.send_create_signal('teams', ['Team'])

        # Adding M2M table for field rounds_unlocked on 'Team'
        db.create_table('teams_team_rounds_unlocked', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['teams.team'], null=False)),
            ('round', models.ForeignKey(orm['rounds.round'], null=False))
        ))
        db.create_unique('teams_team_rounds_unlocked', ['team_id', 'round_id'])

        # Adding M2M table for field puzzles_solved on 'Team'
        db.create_table('teams_team_puzzles_solved', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['teams.team'], null=False)),
            ('puzzle', models.ForeignKey(orm['rounds.puzzle'], null=False))
        ))
        db.create_unique('teams_team_puzzles_solved', ['team_id', 'puzzle_id'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('teams_team')

        # Removing M2M table for field rounds_unlocked on 'Team'
        db.delete_table('teams_team_rounds_unlocked')

        # Removing M2M table for field puzzles_solved on 'Team'
        db.delete_table('teams_team_puzzles_solved')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        'teams.team': {
            'Meta': {'object_name': 'Team', '_ormbases': ['auth.User']},
            'extra_credit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_unlock': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 1, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'puzzles_solved': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['rounds.Puzzle']", 'symmetrical': 'False'}),
            'rounds_unlocked': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['rounds.Round']", 'symmetrical': 'False'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['teams']