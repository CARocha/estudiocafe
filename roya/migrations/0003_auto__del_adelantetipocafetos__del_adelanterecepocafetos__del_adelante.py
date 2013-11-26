# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AdelanteTipoCafetos'
        db.delete_table(u'roya_adelantetipocafetos')

        # Deleting model 'AdelanteRecepoCafetos'
        db.delete_table(u'roya_adelanterecepocafetos')

        # Deleting model 'AdelanteFertilizacion'
        db.delete_table(u'roya_adelantefertilizacion')

        # Deleting model 'AdelanteTipoVariedad'
        db.delete_table(u'roya_adelantetipovariedad')

        # Deleting model 'AdelantePodaCafetos'
        db.delete_table(u'roya_adelantepodacafetos')

        # Deleting model 'AdelanteTipoSombra'
        db.delete_table(u'roya_adelantetiposombra')

        # Deleting model 'AdelanteManejoSombra'
        db.delete_table(u'roya_adelantemanejosombra')

        # Deleting model 'AdelanteAplicacionFungicida'
        db.delete_table(u'roya_adelanteaplicacionfungicida')

        # Deleting model 'AdelanteManejoFertilizacion'
        db.delete_table(u'roya_adelantemanejofertilizacion')

        # Deleting model 'AdelanteTipoAplicacionFungicida'
        db.delete_table(u'roya_adelantetipoaplicacionfungicida')

        # Deleting model 'AdelanteRenovacionCafetales'
        db.delete_table(u'roya_adelanterenovacioncafetales')

        # Adding model 'VariedadRecepo'
        db.create_table(u'roya_variedadrecepo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['VariedadRecepo'])

        # Adding model 'Fotos'
        db.create_table(u'roya_fotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['Fotos'])


        # Changing field 'ManejoFertilizacion.mz_2014'
        db.alter_column(u'roya_manejofertilizacion', 'mz_2014', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ManejoFertilizacion.mz_2012'
        db.alter_column(u'roya_manejofertilizacion', 'mz_2012', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ManejoFertilizacion.tipo_2012'
        db.alter_column(u'roya_manejofertilizacion', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.Fertilizacion']))

        # Changing field 'ManejoFertilizacion.tipo_2014'
        db.alter_column(u'roya_manejofertilizacion', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.Fertilizacion']))

        # Changing field 'ImpactoRoya.trece'
        db.alter_column(u'roya_impactoroya', 'trece', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ImpactoRoya.catorce'
        db.alter_column(u'roya_impactoroya', 'catorce', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ImpactoRoya.doce'
        db.alter_column(u'roya_impactoroya', 'doce', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'CapacitacionesSociales.gratis'
        db.alter_column(u'roya_capacitacionessociales', 'gratis', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'CapacitacionesSociales.cuantas'
        db.alter_column(u'roya_capacitacionessociales', 'cuantas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'CapacitacionesSociales.profesor'
        db.alter_column(u'roya_capacitacionessociales', 'profesor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Capacitor'], null=True))

        # Changing field 'NivelFinca.mas'
        db.alter_column(u'roya_nivelfinca', 'mas_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Mas'], null=True))

        # Changing field 'NivelFinca.otros_productos'
        db.alter_column(u'roya_nivelfinca', 'otros_productos', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'NivelFinca.area'
        db.alter_column(u'roya_nivelfinca', 'area', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'NivelFinca.igual'
        db.alter_column(u'roya_nivelfinca', 'igual_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Igual'], null=True))

        # Changing field 'NivelFinca.produccion'
        db.alter_column(u'roya_nivelfinca', 'produccion', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'NivelFinca.menos'
        db.alter_column(u'roya_nivelfinca', 'menos_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Menos'], null=True))

        # Changing field 'NivelFinca.variedades'
        db.alter_column(u'roya_nivelfinca', 'variedades', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Deleting field 'RenovacionCafetales.mz_2014'
        db.delete_column(u'roya_renovacioncafetales', 'mz_2014')

        # Deleting field 'RenovacionCafetales.mz_2012'
        db.delete_column(u'roya_renovacioncafetales', 'mz_2012')


        # Changing field 'RenovacionCafetales.tipo_2012'
        db.alter_column(u'roya_renovacioncafetales', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoVariedad']))

        # Changing field 'RenovacionCafetales.tipo_2014'
        db.alter_column(u'roya_renovacioncafetales', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoVariedad']))
        # Deleting field 'PodaCafetos.mz_2014'
        db.delete_column(u'roya_podacafetos', 'mz_2014')

        # Deleting field 'PodaCafetos.mz_2012'
        db.delete_column(u'roya_podacafetos', 'mz_2012')


        # Changing field 'PodaCafetos.tipo_2012'
        db.alter_column(u'roya_podacafetos', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoCafetos']))

        # Changing field 'PodaCafetos.tipo_2014'
        db.alter_column(u'roya_podacafetos', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoCafetos']))
        # Adding field 'DetalleIncidenciaRoya.postula'
        db.add_column(u'roya_detalleincidenciaroya', 'postula',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)


        # Changing field 'DetalleIncidenciaRoya.edad'
        db.alter_column(u'roya_detalleincidenciaroya', 'edad', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.nivel'
        db.alter_column(u'roya_detalleincidenciaroya', 'nivel', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.dosis'
        db.alter_column(u'roya_detalleincidenciaroya', 'dosis', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.afectadas'
        db.alter_column(u'roya_detalleincidenciaroya', 'afectadas', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.area'
        db.alter_column(u'roya_detalleincidenciaroya', 'area', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.planta'
        db.alter_column(u'roya_detalleincidenciaroya', 'planta', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.hojas'
        db.alter_column(u'roya_detalleincidenciaroya', 'hojas', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.variedad'
        db.alter_column(u'roya_detalleincidenciaroya', 'variedad', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.aplicaciones'
        db.alter_column(u'roya_detalleincidenciaroya', 'aplicaciones', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DetalleIncidenciaRoya.sombra'
        db.alter_column(u'roya_detalleincidenciaroya', 'sombra', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'NoLeGusta.porque'
        db.alter_column(u'roya_nolegusta', 'porque', self.gf('django.db.models.fields.TextField')(null=True))
        # Deleting field 'ManejoSombra.mz_2014'
        db.delete_column(u'roya_manejosombra', 'mz_2014')

        # Deleting field 'ManejoSombra.mz_2012'
        db.delete_column(u'roya_manejosombra', 'mz_2012')


        # Changing field 'ManejoSombra.tipo_2012'
        db.alter_column(u'roya_manejosombra', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoSombra']))

        # Changing field 'ManejoSombra.tipo_2014'
        db.alter_column(u'roya_manejosombra', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoSombra']))

        # Changing field 'CapacitacionesTecnicas.gratis'
        db.alter_column(u'roya_capacitacionestecnicas', 'gratis', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'CapacitacionesTecnicas.cuantas'
        db.alter_column(u'roya_capacitacionestecnicas', 'cuantas', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'CapacitacionesTecnicas.profesor'
        db.alter_column(u'roya_capacitacionestecnicas', 'profesor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Capacitor'], null=True))

        # Changing field 'SiLeGusta.porque'
        db.alter_column(u'roya_silegusta', 'porque', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'AplicacionFungicida.mz_2014'
        db.alter_column(u'roya_aplicacionfungicida', 'mz_2014', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'AplicacionFungicida.mz_2012'
        db.alter_column(u'roya_aplicacionfungicida', 'mz_2012', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'AplicacionFungicida.dosis_2014'
        db.alter_column(u'roya_aplicacionfungicida', 'dosis_2014', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'AplicacionFungicida.dosis_2012'
        db.alter_column(u'roya_aplicacionfungicida', 'dosis_2012', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'AplicacionFungicida.tipo_2012'
        db.alter_column(u'roya_aplicacionfungicida', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoAplicacionFungicida']))

        # Changing field 'AplicacionFungicida.tipo_2014'
        db.alter_column(u'roya_aplicacionfungicida', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['roya.TipoAplicacionFungicida']))

        # Changing field 'NuevosProductos.cantidad'
        db.alter_column(u'roya_nuevosproductos', 'cantidad', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'NuevosProductos.frecuencia'
        db.alter_column(u'roya_nuevosproductos', 'frecuencia', self.gf('django.db.models.fields.FloatField')(null=True))
        # Deleting field 'RecepoCafetos.mz_2014'
        db.delete_column(u'roya_recepocafetos', 'mz_2014')

        # Deleting field 'RecepoCafetos.mz_2012'
        db.delete_column(u'roya_recepocafetos', 'mz_2012')

        # Adding field 'RecepoCafetos.variedad_2012'
        db.add_column(u'roya_recepocafetos', 'variedad_2012',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='recepo_2012', null=True, to=orm['roya.VariedadRecepo']),
                      keep_default=False)

        # Adding field 'RecepoCafetos.variedad_2014'
        db.add_column(u'roya_recepocafetos', 'variedad_2014',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='recepo_2014', null=True, to=orm['roya.VariedadRecepo']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'AdelanteTipoCafetos'
        db.create_table(u'roya_adelantetipocafetos', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoCafetos'])

        # Adding model 'AdelanteRecepoCafetos'
        db.create_table(u'roya_adelanterecepocafetos', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'roya', ['AdelanteRecepoCafetos'])

        # Adding model 'AdelanteFertilizacion'
        db.create_table(u'roya_adelantefertilizacion', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'roya', ['AdelanteFertilizacion'])

        # Adding model 'AdelanteTipoVariedad'
        db.create_table(u'roya_adelantetipovariedad', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoVariedad'])

        # Adding model 'AdelantePodaCafetos'
        db.create_table(u'roya_adelantepodacafetos', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.AdelanteTipoCafetos'])),
        ))
        db.send_create_signal(u'roya', ['AdelantePodaCafetos'])

        # Adding model 'AdelanteTipoSombra'
        db.create_table(u'roya_adelantetiposombra', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoSombra'])

        # Adding model 'AdelanteManejoSombra'
        db.create_table(u'roya_adelantemanejosombra', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.TipoSombra'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteManejoSombra'])

        # Adding model 'AdelanteAplicacionFungicida'
        db.create_table(u'roya_adelanteaplicacionfungicida', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('dosis_2016', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.TipoAplicacionFungicida'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteAplicacionFungicida'])

        # Adding model 'AdelanteManejoFertilizacion'
        db.create_table(u'roya_adelantemanejofertilizacion', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.Fertilizacion'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteManejoFertilizacion'])

        # Adding model 'AdelanteTipoAplicacionFungicida'
        db.create_table(u'roya_adelantetipoaplicacionfungicida', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoAplicacionFungicida'])

        # Adding model 'AdelanteRenovacionCafetales'
        db.create_table(u'roya_adelanterenovacioncafetales', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.AdelanteTipoVariedad'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteRenovacionCafetales'])

        # Deleting model 'VariedadRecepo'
        db.delete_table(u'roya_variedadrecepo')

        # Deleting model 'Fotos'
        db.delete_table(u'roya_fotos')


        # Changing field 'ManejoFertilizacion.mz_2014'
        db.alter_column(u'roya_manejofertilizacion', 'mz_2014', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'ManejoFertilizacion.mz_2012'
        db.alter_column(u'roya_manejofertilizacion', 'mz_2012', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'ManejoFertilizacion.tipo_2012'
        db.alter_column(u'roya_manejofertilizacion', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Fertilizacion']))

        # Changing field 'ManejoFertilizacion.tipo_2014'
        db.alter_column(u'roya_manejofertilizacion', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Fertilizacion']))

        # Changing field 'ImpactoRoya.trece'
        db.alter_column(u'roya_impactoroya', 'trece', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'ImpactoRoya.catorce'
        db.alter_column(u'roya_impactoroya', 'catorce', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'ImpactoRoya.doce'
        db.alter_column(u'roya_impactoroya', 'doce', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'CapacitacionesSociales.gratis'
        db.alter_column(u'roya_capacitacionessociales', 'gratis', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'CapacitacionesSociales.cuantas'
        db.alter_column(u'roya_capacitacionessociales', 'cuantas', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'CapacitacionesSociales.profesor'
        db.alter_column(u'roya_capacitacionessociales', 'profesor_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Capacitor']))

        # Changing field 'NivelFinca.mas'
        db.alter_column(u'roya_nivelfinca', 'mas_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Mas']))

        # Changing field 'NivelFinca.otros_productos'
        db.alter_column(u'roya_nivelfinca', 'otros_productos', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'NivelFinca.area'
        db.alter_column(u'roya_nivelfinca', 'area', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'NivelFinca.igual'
        db.alter_column(u'roya_nivelfinca', 'igual_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Igual']))

        # Changing field 'NivelFinca.produccion'
        db.alter_column(u'roya_nivelfinca', 'produccion', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'NivelFinca.menos'
        db.alter_column(u'roya_nivelfinca', 'menos_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Menos']))

        # Changing field 'NivelFinca.variedades'
        db.alter_column(u'roya_nivelfinca', 'variedades', self.gf('django.db.models.fields.IntegerField')(default=None))
        # Adding field 'RenovacionCafetales.mz_2014'
        db.add_column(u'roya_renovacioncafetales', 'mz_2014',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)

        # Adding field 'RenovacionCafetales.mz_2012'
        db.add_column(u'roya_renovacioncafetales', 'mz_2012',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)


        # Changing field 'RenovacionCafetales.tipo_2012'
        db.alter_column(u'roya_renovacioncafetales', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoVariedad']))

        # Changing field 'RenovacionCafetales.tipo_2014'
        db.alter_column(u'roya_renovacioncafetales', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoVariedad']))
        # Adding field 'PodaCafetos.mz_2014'
        db.add_column(u'roya_podacafetos', 'mz_2014',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)

        # Adding field 'PodaCafetos.mz_2012'
        db.add_column(u'roya_podacafetos', 'mz_2012',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)


        # Changing field 'PodaCafetos.tipo_2012'
        db.alter_column(u'roya_podacafetos', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoCafetos']))

        # Changing field 'PodaCafetos.tipo_2014'
        db.alter_column(u'roya_podacafetos', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoCafetos']))
        # Deleting field 'DetalleIncidenciaRoya.postula'
        db.delete_column(u'roya_detalleincidenciaroya', 'postula')


        # Changing field 'DetalleIncidenciaRoya.edad'
        db.alter_column(u'roya_detalleincidenciaroya', 'edad', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.nivel'
        db.alter_column(u'roya_detalleincidenciaroya', 'nivel', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.dosis'
        db.alter_column(u'roya_detalleincidenciaroya', 'dosis', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.afectadas'
        db.alter_column(u'roya_detalleincidenciaroya', 'afectadas', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.area'
        db.alter_column(u'roya_detalleincidenciaroya', 'area', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.planta'
        db.alter_column(u'roya_detalleincidenciaroya', 'planta', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.hojas'
        db.alter_column(u'roya_detalleincidenciaroya', 'hojas', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.variedad'
        db.alter_column(u'roya_detalleincidenciaroya', 'variedad', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.aplicaciones'
        db.alter_column(u'roya_detalleincidenciaroya', 'aplicaciones', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'DetalleIncidenciaRoya.sombra'
        db.alter_column(u'roya_detalleincidenciaroya', 'sombra', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'NoLeGusta.porque'
        db.alter_column(u'roya_nolegusta', 'porque', self.gf('django.db.models.fields.TextField')(default=None))
        # Adding field 'ManejoSombra.mz_2014'
        db.add_column(u'roya_manejosombra', 'mz_2014',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)

        # Adding field 'ManejoSombra.mz_2012'
        db.add_column(u'roya_manejosombra', 'mz_2012',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)


        # Changing field 'ManejoSombra.tipo_2012'
        db.alter_column(u'roya_manejosombra', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoSombra']))

        # Changing field 'ManejoSombra.tipo_2014'
        db.alter_column(u'roya_manejosombra', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoSombra']))

        # Changing field 'CapacitacionesTecnicas.gratis'
        db.alter_column(u'roya_capacitacionestecnicas', 'gratis', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'CapacitacionesTecnicas.cuantas'
        db.alter_column(u'roya_capacitacionestecnicas', 'cuantas', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'CapacitacionesTecnicas.profesor'
        db.alter_column(u'roya_capacitacionestecnicas', 'profesor_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.Capacitor']))

        # Changing field 'SiLeGusta.porque'
        db.alter_column(u'roya_silegusta', 'porque', self.gf('django.db.models.fields.TextField')(default=None))

        # Changing field 'AplicacionFungicida.mz_2014'
        db.alter_column(u'roya_aplicacionfungicida', 'mz_2014', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'AplicacionFungicida.mz_2012'
        db.alter_column(u'roya_aplicacionfungicida', 'mz_2012', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'AplicacionFungicida.dosis_2014'
        db.alter_column(u'roya_aplicacionfungicida', 'dosis_2014', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'AplicacionFungicida.dosis_2012'
        db.alter_column(u'roya_aplicacionfungicida', 'dosis_2012', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'AplicacionFungicida.tipo_2012'
        db.alter_column(u'roya_aplicacionfungicida', 'tipo_2012_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoAplicacionFungicida']))

        # Changing field 'AplicacionFungicida.tipo_2014'
        db.alter_column(u'roya_aplicacionfungicida', 'tipo_2014_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['roya.TipoAplicacionFungicida']))

        # Changing field 'NuevosProductos.cantidad'
        db.alter_column(u'roya_nuevosproductos', 'cantidad', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'NuevosProductos.frecuencia'
        db.alter_column(u'roya_nuevosproductos', 'frecuencia', self.gf('django.db.models.fields.FloatField')(default=None))
        # Adding field 'RecepoCafetos.mz_2014'
        db.add_column(u'roya_recepocafetos', 'mz_2014',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)

        # Adding field 'RecepoCafetos.mz_2012'
        db.add_column(u'roya_recepocafetos', 'mz_2012',
                      self.gf('django.db.models.fields.FloatField')(default=None),
                      keep_default=False)

        # Deleting field 'RecepoCafetos.variedad_2012'
        db.delete_column(u'roya_recepocafetos', 'variedad_2012_id')

        # Deleting field 'RecepoCafetos.variedad_2014'
        db.delete_column(u'roya_recepocafetos', 'variedad_2014_id')


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
        u'roya.aplicacionfungicida': {
            'Meta': {'object_name': 'AplicacionFungicida'},
            'dosis_2012': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dosis_2014': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mz_2012': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2012'", 'null': 'True', 'to': u"orm['roya.TipoAplicacionFungicida']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2014'", 'null': 'True', 'to': u"orm['roya.TipoAplicacionFungicida']"})
        },
        u'roya.capacitacionessociales': {
            'Meta': {'object_name': 'CapacitacionesSociales'},
            'cuantas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'gratis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'capacitacion_metodologia'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Capacitor']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.TemasSociales']"})
        },
        u'roya.capacitacionestecnicas': {
            'Meta': {'object_name': 'CapacitacionesTecnicas'},
            'cuantas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'gratis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'metodologia'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Capacitor']", 'null': 'True', 'blank': 'True'}),
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
            'afectadas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'aplicaciones': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dosis': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fertilizacion': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fertilizante'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.TipoFertilizacion']"}),
            'fungicidas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fungicida'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.TipoFungicida']"}),
            'hojas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plantio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Plantio']"}),
            'postula': ('django.db.models.fields.FloatField', [], {}),
            'sombra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'variedad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'roya.fertilizacion': {
            'Meta': {'object_name': 'Fertilizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.fotos': {
            'Meta': {'object_name': 'Fotos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'roya.igual': {
            'Meta': {'object_name': 'Igual'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'roya.impactoroya': {
            'Meta': {'object_name': 'ImpactoRoya'},
            'catorce': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'doce': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Impactos']"}),
            'trece': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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
            'mz_2012': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mz_2014': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2012'", 'null': 'True', 'to': u"orm['roya.Fertilizacion']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2014'", 'null': 'True', 'to': u"orm['roya.Fertilizacion']"})
        },
        u'roya.manejosombra': {
            'Meta': {'object_name': 'ManejoSombra'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2012'", 'null': 'True', 'to': u"orm['roya.TipoSombra']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2014'", 'null': 'True', 'to': u"orm['roya.TipoSombra']"})
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
            'area': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuales': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cuales'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.Variedades']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Igual']", 'null': 'True', 'blank': 'True'}),
            'mas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Mas']", 'null': 'True', 'blank': 'True'}),
            'menos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roya.Menos']", 'null': 'True', 'blank': 'True'}),
            'otros_productos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'produccion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'variedades': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'roya.nolegusta': {
            'Meta': {'object_name': 'NoLeGusta'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'no_metodologia'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'porque': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'roya.nuevosproductos': {
            'Meta': {'object_name': 'NuevosProductos'},
            'cantidad': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
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
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2012'", 'null': 'True', 'to': u"orm['roya.TipoCafetos']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2014'", 'null': 'True', 'to': u"orm['roya.TipoCafetos']"})
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
            'variedad_2012': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recepo_2012'", 'null': 'True', 'to': u"orm['roya.VariedadRecepo']"}),
            'variedad_2014': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recepo_2014'", 'null': 'True', 'to': u"orm['roya.VariedadRecepo']"})
        },
        u'roya.renovacioncafetales': {
            'Meta': {'object_name': 'RenovacionCafetales'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_2012': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2012'", 'null': 'True', 'to': u"orm['roya.TipoVariedad']"}),
            'tipo_2014': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tipo_2014'", 'null': 'True', 'to': u"orm['roya.TipoVariedad']"})
        },
        u'roya.silegusta': {
            'Meta': {'object_name': 'SiLeGusta'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'si_metodologia'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['roya.Metodologia']"}),
            'porque': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
        },
        u'roya.variedadrecepo': {
            'Meta': {'object_name': 'VariedadRecepo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['roya']