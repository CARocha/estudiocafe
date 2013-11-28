# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ElaboraPlanes'
        db.create_table(u'vulnerabilidades_finca_elaboraplanes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['ElaboraPlanes'])

        # Adding model 'TiposCertificados'
        db.create_table(u'vulnerabilidades_finca_tiposcertificados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'vulnerabilidades_finca', ['TiposCertificados'])

        # Deleting field 'Mitigacion.elaborar'
        db.delete_column(u'vulnerabilidades_finca_mitigacion', 'elaborar')

        # Deleting field 'Mitigacion.tipo_certificado'
        db.delete_column(u'vulnerabilidades_finca_mitigacion', 'tipo_certificado')

        # Adding M2M table for field tipos_certificados on 'Mitigacion'
        db.create_table(u'vulnerabilidades_finca_mitigacion_tipos_certificados', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mitigacion', models.ForeignKey(orm[u'vulnerabilidades_finca.mitigacion'], null=False)),
            ('tiposcertificados', models.ForeignKey(orm[u'vulnerabilidades_finca.tiposcertificados'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_mitigacion_tipos_certificados', ['mitigacion_id', 'tiposcertificados_id'])

        # Adding M2M table for field elabora on 'Mitigacion'
        db.create_table(u'vulnerabilidades_finca_mitigacion_elabora', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mitigacion', models.ForeignKey(orm[u'vulnerabilidades_finca.mitigacion'], null=False)),
            ('elaboraplanes', models.ForeignKey(orm[u'vulnerabilidades_finca.elaboraplanes'], null=False))
        ))
        db.create_unique(u'vulnerabilidades_finca_mitigacion_elabora', ['mitigacion_id', 'elaboraplanes_id'])


    def backwards(self, orm):
        # Deleting model 'ElaboraPlanes'
        db.delete_table(u'vulnerabilidades_finca_elaboraplanes')

        # Deleting model 'TiposCertificados'
        db.delete_table(u'vulnerabilidades_finca_tiposcertificados')

        # Adding field 'Mitigacion.elaborar'
        db.add_column(u'vulnerabilidades_finca_mitigacion', 'elaborar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Mitigacion.tipo_certificado'
        db.add_column(u'vulnerabilidades_finca_mitigacion', 'tipo_certificado',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field tipos_certificados on 'Mitigacion'
        db.delete_table('vulnerabilidades_finca_mitigacion_tipos_certificados')

        # Removing M2M table for field elabora on 'Mitigacion'
        db.delete_table('vulnerabilidades_finca_mitigacion_elabora')


    models = {
        u'encuesta.duenofinca': {
            'Meta': {'object_name': 'DuenoFinca'},
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'altitud': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'beneficiarios': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['encuesta.Organizacion']", 'null': 'True', 'blank': 'True'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'dueno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.DuenoFinca']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Entrevistado']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'position': ('geoposition.fields.GeopositionField', [], {'max_length': '42', 'null': 'True', 'blank': 'True'}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'encuesta.entrevistado': {
            'Meta': {'object_name': 'Entrevistado'},
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
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
        u'vulnerabilidades_finca.elaboraplanes': {
            'Meta': {'object_name': 'ElaboraPlanes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'vulnerabilidades_finca.elclima': {
            'Meta': {'object_name': 'ElClima'},
            'clima': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vulnerabilidades_finca.TipoClima']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fecha'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.TipoYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'vulnerabilidades_finca.faltarecurso': {
            'Meta': {'object_name': 'FaltaRecurso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'vulnerabilidades_finca.lasplagas': {
            'Meta': {'object_name': 'LasPlagas'},
            'antracnosis': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'antracnosis'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'broca': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'broca'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gallo': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'gallo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'hierro': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hierro'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nematodos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'nematodos'", 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"}),
            'roya': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'roya'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.Plagas']"})
        },
        u'vulnerabilidades_finca.mitigacion': {
            'Meta': {'object_name': 'Mitigacion'},
            'almacenamiento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cada_cuanto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'certificado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'como_realiza': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'contrato': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'elabora': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.ElaboraPlanes']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'falta_recurso': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['vulnerabilidades_finca.FaltaRecurso']", 'symmetrical': 'False'}),
            'forma_organizada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'monitoreo_plagas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plan_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plan_manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plan_negocio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'puntaje': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reconocida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recursos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'registro_monitoreo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipos_certificados': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vulnerabilidades_finca.TiposCertificados']", 'null': 'True', 'blank': 'True'})
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
            'abundancia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conservacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'degrados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drenaje': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fertil': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fertilidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fertilizacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'foliar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_organica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'obra_conservacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pendiente': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preparan': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'presencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profundidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'textura': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'vulnerabilidades_finca.tipoclima': {
            'Meta': {'object_name': 'TipoClima'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'vulnerabilidades_finca.tiposcertificados': {
            'Meta': {'object_name': 'TiposCertificados'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'vulnerabilidades_finca.tipoyear': {
            'Meta': {'object_name': 'TipoYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['vulnerabilidades_finca']