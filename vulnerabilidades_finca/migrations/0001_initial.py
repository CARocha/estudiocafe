# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoClima'
        db.create_table(u'vulnerabilidades_finca_tipoclima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['TipoClima'])

        # Adding model 'TipoYear'
        db.create_table(u'vulnerabilidades_finca_tipoyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['TipoYear'])

        # Adding model 'ElClima'
        db.create_table(u'vulnerabilidades_finca_elclima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clima', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vulnerabilidades_finca.TipoClima'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['ElClima'])

        # Adding M2M table for field fecha on 'ElClima'
        db.create_table(u'vulnerabilidades_finca_elclima_fecha', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('elclima', models.ForeignKey(orm[u'vulnerabilidades_finca.elclima'], null=False)),
            ('tipoyear', models.ForeignKey(orm[u'vulnerabilidades_finca.tipoyear'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_elclima_fecha', ['elclima_id', 'tipoyear_id'])

        # Adding model 'SueloFertilidad'
        db.create_table(u'vulnerabilidades_finca_suelofertilidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('textura', self.gf('django.db.models.fields.IntegerField')()),
            ('profundidad', self.gf('django.db.models.fields.IntegerField')()),
            ('presencia', self.gf('django.db.models.fields.IntegerField')()),
            ('abundancia', self.gf('django.db.models.fields.IntegerField')()),
            ('pendiente', self.gf('django.db.models.fields.IntegerField')()),
            ('drenaje', self.gf('django.db.models.fields.IntegerField')()),
            ('materia_organica', self.gf('django.db.models.fields.IntegerField')()),
            ('preparan', self.gf('django.db.models.fields.IntegerField')()),
            ('fertilidad', self.gf('django.db.models.fields.IntegerField')()),
            ('foliar', self.gf('django.db.models.fields.IntegerField')()),
            ('fertilizacion', self.gf('django.db.models.fields.IntegerField')()),
            ('conservacion', self.gf('django.db.models.fields.IntegerField')()),
            ('obra_conservacion', self.gf('django.db.models.fields.IntegerField')()),
            ('fertil', self.gf('django.db.models.fields.IntegerField')()),
            ('degrados', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['SueloFertilidad'])

        # Adding model 'Plagas'
        db.create_table(u'vulnerabilidades_finca_plagas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['Plagas'])

        # Adding model 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['LasPlagas'])

        # Adding M2M table for field gallo on 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas_gallo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lasplagas', models.ForeignKey(orm[u'vulnerabilidades_finca.lasplagas'], null=False)),
            ('plagas', models.ForeignKey(orm[u'vulnerabilidades_finca.plagas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_lasplagas_gallo', ['lasplagas_id', 'plagas_id'])

        # Adding M2M table for field roya on 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas_roya', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lasplagas', models.ForeignKey(orm[u'vulnerabilidades_finca.lasplagas'], null=False)),
            ('plagas', models.ForeignKey(orm[u'vulnerabilidades_finca.plagas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_lasplagas_roya', ['lasplagas_id', 'plagas_id'])

        # Adding M2M table for field hierro on 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas_hierro', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lasplagas', models.ForeignKey(orm[u'vulnerabilidades_finca.lasplagas'], null=False)),
            ('plagas', models.ForeignKey(orm[u'vulnerabilidades_finca.plagas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_lasplagas_hierro', ['lasplagas_id', 'plagas_id'])

        # Adding M2M table for field antracnosis on 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas_antracnosis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lasplagas', models.ForeignKey(orm[u'vulnerabilidades_finca.lasplagas'], null=False)),
            ('plagas', models.ForeignKey(orm[u'vulnerabilidades_finca.plagas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_lasplagas_antracnosis', ['lasplagas_id', 'plagas_id'])

        # Adding M2M table for field broca on 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas_broca', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lasplagas', models.ForeignKey(orm[u'vulnerabilidades_finca.lasplagas'], null=False)),
            ('plagas', models.ForeignKey(orm[u'vulnerabilidades_finca.plagas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_lasplagas_broca', ['lasplagas_id', 'plagas_id'])

        # Adding M2M table for field nematodos on 'LasPlagas'
        db.create_table(u'vulnerabilidades_finca_lasplagas_nematodos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lasplagas', models.ForeignKey(orm[u'vulnerabilidades_finca.lasplagas'], null=False)),
            ('plagas', models.ForeignKey(orm[u'vulnerabilidades_finca.plagas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_lasplagas_nematodos', ['lasplagas_id', 'plagas_id'])

        # Adding model 'Causa'
        db.create_table(u'vulnerabilidades_finca_causa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['Causa'])

        # Adding model 'Opciones'
        db.create_table(u'vulnerabilidades_finca_opciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('causa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vulnerabilidades_finca.Causa'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['Opciones'])

        # Adding model 'Respuestas'
        db.create_table(u'vulnerabilidades_finca_respuestas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['Respuestas'])

        # Adding model 'OtroRiesgos'
        db.create_table(u'vulnerabilidades_finca_otroriesgos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vulnerabilidades_finca.Opciones'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['OtroRiesgos'])

        # Adding M2M table for field respuesta on 'OtroRiesgos'
        db.create_table(u'vulnerabilidades_finca_otroriesgos_respuesta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('otroriesgos', models.ForeignKey(orm[u'vulnerabilidades_finca.otroriesgos'], null=False)),
            ('respuestas', models.ForeignKey(orm[u'vulnerabilidades_finca.respuestas'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_otroriesgos_respuesta', ['otroriesgos_id', 'respuestas_id'])

        # Adding model 'Mitigacion'
        db.create_table(u'vulnerabilidades_finca_mitigacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monitoreo_plagas', self.gf('django.db.models.fields.IntegerField')()),
            ('cada_cuanto', self.gf('django.db.models.fields.IntegerField')()),
            ('como_realiza', self.gf('django.db.models.fields.IntegerField')()),
            ('registro_monitoreo', self.gf('django.db.models.fields.IntegerField')()),
            ('recursos', self.gf('django.db.models.fields.IntegerField')()),
            ('falta_recursos', self.gf('django.db.models.fields.IntegerField')()),
            ('almacenamiento', self.gf('django.db.models.fields.IntegerField')()),
            ('forma_organizada', self.gf('django.db.models.fields.IntegerField')()),
            ('contrato', self.gf('django.db.models.fields.IntegerField')()),
            ('certificado', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_certificado', self.gf('django.db.models.fields.IntegerField')()),
            ('reconocida', self.gf('django.db.models.fields.IntegerField')()),
            ('infraestructura', self.gf('django.db.models.fields.IntegerField')()),
            ('plan_manejo', self.gf('django.db.models.fields.IntegerField')()),
            ('plan_negocio', self.gf('django.db.models.fields.IntegerField')()),
            ('plan_inversion', self.gf('django.db.models.fields.IntegerField')()),
            ('elaborar', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['Mitigacion'])


    def backwards(self, orm):
        # Deleting model 'TipoClima'
        db.delete_table(u'vulnerabilidades_finca_tipoclima')

        # Deleting model 'TipoYear'
        db.delete_table(u'vulnerabilidades_finca_tipoyear')

        # Deleting model 'ElClima'
        db.delete_table(u'vulnerabilidades_finca_elclima')

        # Removing M2M table for field fecha on 'ElClima'
        db.delete_table('vulnerabilidades_finca_elclima_fecha')

        # Deleting model 'SueloFertilidad'
        db.delete_table(u'vulnerabilidades_finca_suelofertilidad')

        # Deleting model 'Plagas'
        db.delete_table(u'vulnerabilidades_finca_plagas')

        # Deleting model 'LasPlagas'
        db.delete_table(u'vulnerabilidades_finca_lasplagas')

        # Removing M2M table for field gallo on 'LasPlagas'
        db.delete_table('vulnerabilidades_finca_lasplagas_gallo')

        # Removing M2M table for field roya on 'LasPlagas'
        db.delete_table('vulnerabilidades_finca_lasplagas_roya')

        # Removing M2M table for field hierro on 'LasPlagas'
        db.delete_table('vulnerabilidades_finca_lasplagas_hierro')

        # Removing M2M table for field antracnosis on 'LasPlagas'
        db.delete_table('vulnerabilidades_finca_lasplagas_antracnosis')

        # Removing M2M table for field broca on 'LasPlagas'
        db.delete_table('vulnerabilidades_finca_lasplagas_broca')

        # Removing M2M table for field nematodos on 'LasPlagas'
        db.delete_table('vulnerabilidades_finca_lasplagas_nematodos')

        # Deleting model 'Causa'
        db.delete_table(u'vulnerabilidades_finca_causa')

        # Deleting model 'Opciones'
        db.delete_table(u'vulnerabilidades_finca_opciones')

        # Deleting model 'Respuestas'
        db.delete_table(u'vulnerabilidades_finca_respuestas')

        # Deleting model 'OtroRiesgos'
        db.delete_table(u'vulnerabilidades_finca_otroriesgos')

        # Removing M2M table for field respuesta on 'OtroRiesgos'
        db.delete_table('vulnerabilidades_finca_otroriesgos_respuesta')

        # Deleting model 'Mitigacion'
        db.delete_table(u'vulnerabilidades_finca_mitigacion')


    models = {
        u'encuesta.duenofinca': {
            'Meta': {'object_name': 'DuenoFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'altitud': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'beneficiario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Organizacion']"}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'dueno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.DuenoFinca']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Entrevistado']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'encuesta.entrevistado': {
            'Meta': {'object_name': 'Entrevistado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.recolector': {
            'Meta': {'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'vulnerabilidades_finca.causa': {
            'Meta': {'object_name': 'Causa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'vulnerabilidades_finca.elclima': {
            'Meta': {'object_name': 'ElClima'},
            'clima': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vulnerabilidades_finca.TipoClima']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fecha'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.TipoYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'vulnerabilidades_finca.lasplagas': {
            'Meta': {'object_name': 'LasPlagas'},
            'antracnosis': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'antracnosis'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'broca': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'broca'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            'gallo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'gallo'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'hierro': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'hierro'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nematodos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'nematodos'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'roya': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'roya'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"})
        },
        u'vulnerabilidades_finca.mitigacion': {
            'Meta': {'object_name': 'Mitigacion'},
            'almacenamiento': ('django.db.models.fields.IntegerField', [], {}),
            'cada_cuanto': ('django.db.models.fields.IntegerField', [], {}),
            'certificado': ('django.db.models.fields.IntegerField', [], {}),
            'como_realiza': ('django.db.models.fields.IntegerField', [], {}),
            'contrato': ('django.db.models.fields.IntegerField', [], {}),
            'elaborar': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'falta_recursos': ('django.db.models.fields.IntegerField', [], {}),
            'forma_organizada': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.IntegerField', [], {}),
            'monitoreo_plagas': ('django.db.models.fields.IntegerField', [], {}),
            'plan_inversion': ('django.db.models.fields.IntegerField', [], {}),
            'plan_manejo': ('django.db.models.fields.IntegerField', [], {}),
            'plan_negocio': ('django.db.models.fields.IntegerField', [], {}),
            'reconocida': ('django.db.models.fields.IntegerField', [], {}),
            'recursos': ('django.db.models.fields.IntegerField', [], {}),
            'registro_monitoreo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_certificado': ('django.db.models.fields.IntegerField', [], {})
        },
        u'vulnerabilidades_finca.opciones': {
            'Meta': {'object_name': 'Opciones'},
            'causa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vulnerabilidades_finca.Causa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'vulnerabilidades_finca.otroriesgos': {
            'Meta': {'object_name': 'OtroRiesgos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vulnerabilidades_finca.Opciones']"}),
            'respuesta': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Respuestas']", 'null': 'True', 'blank': 'True'})
        },
        u'vulnerabilidades_finca.plagas': {
            'Meta': {'object_name': 'Plagas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'vulnerabilidades_finca.respuestas': {
            'Meta': {'object_name': 'Respuestas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'vulnerabilidades_finca.suelofertilidad': {
            'Meta': {'object_name': 'SueloFertilidad'},
            'abundancia': ('django.db.models.fields.IntegerField', [], {}),
            'conservacion': ('django.db.models.fields.IntegerField', [], {}),
            'degrados': ('django.db.models.fields.IntegerField', [], {}),
            'drenaje': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fertil': ('django.db.models.fields.IntegerField', [], {}),
            'fertilidad': ('django.db.models.fields.IntegerField', [], {}),
            'fertilizacion': ('django.db.models.fields.IntegerField', [], {}),
            'foliar': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_organica': ('django.db.models.fields.IntegerField', [], {}),
            'obra_conservacion': ('django.db.models.fields.IntegerField', [], {}),
            'pendiente': ('django.db.models.fields.IntegerField', [], {}),
            'preparan': ('django.db.models.fields.IntegerField', [], {}),
            'presencia': ('django.db.models.fields.IntegerField', [], {}),
            'profundidad': ('django.db.models.fields.IntegerField', [], {}),
            'textura': ('django.db.models.fields.IntegerField', [], {})
        },
        u'vulnerabilidades_finca.tipoclima': {
            'Meta': {'object_name': 'TipoClima'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'vulnerabilidades_finca.tipoyear': {
            'Meta': {'object_name': 'TipoYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['vulnerabilidades_finca']