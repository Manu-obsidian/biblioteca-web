from django.shortcuts import render


from .models import Livro


def home(request):
    livros = Livro.objects.all()
    total_livros = livros.count()
    livros_lidos = livros.filter(status="lido").count()
    lendo_agora = livros.filter(status="lendo").count()

    return render(
        request,
        "home.html",
        {
            "livros": livros,
            "total_livros": total_livros,
            "livros_lidos": livros_lidos,
            "lendo_agora": lendo_agora,
        },
    )
