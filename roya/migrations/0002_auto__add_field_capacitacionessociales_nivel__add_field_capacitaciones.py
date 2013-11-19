# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CapacitacionesSociales.nivel'
        db.add_column(u'roya_capacitacionessociales', 'nivel',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CapacitacionesTecnicas.nivel'
        db.add_column(u'roya_capacitacionestecnicas', 'nivel',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CapacitacionesSociales.nivel'
        db.delete_column(u'roya_capacitacionessociales', 'nivel')

        # Deleting field 'CapacitacionesTecnicas.nivel'
        db.delete_column(u'roya_capacitacionestecnicas', 'nivel')


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
        u'roya.adelanteaplicacionfungicida': {
            'Meta': {'object_name': 'AdelanteAplicacionFungicida'},
            'dosis_2016': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2016': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2016': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adelante_tipo_2016'", 'to': u"orm['roya.TipoAplicacionFungicida']"})
        },
        u'roya.adelantefertilizacion': {
            'Meta': {'object_name': 'AdelanteFertilizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.adelantemanejofertilizacion': {
            'Meta': {'object_name': 'AdelanteManejoFertilizacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2016': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2016': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adelante_tipo_2016'", 'to': u"orm['roya.Fertilizacion']"})
        },
        u'roya.adelantemanejosombra': {
            'Meta': {'object_name': 'AdelanteManejoSombra'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2016': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2016': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adelante_tipo_2016'", 'to': u"orm['roya.TipoSombra']"})
        },
        u'roya.adelantepodacafetos': {
            'Meta': {'object_name': 'AdelantePodaCafetos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2016': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2016': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adelante_tipo_2016'", 'to': u"orm['roya.AdelanteTipoCafetos']"})
        },
        u'roya.adelanterecepocafetos': {
            'Meta': {'object_name': 'AdelanteRecepoCafetos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2016': ('django.db.models.fields.FloatField', [], {})
        },
        u'roya.adelanterenovacioncafetales': {
            'Meta': {'object_name': 'AdelanteRenovacionCafetales'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2016': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2016': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adelante_tipo_2016'", 'to': u"orm['roya.AdelanteTipoVariedad']"})
        },
        u'roya.adelantetipoaplicacionfungicida': {
            'Meta': {'object_name': 'AdelanteTipoAplicacionFungicida'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.adelantetipocafetos': {
            'Meta': {'object_name': 'AdelanteTipoCafetos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.adelantetiposombra': {
            'Meta': {'object_name': 'AdelanteTipoSombra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.adelantetipovariedad': {
            'Meta': {'object_name': 'AdelanteTipoVariedad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.aplicacionfungicida': {
            'Meta': {'object_name': 'AplicacionFungicida'},
            'dosis_2012': ('django.db.models.fields.FloatField', [], {}),
            'dosis_2014': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2012'", 'to': u"orm['roya.TipoAplicacionFungicida']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2014'", 'to': u"orm['roya.TipoAplicacionFungicida']"})
        },
        u'roya.capacitacionessociales': {
            'Meta': {'object_name': 'CapacitacionesSociales'},
            'cuantas': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'gratis': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'capacitacion_metodologia'", 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Capacitor']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.TemasSociales']"})
        },
        u'roya.capacitacionestecnicas': {
            'Meta': {'object_name': 'CapacitacionesTecnicas'},
            'cuantas': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'gratis': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'metodologia'", 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Capacitor']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.TipoCapacitaciones']"})
        },
        u'roya.capacitor': {
            'Meta': {'object_name': 'Capacitor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.combatir': {
            'Meta': {'object_name': 'Combatir'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.detalleincidenciaroya': {
            'Meta': {'object_name': 'DetalleIncidenciaRoya'},
            'afectadas': ('django.db.models.fields.FloatField', [], {}),
            'aplicaciones': ('django.db.models.fields.FloatField', [], {}),
            'area': ('django.db.models.fields.FloatField', [], {}),
            'dosis': ('django.db.models.fields.FloatField', [], {}),
            'edad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fertilizacion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fertilizante'", 'symmetrical': 'False', 'to': u"orm['roya.TipoFertilizacion']"}),
            'fungicidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fungicida'", 'symmetrical': 'False', 'to': u"orm['roya.TipoFungicida']"}),
            'hojas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.FloatField', [], {}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'plantio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Plantio']"}),
            'sombra': ('django.db.models.fields.IntegerField', [], {}),
            'variedad': ('django.db.models.fields.IntegerField', [], {})
        },
        u'roya.fertilizacion': {
            'Meta': {'object_name': 'Fertilizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.igual': {
            'Meta': {'object_name': 'Igual'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'roya.impactoroya': {
            'Meta': {'object_name': 'ImpactoRoya'},
            'catorce': ('django.db.models.fields.FloatField', [], {}),
            'doce': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Impactos']"}),
            'trece': ('django.db.models.fields.FloatField', [], {})
        },
        u'roya.impactos': {
            'Meta': {'object_name': 'Impactos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'roya.manejofertilizacion': {
            'Meta': {'object_name': 'ManejoFertilizacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2012'", 'to': u"orm['roya.Fertilizacion']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2014'", 'to': u"orm['roya.Fertilizacion']"})
        },
        u'roya.manejosombra': {
            'Meta': {'object_name': 'ManejoSombra'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2012'", 'to': u"orm['roya.TipoSombra']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2014'", 'to': u"orm['roya.TipoSombra']"})
        },
        u'roya.mas': {
            'Meta': {'object_name': 'Mas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'roya.menos': {
            'Meta': {'object_name': 'Menos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'roya.metodologia': {
            'Meta': {'object_name': 'Metodologia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.nivelfinca': {
            'Meta': {'object_name': 'NivelFinca'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'cuales': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cuales'", 'symmetrical': 'False', 'to': u"orm['roya.Variedades']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Igual']"}),
            'mas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Mas']"}),
            'menos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Menos']"}),
            'otros_productos': ('django.db.models.fields.IntegerField', [], {}),
            'produccion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'variedades': ('django.db.models.fields.IntegerField', [], {})
        },
        u'roya.nolegusta': {
            'Meta': {'object_name': 'NoLeGusta'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'no_metodologia'", 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'porque': ('django.db.models.fields.TextField', [], {})
        },
        u'roya.nuevosproductos': {
            'Meta': {'object_name': 'NuevosProductos'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Productos']"})
        },
        u'roya.oriento': {
            'Meta': {'object_name': 'Oriento'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'opcion'", 'symmetrical': 'False', 'to': u"orm['roya.Combatir']"})
        },
        u'roya.plantio': {
            'Meta': {'object_name': 'Plantio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.podacafetos': {
            'Meta': {'object_name': 'PodaCafetos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2012'", 'to': u"orm['roya.TipoCafetos']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2014'", 'to': u"orm['roya.TipoCafetos']"})
        },
        u'roya.productos': {
            'Meta': {'object_name': 'Productos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.recepocafetos': {
            'Meta': {'object_name': 'RecepoCafetos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {})
        },
        u'roya.renovacioncafetales': {
            'Meta': {'object_name': 'RenovacionCafetales'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2012'", 'to': u"orm['roya.TipoVariedad']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_2014'", 'to': u"orm['roya.TipoVariedad']"})
        },
        u'roya.silegusta': {
            'Meta': {'object_name': 'SiLeGusta'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'si_metodologia'", 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'porque': ('django.db.models.fields.TextField', [], {})
        },
        u'roya.temassociales': {
            'Meta': {'object_name': 'TemasSociales'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tipoaplicacionfungicida': {
            'Meta': {'object_name': 'TipoAplicacionFungicida'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tipocafetos': {
            'Meta': {'object_name': 'TipoCafetos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tipocapacitaciones': {
            'Meta': {'object_name': 'TipoCapacitaciones'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tipofertilizacion': {
            'Meta': {'object_name': 'TipoFertilizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tipofungicida': {
            'Meta': {'object_name': 'TipoFungicida'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tiposombra': {
            'Meta': {'object_name': 'TipoSombra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.tipovariedad': {
            'Meta': {'object_name': 'TipoVariedad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.variedades': {
            'Meta': {'object_name': 'Variedades'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['roya']