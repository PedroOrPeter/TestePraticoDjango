from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
import requests
import json

def list_clientes(request):
    clientes = Cliente.objects.all().order_by('nome', 'sobrenome')
    return render(request, 'clientes.html', {'clientes': clientes})

def create_cliente(request):
    r = 'http://gerador-nomes.herokuapp.com/nome/aleatorio'
    api = requests.get(r)
    api = api.json()
    nomes = ''

    for i in range(int(len(api))):
        nomes += api[i]
        nomes += ' '

    formulario = ClienteForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('list_clientes')

    context = {'api': nomes}
    return render(request, 'cadastroClientes.html', context)

def update_cliente(request, id):
    clientes = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, instance=clientes)

    if formulario.is_valid():
        formulario.save()
        return redirect('list_clientes')
    return render(request, 'clientesFormulario.html', {'formulario': formulario, 'clientes': clientes})

def delete_cliente(request, id):
    clientes = Cliente.objects.get(id=id)

    if request.method == 'POST':
        clientes.delete()
        return redirect('list_clientes')
    return render(request, 'deletarCliente.html', {'clientes': clientes})
