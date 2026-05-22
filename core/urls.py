from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('lendo/', views.livros_por_status, {"status": "lendo"}, name='lendo'),
    path('lidos/', views.livros_por_status, {"status": "lidos"}, name='lidos'),
    path('pretendo-ler/', views.livros_por_status, {"status": "pretendo-ler"}, name='pretendo_ler'),
    path('livros/<int:livro_id>/', views.detalhe_livro, name='detalhe_livro'),
    path('livros/<int:livro_id>/atualizar/', views.atualizar_livro, name='atualizar_livro'),
]
