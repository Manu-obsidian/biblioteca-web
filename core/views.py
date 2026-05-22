from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LivroForm
from .models import Livro


STATUS_PAGES = {
    "lendo": ("Lendo", "Livros que você está lendo agora."),
    "lidos": ("Lidos", "Livros que você já terminou."),
    "pretendo-ler": ("Pretendo ler", "Livros guardados para ler depois."),
}


def _base_context(active_page="home"):
    livros = Livro.objects.all()

    return {
        "active_page": active_page,
        "total_livros": livros.count(),
        "livros_lidos": livros.filter(status="lido").count(),
        "lendo_agora": livros.filter(status="lendo").count(),
        "pretendo_ler": livros.filter(status="quero_ler").count(),
    }


def _search_livros(query):
    livros = Livro.objects.all()

    if query:
        livros = livros.filter(
            Q(titulo__icontains=query)
            | Q(autor__icontains=query)
            | Q(genero__icontains=query)
            | Q(sinopse__icontains=query)
            | Q(resenha__icontains=query)
        )

    return livros


def home(request):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LivroForm()

    query = request.GET.get("q", "").strip()
    livros = _search_livros(query)
    context = _base_context()
    context.update(
        {
            "form": form,
            "query": query,
            "titulo_pagina": "Início",
            "descricao_pagina": "Cadastre obras e acompanhe leitura, favoritos, notas e resenhas.",
            "livros": livros,
            "livros_lendo": Livro.objects.filter(status="lendo")[:6],
            "livros_recentes": Livro.objects.order_by("-criado_em")[:6],
            "mostrar_cadastro": True,
        }
    )
    return render(request, "home.html", context)


def favoritos(request):
    query = request.GET.get("q", "").strip()
    livros = _search_livros(query).filter(favorito=True)
    context = _base_context(active_page="favoritos")
    context.update(
        {
            "query": query,
            "titulo_pagina": "Favoritos",
            "descricao_pagina": "Obras marcadas como favoritas.",
            "livros": livros,
            "mostrar_cadastro": False,
        }
    )
    return render(request, "home.html", context)


def livros_por_status(request, status):
    status_map = {
        "lendo": "lendo",
        "lidos": "lido",
        "pretendo-ler": "quero_ler",
    }
    status_value = status_map[status]
    query = request.GET.get("q", "").strip()
    livros = _search_livros(query).filter(status=status_value)
    titulo, descricao = STATUS_PAGES[status]
    context = _base_context(active_page=status)
    context.update(
        {
            "query": query,
            "titulo_pagina": titulo,
            "descricao_pagina": descricao,
            "livros": livros,
            "mostrar_cadastro": False,
        }
    )
    return render(request, "home.html", context)


def detalhe_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "dados":
            form = LivroForm(request.POST, request.FILES, instance=livro)
            if form.is_valid():
                form.save()
                return redirect("detalhe_livro", livro_id=livro.id)

        elif action == "status":
            status = request.POST.get("status")
            if status in dict(Livro.STATUS_CHOICES):
                livro.status = status
                if status == "lido" and livro.total_paginas:
                    livro.pagina_atual = livro.total_paginas
                elif status == "quero_ler":
                    livro.pagina_atual = 0
                livro.save()
                return redirect("detalhe_livro", livro_id=livro.id)

        elif action == "favorito":
            livro.favorito = not livro.favorito
            livro.save()
            return redirect("detalhe_livro", livro_id=livro.id)

        elif action == "progresso":
            pagina_atual = request.POST.get("pagina_atual")
            if pagina_atual:
                pagina_atual = int(pagina_atual)
                if livro.total_paginas:
                    pagina_atual = min(pagina_atual, livro.total_paginas)
                livro.pagina_atual = max(pagina_atual, 0)
                livro.status = "lendo"
                livro.save()
            return redirect("detalhe_livro", livro_id=livro.id)

        elif action == "avaliacao" and livro.status == "lido":
            nota = request.POST.get("nota")
            livro.nota = int(nota) if nota else None
            livro.resenha = request.POST.get("resenha", "").strip()
            livro.save()
            return redirect("detalhe_livro", livro_id=livro.id)

        elif action == "apagar":
            livro.delete()
            return redirect("home")

    context = _base_context(active_page="")
    context.update(
        {
            "livro": livro,
            "form": LivroForm(instance=livro),
        }
    )
    return render(request, "book_detail.html", context)


def atualizar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "status":
            status = request.POST.get("status")
            if status in dict(Livro.STATUS_CHOICES):
                livro.status = status
                if status == "lido" and livro.total_paginas:
                    livro.pagina_atual = livro.total_paginas
                elif status == "quero_ler":
                    livro.pagina_atual = 0
                livro.save()

        elif action == "favorito":
            livro.favorito = not livro.favorito
            livro.save()

        elif action == "progresso":
            pagina_atual = request.POST.get("pagina_atual")
            if pagina_atual:
                pagina_atual = int(pagina_atual)
                if livro.total_paginas:
                    pagina_atual = min(pagina_atual, livro.total_paginas)
                livro.pagina_atual = max(pagina_atual, 0)
                livro.status = "lendo"
                livro.save()

        elif action == "avaliacao" and livro.status == "lido":
            nota = request.POST.get("nota")
            livro.nota = int(nota) if nota else None
            livro.resenha = request.POST.get("resenha", "").strip()
            livro.save()

    next_url = request.POST.get("next") or "home"
    return redirect(next_url)
