from django.db import models


class Livro(models.Model):
    STATUS_CHOICES = [
        ("quero_ler", "Quero ler"),
        ("lendo", "Lendo"),
        ("lido", "Lido"),
        ("pausado", "Pausado"),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=160)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="quero_ler")
    nota = models.PositiveSmallIntegerField(null=True, blank=True)
    resenha = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
