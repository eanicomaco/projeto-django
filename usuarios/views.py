from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages, auth

def login(request):
    form = request.POST

    if request.method == 'POST':
        login = form.get('login')
        senha = form.get('senha')
        user = auth.authenticate(username=login, password=senha)

        if user is not None:
            auth.login(request,user)
            messages.success(f'Olá {login}! Você logou com sucesso!')
            return redirect('index')
        else:
            messages.error('Falha ao tentar logar no sistema')
            return redirect('login')

    else:
        return render(request, 'usuarios/login.html',{'form':form})

def cadastro(request):
    form = request.POST
    if request.method == 'POST':
        usuario = form.get('usuario')
        email = form.get('email')
        senha1 = form.get('senha1')
        senha2 = form.get('senha2')

        if senha1 != senha2:
            messages.error(request, 'As senhas não conferem')
            return redirect('cadastro')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Nome de usuário já está em uso')
            return redirect('cadastro')

        user = User.objects.create_user(username=usuario, email=email, password=senha1)
        user = authenticate(username=usuario, password=senha1)

        if user is not None:
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('login')
        else:
            messages.error(request, 'Falha ao cadastrar o usuário')
            return redirect('cadastro')

    else:
        return render(request, 'usuarios/cadastro.html')
