# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entrevistado'
        db.create_table(u'encuesta_entrevistado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['Entrevistado'])

        # Adding model 'DuenoFinca'
        db.create_table(u'encuesta_duenofinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['DuenoFinca'])

        # Adding model 'Organizacion'
        db.create_table(u'encuesta_organizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['Organizacion'])

        # Adding model 'Recolector'
        db.create_table(u'encuesta_recolector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['Recolector'])

        # Adding model 'Encuesta'
        db.create_table(u'encuesta_encuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('recolector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Recolector'])),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Entrevistado'])),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dueno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.DuenoFinca'])),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('finca', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Pais'])),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Comunidad'])),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('altitud', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('beneficiario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Organizacion'])),
        ))
        db.send_create_signal(u'encuesta', ['Encuesta'])

        # Adding model 'SocioOrganizacion'
        db.create_table(u'encuesta_socioorganizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['SocioOrganizacion'])

        # Adding model 'Beneficios'
        db.create_table(u'encuesta_beneficios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['Beneficios'])

        # Adding model 'CreditoE'
        db.create_table(u'encuesta_creditoe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['CreditoE'])

        # Adding model 'DeQuien'
        db.create_table(u'encuesta_dequien', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['DeQuien'])

        # Adding model 'QuienFinancia'
        db.create_table(u'encuesta_quienfinancia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desde', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['QuienFinancia'])

        # Adding M2M table for field socio on 'QuienFinancia'
        db.create_table(u'encuesta_quienfinancia_socio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quienfinancia', models.ForeignKey(orm[u'encuesta.quienfinancia'], null=False)),
            ('socioorganizacion', models.ForeignKey(orm[u'encuesta.socioorganizacion'], null=False))
        ))
        db.create_unique(u'encuesta_quienfinancia_socio', ['quienfinancia_id', 'socioorganizacion_id'])

        # Adding M2M table for field beneficio_ser_socio on 'QuienFinancia'
        db.create_table(u'encuesta_quienfinancia_beneficio_ser_socio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quienfinancia', models.ForeignKey(orm[u'encuesta.quienfinancia'], null=False)),
            ('beneficios', models.ForeignKey(orm[u'encuesta.beneficios'], null=False))
        ))
        db.create_unique(u'encuesta_quienfinancia_beneficio_ser_socio', ['quienfinancia_id', 'beneficios_id'])

        # Adding M2M table for field tiene_credito on 'QuienFinancia'
        db.create_table(u'encuesta_quienfinancia_tiene_credito', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quienfinancia', models.ForeignKey(orm[u'encuesta.quienfinancia'], null=False)),
            ('creditoe', models.ForeignKey(orm[u'encuesta.creditoe'], null=False))
        ))
        db.create_unique(u'encuesta_quienfinancia_tiene_credito', ['quienfinancia_id', 'creditoe_id'])

        # Adding M2M table for field de_quien on 'QuienFinancia'
        db.create_table(u'encuesta_quienfinancia_de_quien', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quienfinancia', models.ForeignKey(orm[u'encuesta.quienfinancia'], null=False)),
            ('dequien', models.ForeignKey(orm[u'encuesta.dequien'], null=False))
        ))
        db.create_unique(u'encuesta_quienfinancia_de_quien', ['quienfinancia_id', 'dequien_id'])

        # Adding model 'ViveFamilia'
        db.create_table(u'encuesta_vivefamilia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['ViveFamilia'])

        # Adding model 'Composicion'
        db.create_table(u'encuesta_composicion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('adultos', self.gf('django.db.models.fields.IntegerField')()),
            ('adultas', self.gf('django.db.models.fields.IntegerField')()),
            ('jovenes_varones', self.gf('django.db.models.fields.IntegerField')()),
            ('jovenes_mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('ninos', self.gf('django.db.models.fields.IntegerField')()),
            ('ninas', self.gf('django.db.models.fields.IntegerField')()),
            ('permanente_hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('permanente_mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('temporales_hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('temporales_mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('tecnico_hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('tecnico_mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('relacion_finca_vivienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.ViveFamilia'])),
            ('educacion_dueno', self.gf('django.db.models.fields.IntegerField')()),
            ('educacion_maxima_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('educacion_maxima_mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Composicion'])

        # Adding model 'EnergiaFinca'
        db.create_table(u'encuesta_energiafinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['EnergiaFinca'])

        # Adding model 'Combustible'
        db.create_table(u'encuesta_combustible', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['Combustible'])

        # Adding model 'AguaFinca'
        db.create_table(u'encuesta_aguafinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['AguaFinca'])

        # Adding model 'ServiciosBasicos'
        db.create_table(u'encuesta_serviciosbasicos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['ServiciosBasicos'])

        # Adding M2M table for field electricidad on 'ServiciosBasicos'
        db.create_table(u'encuesta_serviciosbasicos_electricidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serviciosbasicos', models.ForeignKey(orm[u'encuesta.serviciosbasicos'], null=False)),
            ('energiafinca', models.ForeignKey(orm[u'encuesta.energiafinca'], null=False))
        ))
        db.create_unique(u'encuesta_serviciosbasicos_electricidad', ['serviciosbasicos_id', 'energiafinca_id'])

        # Adding M2M table for field combustible on 'ServiciosBasicos'
        db.create_table(u'encuesta_serviciosbasicos_combustible', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serviciosbasicos', models.ForeignKey(orm[u'encuesta.serviciosbasicos'], null=False)),
            ('combustible', models.ForeignKey(orm[u'encuesta.combustible'], null=False))
        ))
        db.create_unique(u'encuesta_serviciosbasicos_combustible', ['serviciosbasicos_id', 'combustible_id'])

        # Adding M2M table for field agua_trabajo_finca on 'ServiciosBasicos'
        db.create_table(u'encuesta_serviciosbasicos_agua_trabajo_finca', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serviciosbasicos', models.ForeignKey(orm[u'encuesta.serviciosbasicos'], null=False)),
            ('aguafinca', models.ForeignKey(orm[u'encuesta.aguafinca'], null=False))
        ))
        db.create_unique(u'encuesta_serviciosbasicos_agua_trabajo_finca', ['serviciosbasicos_id', 'aguafinca_id'])

        # Adding M2M table for field agua_consumo_humano on 'ServiciosBasicos'
        db.create_table(u'encuesta_serviciosbasicos_agua_consumo_humano', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serviciosbasicos', models.ForeignKey(orm[u'encuesta.serviciosbasicos'], null=False)),
            ('aguafinca', models.ForeignKey(orm[u'encuesta.aguafinca'], null=False))
        ))
        db.create_unique(u'encuesta_serviciosbasicos_agua_consumo_humano', ['serviciosbasicos_id', 'aguafinca_id'])

        # Adding model 'Tenecia'
        db.create_table(u'encuesta_tenecia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('documento', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Tenecia'])

        # Adding model 'NecesidadAlimento'
        db.create_table(u'encuesta_necesidadalimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['NecesidadAlimento'])

        # Adding model 'Meses'
        db.create_table(u'encuesta_meses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['Meses'])

        # Adding model 'TiemposCrisis'
        db.create_table(u'encuesta_tiemposcrisis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'encuesta', ['TiemposCrisis'])

        # Adding model 'Seguridad'
        db.create_table(u'encuesta_seguridad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compra_alimento', self.gf('django.db.models.fields.IntegerField')()),
            ('cubrir_necesidades', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal(u'encuesta', ['Seguridad'])

        # Adding M2M table for field porque_no_cubre on 'Seguridad'
        db.create_table(u'encuesta_seguridad_porque_no_cubre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seguridad', models.ForeignKey(orm[u'encuesta.seguridad'], null=False)),
            ('necesidadalimento', models.ForeignKey(orm[u'encuesta.necesidadalimento'], null=False))
        ))
        db.create_unique(u'encuesta_seguridad_porque_no_cubre', ['seguridad_id', 'necesidadalimento_id'])

        # Adding M2M table for field meses_dificiles on 'Seguridad'
        db.create_table(u'encuesta_seguridad_meses_dificiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seguridad', models.ForeignKey(orm[u'encuesta.seguridad'], null=False)),
            ('meses', models.ForeignKey(orm[u'encuesta.meses'], null=False))
        ))
        db.create_unique(u'encuesta_seguridad_meses_dificiles', ['seguridad_id', 'meses_id'])

        # Adding M2M table for field soluciones_crisis on 'Seguridad'
        db.create_table(u'encuesta_seguridad_soluciones_crisis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seguridad', models.ForeignKey(orm[u'encuesta.seguridad'], null=False)),
            ('tiemposcrisis', models.ForeignKey(orm[u'encuesta.tiemposcrisis'], null=False))
        ))
        db.create_unique(u'encuesta_seguridad_soluciones_crisis', ['seguridad_id', 'tiemposcrisis_id'])


    def backwards(self, orm):
        # Deleting model 'Entrevistado'
        db.delete_table(u'encuesta_entrevistado')

        # Deleting model 'DuenoFinca'
        db.delete_table(u'encuesta_duenofinca')

        # Deleting model 'Organizacion'
        db.delete_table(u'encuesta_organizacion')

        # Deleting model 'Recolector'
        db.delete_table(u'encuesta_recolector')

        # Deleting model 'Encuesta'
        db.delete_table(u'encuesta_encuesta')

        # Deleting model 'SocioOrganizacion'
        db.delete_table(u'encuesta_socioorganizacion')

        # Deleting model 'Beneficios'
        db.delete_table(u'encuesta_beneficios')

        # Deleting model 'CreditoE'
        db.delete_table(u'encuesta_creditoe')

        # Deleting model 'DeQuien'
        db.delete_table(u'encuesta_dequien')

        # Deleting model 'QuienFinancia'
        db.delete_table(u'encuesta_quienfinancia')

        # Removing M2M table for field socio on 'QuienFinancia'
        db.delete_table('encuesta_quienfinancia_socio')

        # Removing M2M table for field beneficio_ser_socio on 'QuienFinancia'
        db.delete_table('encuesta_quienfinancia_beneficio_ser_socio')

        # Removing M2M table for field tiene_credito on 'QuienFinancia'
        db.delete_table('encuesta_quienfinancia_tiene_credito')

        # Removing M2M table for field de_quien on 'QuienFinancia'
        db.delete_table('encuesta_quienfinancia_de_quien')

        # Deleting model 'ViveFamilia'
        db.delete_table(u'encuesta_vivefamilia')

        # Deleting model 'Composicion'
        db.delete_table(u'encuesta_composicion')

        # Deleting model 'EnergiaFinca'
        db.delete_table(u'encuesta_energiafinca')

        # Deleting model 'Combustible'
        db.delete_table(u'encuesta_combustible')

        # Deleting model 'AguaFinca'
        db.delete_table(u'encuesta_aguafinca')

        # Deleting model 'ServiciosBasicos'
        db.delete_table(u'encuesta_serviciosbasicos')

        # Removing M2M table for field electricidad on 'ServiciosBasicos'
        db.delete_table('encuesta_serviciosbasicos_electricidad')

        # Removing M2M table for field combustible on 'ServiciosBasicos'
        db.delete_table('encuesta_serviciosbasicos_combustible')

        # Removing M2M table for field agua_trabajo_finca on 'ServiciosBasicos'
        db.delete_table('encuesta_serviciosbasicos_agua_trabajo_finca')

        # Removing M2M table for field agua_consumo_humano on 'ServiciosBasicos'
        db.delete_table('encuesta_serviciosbasicos_agua_consumo_humano')

        # Deleting model 'Tenecia'
        db.delete_table(u'encuesta_tenecia')

        # Deleting model 'NecesidadAlimento'
        db.delete_table(u'encuesta_necesidadalimento')

        # Deleting model 'Meses'
        db.delete_table(u'encuesta_meses')

        # Deleting model 'TiemposCrisis'
        db.delete_table(u'encuesta_tiemposcrisis')

        # Deleting model 'Seguridad'
        db.delete_table(u'encuesta_seguridad')

        # Removing M2M table for field porque_no_cubre on 'Seguridad'
        db.delete_table('encuesta_seguridad_porque_no_cubre')

        # Removing M2M table for field meses_dificiles on 'Seguridad'
        db.delete_table('encuesta_seguridad_meses_dificiles')

        # Removing M2M table for field soluciones_crisis on 'Seguridad'
        db.delete_table('encuesta_seguridad_soluciones_crisis')


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
            'adultas': ('django.db.models.fields.IntegerField', [], {}),
            'adultos': ('django.db.models.fields.IntegerField', [], {}),
            'educacion_dueno': ('django.db.models.fields.IntegerField', [], {}),
            'educacion_maxima_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'educacion_maxima_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'jovenes_varones': ('django.db.models.fields.IntegerField', [], {}),
            'ninas': ('django.db.models.fields.IntegerField', [], {}),
            'ninos': ('django.db.models.fields.IntegerField', [], {}),
            'permanente_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'permanente_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'relacion_finca_vivienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.ViveFamilia']"}),
            'tecnico_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'tecnico_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'temporales_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'temporales_mujeres': ('django.db.models.fields.IntegerField', [], {})
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
        u'encuesta.energiafinca': {
            'Meta': {'object_name': 'EnergiaFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'beneficio_ser_socio': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'beneficiario_socio'", 'symmetrical': 'False', 'to': u"orm['encuesta.Beneficios']"}),
            'de_quien': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'quien'", 'symmetrical': 'False', 'to': u"orm['encuesta.DeQuien']"}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'socios'", 'symmetrical': 'False', 'to': u"orm['encuesta.SocioOrganizacion']"}),
            'tiene_credito': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'credito'", 'symmetrical': 'False', 'to': u"orm['encuesta.CreditoE']"})
        },
        u'encuesta.recolector': {
            'Meta': {'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'encuesta.seguridad': {
            'Meta': {'object_name': 'Seguridad'},
            'compra_alimento': ('django.db.models.fields.IntegerField', [], {}),
            'cubrir_necesidades': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['encuesta.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses_dificiles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dificiles'", 'symmetrical': 'False', 'to': u"orm['encuesta.Meses']"}),
            'porque_no_cubre': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cubre'", 'symmetrical': 'False', 'to': u"orm['encuesta.NecesidadAlimento']"}),
            'soluciones_crisis': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'crisis'", 'symmetrical': 'False', 'to': u"orm['encuesta.TiemposCrisis']"})
        },
        u'encuesta.serviciosbasicos': {
            'Meta': {'object_name': 'ServiciosBasicos'},
            'agua_consumo_humano': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'consumo'", 'symmetrical': 'False', 'to': u"orm['encuesta.AguaFinca']"}),
            'agua_trabajo_finca': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trabaja'", 'symmetrical': 'False', 'to': u"orm['encuesta.AguaFinca']"}),
            'combustible': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'combustible'", 'symmetrical': 'False', 'to': u"orm['encuesta.Combustible']"}),
            'electricidad': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'electricidad'", 'symmetrical': 'False', 'to': u"orm['encuesta.EnergiaFinca']"}),
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