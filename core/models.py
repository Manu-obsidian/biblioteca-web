from django.db import models


class Livro(models.Model):
    STATUS_CHOICES = [
        ("quero_ler", "Quero ler"),
        ("lendo", "Lendo"),
        ("lido", "Lido"),
        ("pausado", "Pausado"),
    ]
    FORMATO_CHOICES = [
        ("livro", "Livro"),
        ("manga", "Manga"),
        ("light_novel", "Light novel"),
        ("manhwa", "Manhwa"),
        ("manhua", "Manhua"),
        ("hq", "HQ"),
        ("outro", "Outro"),
    ]

    titulo = models.CharField(max_length=200)
    capa = models.ImageField(upload_to="capas/", null=True, blank=True)
    ano = models.PositiveIntegerField(null=True, blank=True)
    genero = models.CharField(max_length=100, blank=True)
    autor = models.CharField(max_length=160)
    formato = models.CharField(max_length=30, choices=FORMATO_CHOICES, default="livro")
    total_paginas = models.PositiveIntegerField(null=True, blank=True)
    pagina_atual = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="quero_ler")
    favorito = models.BooleanField(default=False)
    nota = models.PositiveSmallIntegerField(null=True, blank=True)
    sinopse = models.TextField(blank=True)
    resenha = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    @property
    def progresso_percentual(self):
        if not self.total_paginas:
            return 0

        return min(round((self.pagina_atual / self.total_paginas) * 100), 100)
