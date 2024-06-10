from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Banda, Album, Musica

# Register your models here.

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome','foto_preview','biografia','nacionalidade','ano_criacao')
    ordering = ('nome','nacionalidade','ano_criacao')
    search_fields = ('nome',)

    def foto_preview(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.foto.url))
    foto_preview.short_description = 'Foto Preview'

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome','capa_preview','ano')
    ordering = ('ano','nome')
    search_fields = ('nome','ano')

    def capa_preview(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.capa.url))
    capa_preview.short_description = 'Capa Preview'

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome','duracao_musica','letra','display_spotify_link')
    ordering = ( 'nome',)
    search_fields = ('nome',)

    def display_spotify_link(self, obj):
        return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=obj.spotify_link))
    display_spotify_link.short_description = 'Spotify Link'

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)
