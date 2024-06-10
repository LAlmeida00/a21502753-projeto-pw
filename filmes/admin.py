from django.contrib import admin
from .models import Filme, Ator, Genero

# Register your models here.

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Filme, FilmeAdmin)
admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)