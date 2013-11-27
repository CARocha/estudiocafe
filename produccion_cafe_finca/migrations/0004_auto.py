# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field mes_manejo_maleza on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_manejo_maleza', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_manejo_maleza', ['mesesmanejocafe_id', 'meses_id'])


    def backwards(self, orm):
        # Removing M2M table for field mes_manejo_maleza on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_manejo_maleza')


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
        u'encuesta.meses': {
            'Meta': {'object_name': 'Meses'},
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
        u'produccion_cafe_finca.areacafe': {
            'Meta': {'object_name': 'AreaCafe'},
            'catorse': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'doce': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.EstadoActual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'once': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trece': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.beneficiado': {
            'Meta': {'object_name': 'Beneficiado'},
            'beneficiado_seco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.BeneficioSeco']", 'null': 'True', 'blank': 'True'}),
            'calibran': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cortes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuanto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'despulpan_fermentan': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'despulpar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'determina_calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.CalidadCafe']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fermentan': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orean': ('django.db.models.fields.IntegerField', [], {}),
            'precio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'revisan': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'separan': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.beneficioseco': {
            'Meta': {'object_name': 'BeneficioSeco'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_cafe_finca.calidadcafe': {
            'Meta': {'object_name': 'CalidadCafe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_cafe_finca.comercializacion': {
            'Meta': {'object_name': 'Comercializacion'},
            'c_precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'c_venta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'e_precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'e_venta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            'i_precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'i_venta_cafe': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.credito': {
            'Meta': {'object_name': 'Credito'},
            'cobertura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cobertura_necesidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'credito_largo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'credito_mediano': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'facilidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'necesidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.criterios': {
            'Meta': {'object_name': 'Criterios'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.decidesembrar': {
            'Meta': {'object_name': 'DecideSembrar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.estadoactual': {
            'Meta': {'object_name': 'EstadoActual'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.manejocafetales': {
            'Meta': {'object_name': 'ManejoCafetales'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            'fertilizante_foliares': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'foliares'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'fertilizante_suelo': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'suelo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'fungicidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fungicida'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insecticidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'insecticida'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'manejo_cafeto': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cafeto'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'manejo_maleza': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'maleza'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'manejo_sombra': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sombra'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'nematicidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nematicidas'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"})
        },
        u'produccion_cafe_finca.manejos': {
            'Meta': {'object_name': 'Manejos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.manejotejidos': {
            'Meta': {'object_name': 'ManejoTejidos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tejido': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['produccion_cafe_finca.TipoTejido']", 'symmetrical': 'False'})
        },
        u'produccion_cafe_finca.mesesmanejocafe': {
            'Meta': {'object_name': 'MesesManejoCafe'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_fertilizante_foliares': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fertilizante_foliares'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_fertilizante_suelo': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fertilizante_suelo'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_fungicidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'mes_fungicidas'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_insecticidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'mes_insecticida'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_manejo_cafeto': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'manejo_cefeto'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_manejo_maleza': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'manejo_maleza'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_manejo_sombra': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'manejo_sombra'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_nematicidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'mes_nematicidas'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"})
        },
        u'produccion_cafe_finca.nombretipos': {
            'Meta': {'object_name': 'NombreTipos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.opciones': {
            'Meta': {'object_name': 'Opciones'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_cafe_finca.plantio': {
            'Meta': {'object_name': 'Plantio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.produccionvivero': {
            'Meta': {'object_name': 'ProduccionVivero'},
            'consigue_semilla': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'semilla'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Semilla']"}),
            'criterio': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'criterio'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Criterios']"}),
            'decide': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'decide'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.DecideSembrar']"}),
            'disponible': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'disponible'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Variedades']"}),
            'edad_planta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagar_catimore': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pagar_caturra': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pagar_hibrida': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_finca': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_injertadas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_vender': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_vivero': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'resistente_roya': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'resistente'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.ResistenteRoya']"}),
            'variedad': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'variedad'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Variedades']"}),
            'variedad_predomindante': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['produccion_cafe_finca.VariedadPredominante']", 'symmetrical': 'False'}),
            'vivero_finca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.resistenteroya': {
            'Meta': {'object_name': 'ResistenteRoya'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.semilla': {
            'Meta': {'object_name': 'Semilla'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.tiposinsumos': {
            'Meta': {'object_name': 'TiposInsumos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.tipotejido': {
            'Meta': {'object_name': 'TipoTejido'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_cafe_finca.usoinsumos': {
            'Meta': {'object_name': 'UsoInsumos'},
            'aplicaciones': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'momento': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'momento'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.NombreTipos']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.TiposInsumos']"}),
            'unidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.usoopcionesagroecologica': {
            'Meta': {'object_name': 'UsoOpcionesAgroecologica'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'opcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.Opciones']", 'null': 'True', 'blank': 'True'})
        },
        u'produccion_cafe_finca.variedadedadroya': {
            'Meta': {'object_name': 'VariedadEdadRoya'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'edad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_roya': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_plantio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.Plantio']"}),
            'produccion_2012': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'produccion_2013': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'produccion_2014': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'variedades': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'variedades'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Variedades']"})
        },
        u'produccion_cafe_finca.variedades': {
            'Meta': {'object_name': 'Variedades'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.variedadpredominante': {
            'Meta': {'object_name': 'VariedadPredominante'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['produccion_cafe_finca']