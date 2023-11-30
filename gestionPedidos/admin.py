from django.contrib import admin

# Register your models here.

from gestionPedidos.models import Clientes, Articulos, Pedidos


# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "tlfn")
    search_fields = ("nombre", "tlfn")


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('seccion', 'nombre')
    list_filter = ('seccion', 'nombre')


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
