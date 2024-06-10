from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','apresentacao','objetivos','competencias')
    search_fields = ('nome',)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre','ects','area_cientifica')
    ordering = ('ano', 'semestre','ects',)
    search_fields = ('nome', 'area_cientifica','ano','semestre')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'descricao','conceitos_aplicados','tecnologias_utilizadas','imagem_preview','video_link','github_link')
    search_fields = ('disciplina',)

    def imagem_preview(self, obj):
        if obj.imagem:
            return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.imagem.url))
        return "-"
    imagem_preview.short_description = 'Imagem Preview'

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)