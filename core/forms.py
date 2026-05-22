from django import forms

from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "capa", "ano", "genero", "autor", "formato", "total_paginas", "sinopse"]
        labels = {
            "titulo": "Título",
            "capa": "Capa",
            "ano": "Ano",
            "genero": "Gênero",
            "autor": "Autor",
            "formato": "Formato",
            "total_paginas": "Total de páginas",
            "sinopse": "Sinopse",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ex: Jogos Vorazes"}),
            "ano": forms.NumberInput(attrs={"placeholder": "Ex: 2008", "min": 0}),
            "genero": forms.TextInput(attrs={"placeholder": "Ex: Distopia, fantasia, romance"}),
            "autor": forms.TextInput(attrs={"placeholder": "Ex: Suzanne Collins"}),
            "total_paginas": forms.NumberInput(attrs={"placeholder": "Ex: 374", "min": 1}),
            "sinopse": forms.Textarea(attrs={"rows": 4, "placeholder": "Resumo da história"}),
        }
