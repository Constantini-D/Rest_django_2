from django.contrib import admin
from .models import Sorvete


@admin.register(Sorvete)
class SorveteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
