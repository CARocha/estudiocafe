# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EstadoActual'
        db.create_table(u'produccion_cafe_finca_estadoactual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['EstadoActual'])

        # Adding model 'AreaCafe'
        db.create_table(u'produccion_cafe_finca_areacafe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.EstadoActual'])),
            ('once', self.gf('django.db.models.fields.FloatField')()),
            ('doce', self.gf('django.db.models.fields.FloatField')()),
            ('trece', self.gf('django.db.models.fields.FloatField')()),
            ('catorse', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['AreaCafe'])

        # Adding model 'Plantio'
        db.create_table(u'produccion_cafe_finca_plantio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Plantio'])

        # Adding model 'Variedades'
        db.create_table(u'produccion_cafe_finca_variedades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Variedades'])

        # Adding model 'VariedadEdadRoya'
        db.create_table(u'produccion_cafe_finca_variedadedadroya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_plantio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.Plantio'])),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('produccion_2012', self.gf('django.db.models.fields.FloatField')()),
            ('produccion_2013', self.gf('django.db.models.fields.FloatField')()),
            ('produccion_2014', self.gf('django.db.models.fields.FloatField')()),
            ('nivel_roya', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['VariedadEdadRoya'])

        # Adding M2M table for field variedades on 'VariedadEdadRoya'
        db.create_table(u'produccion_cafe_finca_variedadedadroya_variedades', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('variedadedadroya', models.ForeignKey(orm[u'produccion_cafe_finca.variedadedadroya'], null=False)),
            ('variedades', models.ForeignKey(orm[u'produccion_cafe_finca.variedades'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_variedadedadroya_variedades', ['variedadedadroya_id', 'variedades_id'])

        # Adding model 'ResistenteRoya'
        db.create_table(u'produccion_cafe_finca_resistenteroya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['ResistenteRoya'])

        # Adding model 'Semilla'
        db.create_table(u'produccion_cafe_finca_semilla', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Semilla'])

        # Adding model 'DecideSembrar'
        db.create_table(u'produccion_cafe_finca_decidesembrar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['DecideSembrar'])

        # Adding model 'Criterios'
        db.create_table(u'produccion_cafe_finca_criterios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Criterios'])

        # Adding model 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vivero_finca', self.gf('django.db.models.fields.IntegerField')()),
            ('plantas_vivero', self.gf('django.db.models.fields.FloatField')()),
            ('plantas_finca', self.gf('django.db.models.fields.FloatField')()),
            ('plantas_vender', self.gf('django.db.models.fields.FloatField')()),
            ('plantas_injertadas', self.gf('django.db.models.fields.FloatField')()),
            ('edad_planta', self.gf('django.db.models.fields.FloatField')()),
            ('costo_planta_caturra', self.gf('django.db.models.fields.FloatField')()),
            ('costo_planta_catimore', self.gf('django.db.models.fields.FloatField')()),
            ('costo_planta_hibridas', self.gf('django.db.models.fields.FloatField')()),
            ('pagar_caturra', self.gf('django.db.models.fields.FloatField')()),
            ('pagar_catimore', self.gf('django.db.models.fields.FloatField')()),
            ('pagar_hibrida', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['ProduccionVivero'])

        # Adding M2M table for field variedad on 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero_variedad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionvivero', models.ForeignKey(orm[u'produccion_cafe_finca.produccionvivero'], null=False)),
            ('variedades', models.ForeignKey(orm[u'produccion_cafe_finca.variedades'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_produccionvivero_variedad', ['produccionvivero_id', 'variedades_id'])

        # Adding M2M table for field resistente_roya on 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero_resistente_roya', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionvivero', models.ForeignKey(orm[u'produccion_cafe_finca.produccionvivero'], null=False)),
            ('resistenteroya', models.ForeignKey(orm[u'produccion_cafe_finca.resistenteroya'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_produccionvivero_resistente_roya', ['produccionvivero_id', 'resistenteroya_id'])

        # Adding M2M table for field consigue_semilla on 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero_consigue_semilla', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionvivero', models.ForeignKey(orm[u'produccion_cafe_finca.produccionvivero'], null=False)),
            ('semilla', models.ForeignKey(orm[u'produccion_cafe_finca.semilla'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_produccionvivero_consigue_semilla', ['produccionvivero_id', 'semilla_id'])

        # Adding M2M table for field disponible on 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero_disponible', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionvivero', models.ForeignKey(orm[u'produccion_cafe_finca.produccionvivero'], null=False)),
            ('variedades', models.ForeignKey(orm[u'produccion_cafe_finca.variedades'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_produccionvivero_disponible', ['produccionvivero_id', 'variedades_id'])

        # Adding M2M table for field decide on 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero_decide', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionvivero', models.ForeignKey(orm[u'produccion_cafe_finca.produccionvivero'], null=False)),
            ('decidesembrar', models.ForeignKey(orm[u'produccion_cafe_finca.decidesembrar'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_produccionvivero_decide', ['produccionvivero_id', 'decidesembrar_id'])

        # Adding M2M table for field criterio on 'ProduccionVivero'
        db.create_table(u'produccion_cafe_finca_produccionvivero_criterio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionvivero', models.ForeignKey(orm[u'produccion_cafe_finca.produccionvivero'], null=False)),
            ('criterios', models.ForeignKey(orm[u'produccion_cafe_finca.criterios'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_produccionvivero_criterio', ['produccionvivero_id', 'criterios_id'])

        # Adding model 'Manejos'
        db.create_table(u'produccion_cafe_finca_manejos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Manejos'])

        # Adding model 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['ManejoCafetales'])

        # Adding M2M table for field manejo_cafeto on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_manejo_cafeto', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_manejo_cafeto', ['manejocafetales_id', 'manejos_id'])

        # Adding M2M table for field manejo_sombra on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_manejo_sombra', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_manejo_sombra', ['manejocafetales_id', 'manejos_id'])

        # Adding M2M table for field fertilizante_suelo on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_fertilizante_suelo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_fertilizante_suelo', ['manejocafetales_id', 'manejos_id'])

        # Adding M2M table for field fertilizante_foliares on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_fertilizante_foliares', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_fertilizante_foliares', ['manejocafetales_id', 'manejos_id'])

        # Adding M2M table for field fungicidas on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_fungicidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_fungicidas', ['manejocafetales_id', 'manejos_id'])

        # Adding M2M table for field insecticidas on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_insecticidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_insecticidas', ['manejocafetales_id', 'manejos_id'])

        # Adding M2M table for field nematicidas on 'ManejoCafetales'
        db.create_table(u'produccion_cafe_finca_manejocafetales_nematicidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejocafetales', models.ForeignKey(orm[u'produccion_cafe_finca.manejocafetales'], null=False)),
            ('manejos', models.ForeignKey(orm[u'produccion_cafe_finca.manejos'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_manejocafetales_nematicidas', ['manejocafetales_id', 'manejos_id'])

        # Adding model 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['MesesManejoCafe'])

        # Adding M2M table for field mes_manejo_cafeto on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto', ['mesesmanejocafe_id', 'meses_id'])

        # Adding M2M table for field mes_manejo_sombra on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra', ['mesesmanejocafe_id', 'meses_id'])

        # Adding M2M table for field mes_fertilizante_suelo on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo', ['mesesmanejocafe_id', 'meses_id'])

        # Adding M2M table for field mes_fertilizante_foliares on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares', ['mesesmanejocafe_id', 'meses_id'])

        # Adding M2M table for field mes_fungicidas on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_fungicidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_fungicidas', ['mesesmanejocafe_id', 'meses_id'])

        # Adding M2M table for field mes_insecticidas on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_insecticidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_insecticidas', ['mesesmanejocafe_id', 'meses_id'])

        # Adding M2M table for field mes_nematicidas on 'MesesManejoCafe'
        db.create_table(u'produccion_cafe_finca_mesesmanejocafe_mes_nematicidas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mesesmanejocafe', models.ForeignKey(orm[u'produccion_cafe_finca.mesesmanejocafe'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_mesesmanejocafe_mes_nematicidas', ['mesesmanejocafe_id', 'meses_id'])

        # Adding model 'TiposInsumos'
        db.create_table(u'produccion_cafe_finca_tiposinsumos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['TiposInsumos'])

        # Adding model 'NombreTipos'
        db.create_table(u'produccion_cafe_finca_nombretipos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['NombreTipos'])

        # Adding model 'UsoInsumos'
        db.create_table(u'produccion_cafe_finca_usoinsumos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.TiposInsumos'])),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.NombreTipos'])),
            ('aplicaciones', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['UsoInsumos'])

        # Adding M2M table for field momento on 'UsoInsumos'
        db.create_table(u'produccion_cafe_finca_usoinsumos_momento', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usoinsumos', models.ForeignKey(orm[u'produccion_cafe_finca.usoinsumos'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'produccion_cafe_finca_usoinsumos_momento', ['usoinsumos_id', 'meses_id'])

        # Adding model 'Opciones'
        db.create_table(u'produccion_cafe_finca_opciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Opciones'])

        # Adding model 'UsoOpcionesAgroecologica'
        db.create_table(u'produccion_cafe_finca_usoopcionesagroecologica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.Opciones'])),
            ('nivel', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['UsoOpcionesAgroecologica'])

        # Adding model 'BeneficioSeco'
        db.create_table(u'produccion_cafe_finca_beneficioseco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['BeneficioSeco'])

        # Adding model 'CalidadCafe'
        db.create_table(u'produccion_cafe_finca_calidadcafe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['CalidadCafe'])

        # Adding model 'Beneficiado'
        db.create_table(u'produccion_cafe_finca_beneficiado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cortes', self.gf('django.db.models.fields.IntegerField')()),
            ('separan', self.gf('django.db.models.fields.IntegerField')()),
            ('despulpan_fermentan', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
            ('calibran', self.gf('django.db.models.fields.IntegerField')()),
            ('revisan', self.gf('django.db.models.fields.IntegerField')()),
            ('despulpar', self.gf('django.db.models.fields.IntegerField')()),
            ('fermentan', self.gf('django.db.models.fields.IntegerField')()),
            ('orean', self.gf('django.db.models.fields.IntegerField')()),
            ('beneficiado_seco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.BeneficioSeco'])),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
            ('determina_calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['produccion_cafe_finca.CalidadCafe'])),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('cuanto', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Beneficiado'])

        # Adding model 'Comercializacion'
        db.create_table(u'produccion_cafe_finca_comercializacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.IntegerField')()),
            ('p_total', self.gf('django.db.models.fields.FloatField')()),
            ('i_venta_cafe', self.gf('django.db.models.fields.FloatField')()),
            ('i_precio', self.gf('django.db.models.fields.FloatField')()),
            ('c_venta', self.gf('django.db.models.fields.FloatField')()),
            ('c_precio', self.gf('django.db.models.fields.FloatField')()),
            ('e_venta', self.gf('django.db.models.fields.FloatField')()),
            ('e_precio', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Comercializacion'])

        # Adding model 'Credito'
        db.create_table(u'produccion_cafe_finca_credito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.IntegerField')()),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('cobertura', self.gf('django.db.models.fields.FloatField')()),
            ('credito_mediano', self.gf('django.db.models.fields.FloatField')()),
            ('necesidad', self.gf('django.db.models.fields.FloatField')()),
            ('credito_largo', self.gf('django.db.models.fields.FloatField')()),
            ('cobertura_necesidad', self.gf('django.db.models.fields.FloatField')()),
            ('facilidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'produccion_cafe_finca', ['Credito'])


    def backwards(self, orm):
        # Deleting model 'EstadoActual'
        db.delete_table(u'produccion_cafe_finca_estadoactual')

        # Deleting model 'AreaCafe'
        db.delete_table(u'produccion_cafe_finca_areacafe')

        # Deleting model 'Plantio'
        db.delete_table(u'produccion_cafe_finca_plantio')

        # Deleting model 'Variedades'
        db.delete_table(u'produccion_cafe_finca_variedades')

        # Deleting model 'VariedadEdadRoya'
        db.delete_table(u'produccion_cafe_finca_variedadedadroya')

        # Removing M2M table for field variedades on 'VariedadEdadRoya'
        db.delete_table('produccion_cafe_finca_variedadedadroya_variedades')

        # Deleting model 'ResistenteRoya'
        db.delete_table(u'produccion_cafe_finca_resistenteroya')

        # Deleting model 'Semilla'
        db.delete_table(u'produccion_cafe_finca_semilla')

        # Deleting model 'DecideSembrar'
        db.delete_table(u'produccion_cafe_finca_decidesembrar')

        # Deleting model 'Criterios'
        db.delete_table(u'produccion_cafe_finca_criterios')

        # Deleting model 'ProduccionVivero'
        db.delete_table(u'produccion_cafe_finca_produccionvivero')

        # Removing M2M table for field variedad on 'ProduccionVivero'
        db.delete_table('produccion_cafe_finca_produccionvivero_variedad')

        # Removing M2M table for field resistente_roya on 'ProduccionVivero'
        db.delete_table('produccion_cafe_finca_produccionvivero_resistente_roya')

        # Removing M2M table for field consigue_semilla on 'ProduccionVivero'
        db.delete_table('produccion_cafe_finca_produccionvivero_consigue_semilla')

        # Removing M2M table for field disponible on 'ProduccionVivero'
        db.delete_table('produccion_cafe_finca_produccionvivero_disponible')

        # Removing M2M table for field decide on 'ProduccionVivero'
        db.delete_table('produccion_cafe_finca_produccionvivero_decide')

        # Removing M2M table for field criterio on 'ProduccionVivero'
        db.delete_table('produccion_cafe_finca_produccionvivero_criterio')

        # Deleting model 'Manejos'
        db.delete_table(u'produccion_cafe_finca_manejos')

        # Deleting model 'ManejoCafetales'
        db.delete_table(u'produccion_cafe_finca_manejocafetales')

        # Removing M2M table for field manejo_cafeto on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_manejo_cafeto')

        # Removing M2M table for field manejo_sombra on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_manejo_sombra')

        # Removing M2M table for field fertilizante_suelo on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_fertilizante_suelo')

        # Removing M2M table for field fertilizante_foliares on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_fertilizante_foliares')

        # Removing M2M table for field fungicidas on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_fungicidas')

        # Removing M2M table for field insecticidas on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_insecticidas')

        # Removing M2M table for field nematicidas on 'ManejoCafetales'
        db.delete_table('produccion_cafe_finca_manejocafetales_nematicidas')

        # Deleting model 'MesesManejoCafe'
        db.delete_table(u'produccion_cafe_finca_mesesmanejocafe')

        # Removing M2M table for field mes_manejo_cafeto on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_manejo_cafeto')

        # Removing M2M table for field mes_manejo_sombra on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_manejo_sombra')

        # Removing M2M table for field mes_fertilizante_suelo on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_suelo')

        # Removing M2M table for field mes_fertilizante_foliares on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_fertilizante_foliares')

        # Removing M2M table for field mes_fungicidas on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_fungicidas')

        # Removing M2M table for field mes_insecticidas on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_insecticidas')

        # Removing M2M table for field mes_nematicidas on 'MesesManejoCafe'
        db.delete_table('produccion_cafe_finca_mesesmanejocafe_mes_nematicidas')

        # Deleting model 'TiposInsumos'
        db.delete_table(u'produccion_cafe_finca_tiposinsumos')

        # Deleting model 'NombreTipos'
        db.delete_table(u'produccion_cafe_finca_nombretipos')

        # Deleting model 'UsoInsumos'
        db.delete_table(u'produccion_cafe_finca_usoinsumos')

        # Removing M2M table for field momento on 'UsoInsumos'
        db.delete_table('produccion_cafe_finca_usoinsumos_momento')

        # Deleting model 'Opciones'
        db.delete_table(u'produccion_cafe_finca_opciones')

        # Deleting model 'UsoOpcionesAgroecologica'
        db.delete_table(u'produccion_cafe_finca_usoopcionesagroecologica')

        # Deleting model 'BeneficioSeco'
        db.delete_table(u'produccion_cafe_finca_beneficioseco')

        # Deleting model 'CalidadCafe'
        db.delete_table(u'produccion_cafe_finca_calidadcafe')

        # Deleting model 'Beneficiado'
        db.delete_table(u'produccion_cafe_finca_beneficiado')

        # Deleting model 'Comercializacion'
        db.delete_table(u'produccion_cafe_finca_comercializacion')

        # Deleting model 'Credito'
        db.delete_table(u'produccion_cafe_finca_credito')


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
            'catorse': ('django.db.models.fields.FloatField', [], {}),
            'doce': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.EstadoActual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'once': ('django.db.models.fields.FloatField', [], {}),
            'trece': ('django.db.models.fields.FloatField', [], {})
        },
        u'produccion_cafe_finca.beneficiado': {
            'Meta': {'object_name': 'Beneficiado'},
            'beneficiado_seco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.BeneficioSeco']"}),
            'calibran': ('django.db.models.fields.IntegerField', [], {}),
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'cortes': ('django.db.models.fields.IntegerField', [], {}),
            'cuanto': ('django.db.models.fields.FloatField', [], {}),
            'despulpan_fermentan': ('django.db.models.fields.IntegerField', [], {}),
            'despulpar': ('django.db.models.fields.IntegerField', [], {}),
            'determina_calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.CalidadCafe']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'fermentan': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orean': ('django.db.models.fields.IntegerField', [], {}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'revisan': ('django.db.models.fields.IntegerField', [], {}),
            'separan': ('django.db.models.fields.IntegerField', [], {})
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
            'c_precio': ('django.db.models.fields.FloatField', [], {}),
            'c_venta': ('django.db.models.fields.FloatField', [], {}),
            'e_precio': ('django.db.models.fields.FloatField', [], {}),
            'e_venta': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            'i_precio': ('django.db.models.fields.FloatField', [], {}),
            'i_venta_cafe': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_total': ('django.db.models.fields.FloatField', [], {})
        },
        u'produccion_cafe_finca.credito': {
            'Meta': {'object_name': 'Credito'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'cobertura_necesidad': ('django.db.models.fields.FloatField', [], {}),
            'credito_largo': ('django.db.models.fields.FloatField', [], {}),
            'credito_mediano': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'facilidad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'necesidad': ('django.db.models.fields.FloatField', [], {})
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
            'fertilizante_foliares': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'foliares'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'fertilizante_suelo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'suelo'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'fungicidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fungicida'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insecticidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'insecticida'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'manejo_cafeto': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cafeto'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'manejo_sombra': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sombra'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"}),
            'nematicidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'nematicidas'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Manejos']"})
        },
        u'produccion_cafe_finca.manejos': {
            'Meta': {'object_name': 'Manejos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'produccion_cafe_finca.mesesmanejocafe': {
            'Meta': {'object_name': 'MesesManejoCafe'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_fertilizante_foliares': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fertilizante_foliares'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_fertilizante_suelo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fertilizante_suelo'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_fungicidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mes_fungicidas'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_insecticidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mes_insecticida'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_manejo_cafeto': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'manejo_cefeto'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_manejo_sombra': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'manejo_sombra'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'mes_nematicidas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mes_nematicidas'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"})
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
            'consigue_semilla': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'semilla'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Semilla']"}),
            'costo_planta_catimore': ('django.db.models.fields.FloatField', [], {}),
            'costo_planta_caturra': ('django.db.models.fields.FloatField', [], {}),
            'costo_planta_hibridas': ('django.db.models.fields.FloatField', [], {}),
            'criterio': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'criterio'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Criterios']"}),
            'decide': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'decide'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.DecideSembrar']"}),
            'disponible': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'disponible'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Variedades']"}),
            'edad_planta': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagar_catimore': ('django.db.models.fields.FloatField', [], {}),
            'pagar_caturra': ('django.db.models.fields.FloatField', [], {}),
            'pagar_hibrida': ('django.db.models.fields.FloatField', [], {}),
            'plantas_finca': ('django.db.models.fields.FloatField', [], {}),
            'plantas_injertadas': ('django.db.models.fields.FloatField', [], {}),
            'plantas_vender': ('django.db.models.fields.FloatField', [], {}),
            'plantas_vivero': ('django.db.models.fields.FloatField', [], {}),
            'resistente_roya': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'resistente'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.ResistenteRoya']"}),
            'variedad': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'variedad'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Variedades']"}),
            'vivero_finca': ('django.db.models.fields.IntegerField', [], {})
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
        u'produccion_cafe_finca.usoinsumos': {
            'Meta': {'object_name': 'UsoInsumos'},
            'aplicaciones': ('django.db.models.fields.FloatField', [], {}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'momento': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'momento'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.NombreTipos']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.TiposInsumos']"})
        },
        u'produccion_cafe_finca.usoopcionesagroecologica': {
            'Meta': {'object_name': 'UsoOpcionesAgroecologica'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {}),
            'opcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.Opciones']"})
        },
        u'produccion_cafe_finca.variedadedadroya': {
            'Meta': {'object_name': 'VariedadEdadRoya'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_roya': ('django.db.models.fields.FloatField', [], {}),
            'nombre_plantio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['produccion_cafe_finca.Plantio']"}),
            'produccion_2012': ('django.db.models.fields.FloatField', [], {}),
            'produccion_2013': ('django.db.models.fields.FloatField', [], {}),
            'produccion_2014': ('django.db.models.fields.FloatField', [], {}),
            'variedades': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'variedades'", 'symmetrical': 'False', 'to': u"orm['produccion_cafe_finca.Variedades']"})
        },
        u'produccion_cafe_finca.variedades': {
            'Meta': {'object_name': 'Variedades'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['produccion_cafe_finca']