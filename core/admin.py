from django.contrib import admin

from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "status", "nota")
    list_filter = ("status",)
    search_fields = ("titulo", "autor")
