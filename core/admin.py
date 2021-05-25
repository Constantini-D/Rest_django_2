from django.contrib import admin
from .models import Sorvete, Avaliacao


@admin.register(Sorvete)
class SorveteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'nota', 'comentario')