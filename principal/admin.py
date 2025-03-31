from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Elimina las referencias a 'fecha_inicio' y 'fecha_fin'
    search_fields = ('nombre', 'descripcion')  # Habilitar búsqueda por nombre y descripción
    list_filter = ('nombre',)  # Usa solo campos que están en tu modelo
    ordering = ('nombre',)  # Usa solo campos que están en tu modelo

