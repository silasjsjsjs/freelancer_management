from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.novo_cliente, name='novo_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.novo_projeto, name='novo_projeto'),
    path('projetos/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/excluir/<int:id>/', views.excluir_projeto, name='excluir_projeto'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.nova_tarefa, name='nova_tarefa'),
    path('tarefas/editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
]
