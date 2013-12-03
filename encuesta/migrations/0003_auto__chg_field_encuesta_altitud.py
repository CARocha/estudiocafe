# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Encuesta.altitud'
        db.alter_column(u'encuesta_encuesta', 'altitud', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Encuesta.altitud'
        db.alter_column(u'encuesta_encuesta', 'altitud', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    models = {
        u'encuesta.aguafinca': {
            'Meta': {'object_name': 'AguaFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.beneficios': {
            'Meta': {'object_name': 'Beneficios'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.combustible': {
            'Meta': {'object_name': 'Combustible'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.composicion': {
            'Meta': {'object_name': 'Composicion'},
            'adultas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'adultos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'educacion_dueno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'educacion_maxima_hombre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'educacion_maxima_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'jovenes_varones': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ninas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'permanente_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'permanente_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relacion_finca_vivienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.ViveFamilia']", 'null': 'True', 'blank': 'True'}),
            'tecnico_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tecnico_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temporales_hombres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temporales_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'encuesta.creditoe': {
            'Meta': {'object_name': 'CreditoE'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.dequien': {
            'Meta': {'object_name': 'DeQuien'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.duenofinca': {
            'Meta': {'object_name': 'DuenoFinca'},
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'altitud': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        u'encuesta.energiafinca': {
            'Meta': {'object_name': 'EnergiaFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.entrevistado': {
            'Meta': {'object_name': 'Entrevistado'},
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.meses': {
            'Meta': {'object_name': 'Meses'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.necesidadalimento': {
            'Meta': {'object_name': 'NecesidadAlimento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.quienfinancia': {
            'Meta': {'object_name': 'QuienFinancia'},
            'beneficio_ser_socio': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'beneficiario_socio'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Beneficios']"}),
            'de_quien': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'quien'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.DeQuien']"}),
            'desde': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'socios'", 'symmetrical': 'False', 'to': u"orm['encuesta.SocioOrganizacion']"}),
            'tiene_credito': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'credito'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.CreditoE']"})
        },
        u'encuesta.recolector': {
            'Meta': {'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.seguridad': {
            'Meta': {'object_name': 'Seguridad'},
            'compra_alimento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cubrir_necesidades': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses_dificiles': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dificiles'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'porque_no_cubre': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cubre'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.NecesidadAlimento']"}),
            'soluciones_crisis': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'crisis'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.TiemposCrisis']"})
        },
        u'encuesta.serviciosbasicos': {
            'Meta': {'object_name': 'ServiciosBasicos'},
            'agua_consumo_humano': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'consumo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.AguaFinca']"}),
            'agua_trabajo_finca': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trabaja'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.AguaFinca']"}),
            'combustible': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'combustible'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Combustible']"}),
            'electricidad': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'electricidad'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.EnergiaFinca']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'encuesta.socioorganizacion': {
            'Meta': {'object_name': 'SocioOrganizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.tenecia': {
            'Meta': {'object_name': 'Tenecia'},
            'documento': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'encuesta.tiemposcrisis': {
            'Meta': {'object_name': 'TiemposCrisis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.vivefamilia': {
            'Meta': {'object_name': 'ViveFamilia'},
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
        }
    }

    complete_apps = ['encuesta']