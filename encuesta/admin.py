from django.contrib import admin
from .models import *
from produccion_finca.models import *
from produccion_cafe_finca.models import *
from vulnerabilidades_finca.models import *
from roya.models import *

class QuienFinanciaInline(admin.TabularInline):
    model = QuienFinancia
    extra = 1
    max_num = 1

class ComposicioInline(admin.TabularInline):
    model = Composicion
    extra = 1
    max_num = 1

class ServiciosBasicosInline(admin.TabularInline):
    model = ServiciosBasicos
    extra = 1
    max_num = 1

class TeneciaInline(admin.TabularInline):
    model = Tenecia
    extra = 1
    max_num = 1

class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    max_num = 1

class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = 8

class ReforestacionInline(admin.TabularInline):
    model = Reforestacion
    extra = 1
    max_num = 10

class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    max_num = 14

class ProductoFincaInline(admin.TabularInline):
    model = ProductoFinca
    extra = 1
    max_num = None

class ProductoPatioInline(admin.TabularInline):
    model = ProductoPatio
    extra = 1
    max_num = None

class IngresoFamiliarInline(admin.TabularInline):
    model = IngresoFamiliar
    extra = 1
    max_num = None

class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    max_num = None

class AreaCafeInline(admin.TabularInline):
    model = AreaCafe
    extra = 1
    max_num = None

class VariedadEdadRoyaInline(admin.TabularInline):
    model = VariedadEdadRoya
    fields = ('nombre_plantio','area','edad','variedades','produccion_2014','nivel_roya')
    extra = 1
    max_num = None

class ProduccionViveroInline(admin.StackedInline):
    model = ProduccionVivero
    extra = 1
    max_num = 1

class ManejoCafetalesInline(admin.TabularInline):
    model = ManejoCafetales
    extra = 1
    max_num = None

class ManejoTejidosInline(admin.TabularInline):
    model = ManejoTejidos
    extra = 1
    max_num = 1

class MesesManejoCafeInline(admin.TabularInline):
    model = MesesManejoCafe
    extra = 1
    max_num = 1

class UsoInsumosInline(admin.TabularInline):
    model = UsoInsumos
    extra = 1
    max_num = None

class UsoOpcionesAgroecologicaInline(admin.TabularInline):
    model = UsoOpcionesAgroecologica
    extra = 1
    max_num = None

class BeneficiadoInline(admin.StackedInline):
    model = Beneficiado
    extra = 1
    max_num = 1

class ComercializacionInline(admin.TabularInline):
    model = Comercializacion
    extra = 1
    max_num = None

class CreditoInline(admin.TabularInline):
    model = Credito
    fields = ('fecha','monto','credito_mediano','credito_largo','facilidad')
    extra = 1
    max_num = None

class ElClimaInline(admin.TabularInline):
    model = ElClima
    extra = 1
    max_num = None

class SueloFertilidadInline(admin.StackedInline):
    model = SueloFertilidad
    extra = 1
    max_num = 1

class LasPlagasInline(admin.StackedInline):
    model = LasPlagas
    extra = 1
    max_num = 3

class OtroRiesgosInline(admin.TabularInline):
    model = OtroRiesgos
    extra = 1
    max_num = None

class MitigacionInline(admin.StackedInline):
    model = Mitigacion
    extra = 1
    max_num = 1

class ImpactoRoyaInline(admin.TabularInline):
    model = ImpactoRoya
    extra = 1
    max_num = None

class PodaCafetosInline(admin.TabularInline):
    model = PodaCafetos
    extra = 1
    max_num = 1

class RecepoCafetosInline(admin.TabularInline):
    model = RecepoCafetos
    extra = 1
    max_num = 1

class RenovacionCafetalesInline(admin.TabularInline):
    model = RenovacionCafetales
    extra = 1
    max_num = 1

class ManejoSombraInline(admin.TabularInline):
    model = ManejoSombra
    extra = 1
    max_num = 1

class ManejoFertilizacionInline(admin.TabularInline):
    model = ManejoFertilizacion
    extra = 1
    max_num = 1

class AplicacionFungicidaInline(admin.TabularInline):
    model = AplicacionFungicida
    extra = 1
    max_num = 1

