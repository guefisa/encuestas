from django.contrib import admin
from django.utils.html import format_html

from .models import Pregunta, Opcion


# En la administración las opciones se muestran dentro de las preguntas
class OpcionInline(admin.TabularInline):
    model = Opcion
    fk_name = 'pregunta'
    extra = 1


class PreguntaAdmin(admin.ModelAdmin):
    fields = ('codigo', 'texto', 'opcion_seleccionada', 'salto', 'orden',)
    list_display = ('codigo', 'texto', 'opcion_seleccionada', 'salto', 'orden',)
    list_editable = ('opcion_seleccionada', 'salto', 'orden',)

    inlines = [OpcionInline]


admin.site.register(Pregunta, PreguntaAdmin)
