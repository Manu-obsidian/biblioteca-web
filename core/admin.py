from django.contrib import admin

from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "genero", "formato", "status", "favorito", "nota", "pagina_atual", "total_paginas")
    list_filter = ("status", "favorito", "formato", "genero")
    search_fields = ("titulo", "autor", "genero", "sinopse", "resenha")
