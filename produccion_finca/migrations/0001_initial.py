# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Uso'
        db.create_table(u'produccion_finca_uso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'produccion_finca', ['Uso'])

        # Adding model 'UsoTierra'
        db.create_table(u'produccion_finca_usotierra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tierra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.Uso'], null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['UsoTierra'])

        # Adding model 'Actividad'
        db.create_table(u'produccion_finca_actividad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'produccion_finca', ['Actividad'])

        # Adding model 'Reforestacion'
        db.create_table(u'produccion_finca_reforestacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reforestacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.Actividad'])),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['Reforestacion'])

        # Adding model 'Animales'
        db.create_table(u'produccion_finca_animales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'produccion_finca', ['Animales'])

        # Adding model 'Productos'
        db.create_table(u'produccion_finca_productos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_finca', ['Productos'])

        # Adding model 'ProductosPatio'
        db.create_table(u'produccion_finca_productospatio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_finca', ['ProductosPatio'])

        # Adding model 'AnimalesFinca'
        db.create_table(u'produccion_finca_animalesfinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('animales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.Animales'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['AnimalesFinca'])

        # Adding model 'ProductoFinca'
        db.create_table(u'produccion_finca_productofinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.Productos'], null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('total_produccion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('consumo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('venta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['ProductoFinca'])

        # Adding model 'ProductoPatio'
        db.create_table(u'produccion_finca_productopatio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.ProductosPatio'], null=True, blank=True)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('total_produccion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('consumo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('venta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['ProductoPatio'])

        # Adding model 'Rubros'
        db.create_table(u'produccion_finca_rubros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categoria', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'produccion_finca', ['Rubros'])

        # Adding model 'IngresoFamiliar'
        db.create_table(u'produccion_finca_ingresofamiliar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.Rubros'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('quien_vendio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('maneja_negocio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['IngresoFamiliar'])

        # Adding model 'Fuentes'
        db.create_table(u'produccion_finca_fuentes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_finca', ['Fuentes'])

        # Adding model 'TipoTrabajo'
        db.create_table(u'produccion_finca_tipotrabajo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'produccion_finca', ['TipoTrabajo'])

        # Adding model 'OtrosIngresos'
        db.create_table(u'produccion_finca_otrosingresos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.Fuentes'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_finca.TipoTrabajo'], null=True, blank=True)),
            ('meses', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ingreso', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tiene_ingreso', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_finca', ['OtrosIngresos'])


    def backwards(self, orm):
        # Deleting model 'Uso'
        db.delete_table(u'produccion_finca_uso')

        # Deleting model 'UsoTierra'
        db.delete_table(u'produccion_finca_usotierra')

        # Deleting model 'Actividad'
        db.delete_table(u'produccion_finca_actividad')

        # Deleting model 'Reforestacion'
        db.delete_table(u'produccion_finca_reforestacion')

        # Deleting model 'Animales'
        db.delete_table(u'produccion_finca_animales')

        # Deleting model 'Productos'
        db.delete_table(u'produccion_finca_productos')

        # Deleting model 'ProductosPatio'
        db.delete_table(u'produccion_finca_productospatio')

        # Deleting model 'AnimalesFinca'
        db.delete_table(u'produccion_finca_animalesfinca')

        # Deleting model 'ProductoFinca'
        db.delete_table(u'produccion_finca_productofinca')

        # Deleting model 'ProductoPatio'
        db.delete_table(u'produccion_finca_productopatio')

        # Deleting model 'Rubros'
        db.delete_table(u'produccion_finca_rubros')

        # Deleting model 'IngresoFamiliar'
        db.delete_table(u'produccion_finca_ingresofamiliar')

        # Deleting model 'Fuentes'
        db.delete_table(u'produccion_finca_fuentes')

        # Deleting model 'TipoTrabajo'
        db.delete_table(u'produccion_finca_tipotrabajo')

        # Deleting model 'OtrosIngresos'
        db.delete_table(u'produccion_finca_otrosingresos')


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
        u'produccion_finca.actividad': {
            'Meta': {'object_name': 'Actividad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_finca.animales': {
            'Meta': {'object_name': 'Animales'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'produccion_finca.animalesfinca': {
            'Meta': {'object_name': 'AnimalesFinca'},
            'animales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.Animales']"}),
            'cantidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'produccion_finca.fuentes': {
            'Meta': {'object_name': 'Fuentes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_finca.ingresofamiliar': {
            'Meta': {'object_name': 'IngresoFamiliar'},
            'cantidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneja_negocio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'quien_vendio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.Rubros']"})
        },
        u'produccion_finca.otrosingresos': {
            'Meta': {'object_name': 'OtrosIngresos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.Fuentes']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tiene_ingreso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.TipoTrabajo']", 'null': 'True', 'blank': 'True'})
        },
        u'produccion_finca.productofinca': {
            'Meta': {'object_name': 'ProductoFinca'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'consumo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.Productos']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_produccion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'venta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_finca.productopatio': {
            'Meta': {'object_name': 'ProductoPatio'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'consumo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.ProductosPatio']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_produccion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'venta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_finca.productos': {
            'Meta': {'object_name': 'Productos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_finca.productospatio': {
            'Meta': {'object_name': 'ProductosPatio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_finca.reforestacion': {
            'Meta': {'object_name': 'Reforestacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reforestacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.Actividad']"}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'produccion_finca.rubros': {
            'Meta': {'object_name': 'Rubros'},
            'categoria': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_finca.tipotrabajo': {
            'Meta': {'object_name': 'TipoTrabajo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_finca.uso': {
            'Meta': {'object_name': 'Uso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'produccion_finca.usotierra': {
            'Meta': {'object_name': 'UsoTierra'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tierra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_finca.Uso']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['produccion_finca']