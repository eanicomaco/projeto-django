from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth

def login(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user is not None:
            login(request,user)
            messages.success(f'Olá {usuario}! Você logou com sucesso!')
            return redirect('index')
        else:
            messages.error('Falha ao tentar logar no sistema')
            return redirect('login')

    else:
        return render(request, 'usuarios/login.html')

def cadastro(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')

        data = {
            'usuario':usuario,
            'email':email,
        }

        if senha1 != senha2:
            messages.error(request, 'As senhas não conferem')
            return redirect('cadastro', {'form':data})

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Nome de usuário já está em uso')
            return redirect('cadastro', {'form':data})

        user = User.objects.create_user(username=usuario, email=email, password=senha1)

        if user:
            user = authenticate(username=usuario, password=senha1)
            if user is not None:
                messages.success(request, 'Usuário cadastrado com sucesso')
                return redirect('login')
            else:
                messages.error(request, 'Falha ao autenticar o usuário após o cadastro')
                return redirect('cadastro', {'form':data})
        else:
            messages.error(request, 'Falha ao cadastrar o usuário')
            return redirect('cadastro', {'form':data})

    else:
        messages.error(request, 'Operação ilegal')
        return render(request, 'usuarios/cadastro.html')