class OrientoInline(admin.TabularInline):
    model = Oriento
    extra = 1
    max_num = 1

class NuevosProductosInline(admin.TabularInline):
    model = NuevosProductos
    extra = 1
    max_num = None

# class AdelantePodaCafetosInline(admin.TabularInline):
#     model = AdelantePodaCafetos
#     extra = 1
#     max_num = 1

# class AdelanteRecepoCafetosInline(admin.TabularInline):
#     model = AdelanteRecepoCafetos
#     extra = 1
#     max_num = 1

# class AdelanteRenovacionCafetalesInline(admin.TabularInline):
#     model = AdelanteRenovacionCafetales
#     extra = 1
#     max_num = 1

# class AdelanteManejoSombraInline(admin.TabularInline):
#     model = AdelanteManejoSombra
#     extra = 1
#     max_num = 1

# class AdelanteManejoFertilizacionInline(admin.TabularInline):
#     model = AdelanteManejoFertilizacion
#     extra = 1
#     max_num = 1

# class AdelanteAplicacionFungicidaInline(admin.TabularInline):
#     model = AdelanteAplicacionFungicida
#     extra = 1
#     max_num = 1

class NivelFincaInline(admin.TabularInline):
    model = NivelFinca
    extra = 1
    max_num = 1

class CapacitacionesTecnicasInline(admin.TabularInline):
    model = CapacitacionesTecnicas
    extra = 1
    max_num = None

class CapacitacionesSocialesInline(admin.TabularInline):
    model = CapacitacionesSociales
    extra = 1
    max_num = None

class SiLeGustaInline(admin.TabularInline):
    model = SiLeGusta
    extra = 1
    max_num = 1

class NoLeGustaInline(admin.TabularInline):
    model = NoLeGusta
    extra = 1
    max_num = 1

class DetalleIncidenciaRoyaInline(admin.TabularInline):
    model = DetalleIncidenciaRoya
    extra = 1
    max_num = None

class FotosInline(admin.TabularInline):
    model = Fotos
    extra = 1
    max_num = None

class EncuestaAdmin(admin.ModelAdmin):
    inlines = [QuienFinanciaInline,ComposicioInline,ServiciosBasicosInline,TeneciaInline,SeguridadInline,
                    UsoTierraInline,ReforestacionInline,
                    AreaCafeInline,VariedadEdadRoyaInline,
                    ProduccionViveroInline,ManejoCafetalesInline,ManejoTejidosInline,MesesManejoCafeInline,UsoInsumosInline,
                    UsoOpcionesAgroecologicaInline,BeneficiadoInline,ComercializacionInline,CreditoInline,
                    ElClimaInline,SueloFertilidadInline,LasPlagasInline,OtroRiesgosInline,MitigacionInline,
                    ImpactoRoyaInline,PodaCafetosInline,RecepoCafetosInline,RenovacionCafetalesInline,
                    ManejoSombraInline,ManejoFertilizacionInline,AplicacionFungicidaInline,OrientoInline,
                    NuevosProductosInline,
                    NivelFincaInline,CapacitacionesTecnicasInline,
                    CapacitacionesSocialesInline,SiLeGustaInline,NoLeGustaInline,DetalleIncidenciaRoyaInline,
                    FotosInline]

    list_display = ('nombre','altitud','dueno','sexo')
    list_filter = ['pais', 'departamento','beneficiarios','composicion__educacion_dueno',
                        'produccionvivero__variedad_predomindante','quienfinancia__tiene_credito']
    search_fields = ['nombre']
    date_hierarchy = 'fecha'

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Recolector)
admin.site.register(Entrevistado)
admin.site.register(DuenoFinca)
admin.site.register(Organizacion)
#1.2
admin.site.register(SocioOrganizacion)
admin.site.register(Beneficios)
admin.site.register(CreditoE)
admin.site.register(DeQuien)
#1.3
admin.site.register(ViveFamilia)
#1.4
admin.site.register(EnergiaFinca)
admin.site.register(Combustible)
admin.site.register(AguaFinca)
#1.5
#admin.site.register(Tenecia)
#1.6
admin.site.register(NecesidadAlimento)
admin.site.register(Meses)
admin.site.register(TiemposCrisis)