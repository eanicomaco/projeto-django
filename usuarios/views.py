from django.shortcuts import render, redirect
from django.contrib.auth.models import User #dá acesso a tabela de usuário do django
from django.contrib.auth import authenticate
from django.contrib import messages, auth

def login(request):
    form = request.POST

    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        usuario = auth.authenticate(username=login, password=senha)

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Usuário logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Falha ao autenticar o usuário!')
            return redirect('login')

    else:
        messages.error(request, 'Operação ilegal')
        return render(request, 'usuarios/login.html',{'form':form})

def cadastro(request):
    form = request.POST
    #outra forma de capturar os dados seria nome=form.get('nome)

    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']

        if senha1 != senha2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'O nome de usuário informado já está em uso.')
            return redirect('cadastro')

        user = User.objects.create_user(username=usuario,email=email,password=senha1)

        user = authenticate(username=usuario, password=senha1)

        if user is not None:
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Falha ao autenticar o usuário!')
            return redirect('cadastro')
    else:
        return render(request, 'usuarios/cadastro.html', {'form':form})
