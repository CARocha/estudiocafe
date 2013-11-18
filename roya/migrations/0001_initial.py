# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Impactos'
        db.create_table(u'roya_impactos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'roya', ['Impactos'])

        # Adding model 'ImpactoRoya'
        db.create_table(u'roya_impactoroya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('impacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Impactos'])),
            ('doce', self.gf('django.db.models.fields.FloatField')()),
            ('trece', self.gf('django.db.models.fields.FloatField')()),
            ('catorce', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['ImpactoRoya'])

        # Adding model 'TipoCafetos'
        db.create_table(u'roya_tipocafetos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoCafetos'])

        # Adding model 'PodaCafetos'
        db.create_table(u'roya_podacafetos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2012', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2012', to=orm['roya.TipoCafetos'])),
            ('tipo_2014', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2014', to=orm['roya.TipoCafetos'])),
            ('mz_2012', self.gf('django.db.models.fields.FloatField')()),
            ('mz_2014', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['PodaCafetos'])

        # Adding model 'RecepoCafetos'
        db.create_table(u'roya_recepocafetos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mz_2012', self.gf('django.db.models.fields.FloatField')()),
            ('mz_2014', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['RecepoCafetos'])

        # Adding model 'TipoVariedad'
        db.create_table(u'roya_tipovariedad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoVariedad'])

        # Adding model 'RenovacionCafetales'
        db.create_table(u'roya_renovacioncafetales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2012', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2012', to=orm['roya.TipoVariedad'])),
            ('tipo_2014', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2014', to=orm['roya.TipoVariedad'])),
            ('mz_2012', self.gf('django.db.models.fields.FloatField')()),
            ('mz_2014', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['RenovacionCafetales'])

        # Adding model 'TipoSombra'
        db.create_table(u'roya_tiposombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoSombra'])

        # Adding model 'ManejoSombra'
        db.create_table(u'roya_manejosombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2012', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2012', to=orm['roya.TipoSombra'])),
            ('tipo_2014', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2014', to=orm['roya.TipoSombra'])),
            ('mz_2012', self.gf('django.db.models.fields.FloatField')()),
            ('mz_2014', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['ManejoSombra'])

        # Adding model 'Fertilizacion'
        db.create_table(u'roya_fertilizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['Fertilizacion'])

        # Adding model 'ManejoFertilizacion'
        db.create_table(u'roya_manejofertilizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2012', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2012', to=orm['roya.Fertilizacion'])),
            ('tipo_2014', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2014', to=orm['roya.Fertilizacion'])),
            ('mz_2012', self.gf('django.db.models.fields.FloatField')()),
            ('mz_2014', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['ManejoFertilizacion'])

        # Adding model 'TipoAplicacionFungicida'
        db.create_table(u'roya_tipoaplicacionfungicida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoAplicacionFungicida'])

        # Adding model 'AplicacionFungicida'
        db.create_table(u'roya_aplicacionfungicida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2012', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2012', to=orm['roya.TipoAplicacionFungicida'])),
            ('tipo_2014', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_2014', to=orm['roya.TipoAplicacionFungicida'])),
            ('mz_2012', self.gf('django.db.models.fields.FloatField')()),
            ('mz_2014', self.gf('django.db.models.fields.FloatField')()),
            ('dosis_2012', self.gf('django.db.models.fields.FloatField')()),
            ('dosis_2014', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AplicacionFungicida'])

        # Adding model 'Combatir'
        db.create_table(u'roya_combatir', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['Combatir'])

        # Adding model 'Oriento'
        db.create_table(u'roya_oriento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['Oriento'])

        # Adding M2M table for field opcion on 'Oriento'
        db.create_table(u'roya_oriento_opcion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('oriento', models.ForeignKey(orm[u'roya.oriento'], null=False)),
            ('combatir', models.ForeignKey(orm[u'roya.combatir'], null=False))
        ))
        db.create_unique(u'roya_oriento_opcion', ['oriento_id', 'combatir_id'])

        # Adding model 'Productos'
        db.create_table(u'roya_productos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['Productos'])

        # Adding model 'NuevosProductos'
        db.create_table(u'roya_nuevosproductos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Productos'])),
            ('frecuencia', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['NuevosProductos'])

        # Adding model 'AdelanteTipoCafetos'
        db.create_table(u'roya_adelantetipocafetos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoCafetos'])

        # Adding model 'AdelantePodaCafetos'
        db.create_table(u'roya_adelantepodacafetos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.AdelanteTipoCafetos'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AdelantePodaCafetos'])

        # Adding model 'AdelanteRecepoCafetos'
        db.create_table(u'roya_adelanterecepocafetos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteRecepoCafetos'])

        # Adding model 'AdelanteTipoVariedad'
        db.create_table(u'roya_adelantetipovariedad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoVariedad'])

        # Adding model 'AdelanteRenovacionCafetales'
        db.create_table(u'roya_adelanterenovacioncafetales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.AdelanteTipoVariedad'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteRenovacionCafetales'])

        # Adding model 'AdelanteTipoSombra'
        db.create_table(u'roya_adelantetiposombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoSombra'])

        # Adding model 'AdelanteManejoSombra'
        db.create_table(u'roya_adelantemanejosombra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.TipoSombra'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteManejoSombra'])

        # Adding model 'AdelanteFertilizacion'
        db.create_table(u'roya_adelantefertilizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['AdelanteFertilizacion'])

        # Adding model 'AdelanteManejoFertilizacion'
        db.create_table(u'roya_adelantemanejofertilizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.Fertilizacion'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteManejoFertilizacion'])

        # Adding model 'AdelanteTipoAplicacionFungicida'
        db.create_table(u'roya_adelantetipoaplicacionfungicida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['AdelanteTipoAplicacionFungicida'])

        # Adding model 'AdelanteAplicacionFungicida'
        db.create_table(u'roya_adelanteaplicacionfungicida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_2016', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adelante_tipo_2016', to=orm['roya.TipoAplicacionFungicida'])),
            ('mz_2016', self.gf('django.db.models.fields.FloatField')()),
            ('dosis_2016', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['AdelanteAplicacionFungicida'])

        # Adding model 'Igual'
        db.create_table(u'roya_igual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'roya', ['Igual'])

        # Adding model 'Mas'
        db.create_table(u'roya_mas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'roya', ['Mas'])

        # Adding model 'Menos'
        db.create_table(u'roya_menos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'roya', ['Menos'])

        # Adding model 'Variedades'
        db.create_table(u'roya_variedades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'roya', ['Variedades'])

        # Adding model 'NivelFinca'
        db.create_table(u'roya_nivelfinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('variedades', self.gf('django.db.models.fields.IntegerField')()),
            ('produccion', self.gf('django.db.models.fields.IntegerField')()),
            ('igual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Igual'])),
            ('mas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Mas'])),
            ('menos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Menos'])),
            ('otros_productos', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['NivelFinca'])

        # Adding M2M table for field cuales on 'NivelFinca'
        db.create_table(u'roya_nivelfinca_cuales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nivelfinca', models.ForeignKey(orm[u'roya.nivelfinca'], null=False)),
            ('variedades', models.ForeignKey(orm[u'roya.variedades'], null=False))
        ))
        db.create_unique(u'roya_nivelfinca_cuales', ['nivelfinca_id', 'variedades_id'])

        # Adding model 'TipoCapacitaciones'
        db.create_table(u'roya_tipocapacitaciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoCapacitaciones'])

        # Adding model 'Capacitor'
        db.create_table(u'roya_capacitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['Capacitor'])

        # Adding model 'Metodologia'
        db.create_table(u'roya_metodologia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['Metodologia'])

        # Adding model 'CapacitacionesTecnicas'
        db.create_table(u'roya_capacitacionestecnicas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.TipoCapacitaciones'])),
            ('cuantas', self.gf('django.db.models.fields.IntegerField')()),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Capacitor'])),
            ('gratis', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['CapacitacionesTecnicas'])

        # Adding M2M table for field metodologia on 'CapacitacionesTecnicas'
        db.create_table(u'roya_capacitacionestecnicas_metodologia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('capacitacionestecnicas', models.ForeignKey(orm[u'roya.capacitacionestecnicas'], null=False)),
            ('metodologia', models.ForeignKey(orm[u'roya.metodologia'], null=False))
        ))
        db.create_unique(u'roya_capacitacionestecnicas_metodologia', ['capacitacionestecnicas_id', 'metodologia_id'])

        # Adding model 'TemasSociales'
        db.create_table(u'roya_temassociales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TemasSociales'])

        # Adding model 'CapacitacionesSociales'
        db.create_table(u'roya_capacitacionessociales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.TemasSociales'])),
            ('cuantas', self.gf('django.db.models.fields.IntegerField')()),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Capacitor'])),
            ('gratis', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['CapacitacionesSociales'])

        # Adding M2M table for field metodologia on 'CapacitacionesSociales'
        db.create_table(u'roya_capacitacionessociales_metodologia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('capacitacionessociales', models.ForeignKey(orm[u'roya.capacitacionessociales'], null=False)),
            ('metodologia', models.ForeignKey(orm[u'roya.metodologia'], null=False))
        ))
        db.create_unique(u'roya_capacitacionessociales_metodologia', ['capacitacionessociales_id', 'metodologia_id'])

        # Adding model 'SiLeGusta'
        db.create_table(u'roya_silegusta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porque', self.gf('django.db.models.fields.TextField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['SiLeGusta'])

        # Adding M2M table for field metodologia on 'SiLeGusta'
        db.create_table(u'roya_silegusta_metodologia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('silegusta', models.ForeignKey(orm[u'roya.silegusta'], null=False)),
            ('metodologia', models.ForeignKey(orm[u'roya.metodologia'], null=False))
        ))
        db.create_unique(u'roya_silegusta_metodologia', ['silegusta_id', 'metodologia_id'])

        # Adding model 'NoLeGusta'
        db.create_table(u'roya_nolegusta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porque', self.gf('django.db.models.fields.TextField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['NoLeGusta'])

        # Adding M2M table for field metodologia on 'NoLeGusta'
        db.create_table(u'roya_nolegusta_metodologia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nolegusta', models.ForeignKey(orm[u'roya.nolegusta'], null=False)),
            ('metodologia', models.ForeignKey(orm[u'roya.metodologia'], null=False))
        ))
        db.create_unique(u'roya_nolegusta_metodologia', ['nolegusta_id', 'metodologia_id'])

        # Adding model 'Plantio'
        db.create_table(u'roya_plantio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['Plantio'])

        # Adding model 'TipoFertilizacion'
        db.create_table(u'roya_tipofertilizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoFertilizacion'])

        # Adding model 'TipoFungicida'
        db.create_table(u'roya_tipofungicida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'roya', ['TipoFungicida'])

        # Adding model 'DetalleIncidenciaRoya'
        db.create_table(u'roya_detalleincidenciaroya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roya.Plantio'])),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('planta', self.gf('django.db.models.fields.IntegerField')()),
            ('edad', self.gf('django.db.models.fields.FloatField')()),
            ('variedad', self.gf('django.db.models.fields.IntegerField')()),
            ('sombra', self.gf('django.db.models.fields.IntegerField')()),
            ('nivel', self.gf('django.db.models.fields.FloatField')()),
            ('dosis', self.gf('django.db.models.fields.FloatField')()),
            ('aplicaciones', self.gf('django.db.models.fields.FloatField')()),
            ('afectadas', self.gf('django.db.models.fields.FloatField')()),
            ('hojas', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'roya', ['DetalleIncidenciaRoya'])

        # Adding M2M table for field fertilizacion on 'DetalleIncidenciaRoya'
        db.create_table(u'roya_detalleincidenciaroya_fertilizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('detalleincidenciaroya', models.ForeignKey(orm[u'roya.detalleincidenciaroya'], null=False)),
            ('tipofertilizacion', models.ForeignKey(orm[u'roya.tipofertilizacion'], null=False))
        ))
        db.create_unique(u'roya_detalleincidenciaroya_fertilizacion', ['detalleincidenciaroya_id', 'tipofertilizacion_id'])

        # Adding M2M table for field fungicidas on 'DetalleIncidenciaRoya'
        db.create_table(u'roya_detalleincidenciaroya_fungicidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('detalleincidenciaroya', models.ForeignKey(orm[u'roya.detalleincidenciaroya'], null=False)),
            ('tipofungicida', models.ForeignKey(orm[u'roya.tipofungicida'], null=False))
        ))
        db.create_unique(u'roya_detalleincidenciaroya_fungicidas', ['detalleincidenciaroya_id', 'tipofungicida_id'])


    def backwards(self, orm):
        # Deleting model 'Impactos'
        db.delete_table(u'roya_impactos')

        # Deleting model 'ImpactoRoya'
        db.delete_table(u'roya_impactoroya')

        # Deleting model 'TipoCafetos'
        db.delete_table(u'roya_tipocafetos')

        # Deleting model 'PodaCafetos'
        db.delete_table(u'roya_podacafetos')

        # Deleting model 'RecepoCafetos'
        db.delete_table(u'roya_recepocafetos')

        # Deleting model 'TipoVariedad'
        db.delete_table(u'roya_tipovariedad')

        # Deleting model 'RenovacionCafetales'
        db.delete_table(u'roya_renovacioncafetales')

        # Deleting model 'TipoSombra'
        db.delete_table(u'roya_tiposombra')

        # Deleting model 'ManejoSombra'
        db.delete_table(u'roya_manejosombra')

        # Deleting model 'Fertilizacion'
        db.delete_table(u'roya_fertilizacion')

        # Deleting model 'ManejoFertilizacion'
        db.delete_table(u'roya_manejofertilizacion')

        # Deleting model 'TipoAplicacionFungicida'
        db.delete_table(u'roya_tipoaplicacionfungicida')

        # Deleting model 'AplicacionFungicida'
        db.delete_table(u'roya_aplicacionfungicida')

        # Deleting model 'Combatir'
        db.delete_table(u'roya_combatir')

        # Deleting model 'Oriento'
        db.delete_table(u'roya_oriento')

        # Removing M2M table for field opcion on 'Oriento'
        db.delete_table('roya_oriento_opcion')

        # Deleting model 'Productos'
        db.delete_table(u'roya_productos')

        # Deleting model 'NuevosProductos'
        db.delete_table(u'roya_nuevosproductos')

        # Deleting model 'AdelanteTipoCafetos'
        db.delete_table(u'roya_adelantetipocafetos')

        # Deleting model 'AdelantePodaCafetos'
        db.delete_table(u'roya_adelantepodacafetos')

        # Deleting model 'AdelanteRecepoCafetos'
        db.delete_table(u'roya_adelanterecepocafetos')

        # Deleting model 'AdelanteTipoVariedad'
        db.delete_table(u'roya_adelantetipovariedad')

        # Deleting model 'AdelanteRenovacionCafetales'
        db.delete_table(u'roya_adelanterenovacioncafetales')

        # Deleting model 'AdelanteTipoSombra'
        db.delete_table(u'roya_adelantetiposombra')

        # Deleting model 'AdelanteManejoSombra'
        db.delete_table(u'roya_adelantemanejosombra')

        # Deleting model 'AdelanteFertilizacion'
        db.delete_table(u'roya_adelantefertilizacion')

        # Deleting model 'AdelanteManejoFertilizacion'
        db.delete_table(u'roya_adelantemanejofertilizacion')

        # Deleting model 'AdelanteTipoAplicacionFungicida'
        db.delete_table(u'roya_adelantetipoaplicacionfungicida')

        # Deleting model 'AdelanteAplicacionFungicida'
        db.delete_table(u'roya_adelanteaplicacionfungicida')

        # Deleting model 'Igual'
        db.delete_table(u'roya_igual')

        # Deleting model 'Mas'
        db.delete_table(u'roya_mas')

        # Deleting model 'Menos'
        db.delete_table(u'roya_menos')

        # Deleting model 'Variedades'
        db.delete_table(u'roya_variedades')

        # Deleting model 'NivelFinca'
        db.delete_table(u'roya_nivelfinca')

        # Removing M2M table for field cuales on 'NivelFinca'
        db.delete_table('roya_nivelfinca_cuales')

        # Deleting model 'TipoCapacitaciones'
        db.delete_table(u'roya_tipocapacitaciones')

        # Deleting model 'Capacitor'
        db.delete_table(u'roya_capacitor')

        # Deleting model 'Metodologia'
        db.delete_table(u'roya_metodologia')

        # Deleting model 'CapacitacionesTecnicas'
        db.delete_table(u'roya_capacitacionestecnicas')

        # Removing M2M table for field metodologia on 'CapacitacionesTecnicas'
        db.delete_table('roya_capacitacionestecnicas_metodologia')

        # Deleting model 'TemasSociales'
        db.delete_table(u'roya_temassociales')

        # Deleting model 'CapacitacionesSociales'
        db.delete_table(u'roya_capacitacionessociales')

        # Removing M2M table for field metodologia on 'CapacitacionesSociales'
        db.delete_table('roya_capacitacionessociales_metodologia')

        # Deleting model 'SiLeGusta'
        db.delete_table(u'roya_silegusta')

        # Removing M2M table for field metodologia on 'SiLeGusta'
        db.delete_table('roya_silegusta_metodologia')

        # Deleting model 'NoLeGusta'
        db.delete_table(u'roya_nolegusta')

        # Removing M2M table for field metodologia on 'NoLeGusta'
        db.delete_table('roya_nolegusta_metodologia')

        # Deleting model 'Plantio'
        db.delete_table(u'roya_plantio')

        # Deleting model 'TipoFertilizacion'
        db.delete_table(u'roya_tipofertilizacion')

        # Deleting model 'TipoFungicida'
        db.delete_table(u'roya_tipofungicida')

        # Deleting model 'DetalleIncidenciaRoya'
        db.delete_table(u'roya_detalleincidenciaroya')

        # Removing M2M table for field fertilizacion on 'DetalleIncidenciaRoya'
        db.delete_table('roya_detalleincidenciaroya_fertilizacion')

        # Removing M2M table for field fungicidas on 'DetalleIncidenciaRoya'
        db.delete_table('roya_detalleincidenciaroya_fungicidas')


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