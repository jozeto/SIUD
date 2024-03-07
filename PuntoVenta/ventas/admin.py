from django.contrib import admin
from ventas.models import *


# Register your models here.
"""
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cod_cliente', 'cupo_credito')
    search_fields = ['cod_empleado']
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)
"""

admin.site.register(Novedadproducto)
admin.site.register(Persona)
admin.site.register(Empleado)
admin.site.register(Cliente)