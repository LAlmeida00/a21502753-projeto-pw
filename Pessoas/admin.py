from django.contrib import admin
from django.utils.html import format_html
from .models import Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome','idade')
    ordering = ('nome','idade')
    search_fields = ('nome','idade')


admin.site.register(Pessoa, PessoaAdmin)
