from django import forms
from .models import Cliente, Projeto, Tarefa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'cliente', 'data_inicio', 'data_fim', 'status']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'projeto', 'data_conclusao', 'concluida']
