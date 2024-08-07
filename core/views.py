from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Projeto, Tarefa
from .forms import ClienteForm, ProjetoForm, TarefaForm

def home(request):
    return render(request, 'core/home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/cliente_form.html', {'form': form})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'core/cliente_confirm_delete.html', {'cliente': cliente})

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/lista_projetos.html', {'projetos': projetos})

def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'core/projeto_form.html', {'form': form})

def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'core/projeto_form.html', {'form': form})

def excluir_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('lista_projetos')
    return render(request, 'core/projeto_confirm_delete.html', {'projeto': projeto})

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'core/lista_tarefas.html', {'tarefas': tarefas})

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'core/tarefa_form.html', {'form': form})

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/tarefa_form.html', {'form': form})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'core/tarefa_confirm_delete.html', {'tarefa': tarefa})

