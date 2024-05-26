from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.core.exceptions import ValidationError
from apps.utils.utils import validar_username, validar_senha, validar_username_em_uso, validar_email

def login(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=usuario, password=senha)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Olá {usuario}! Você logou com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Falha ao tentar logar no sistema')
            return redirect('login')

    else:
        return render(request, 'apps/usuarios/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('login')

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

        errors = []
        errors.extend(validar_username_em_uso(usuario))
        errors.extend(validar_username(usuario))
        errors.extend(validar_senha(senha1, senha2))
        errors.extend(validar_email(email))

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'apps/usuarios/cadastro.html', {'form':data})

        user = User.objects.create_user(username=usuario, email=email, password=senha1)

        if user:
            user = authenticate(username=usuario, password=senha1)
            if user is not None:
                messages.success(request, 'Usuário cadastrado com sucesso')
                return redirect('login')
            else:
                messages.error(request, 'Falha ao autenticar o usuário após o cadastro')
                return render(request, 'apps/usuarios/cadastro.html', {'form':data})
        else:
            messages.error(request, 'Falha ao cadastrar o usuário')
            return render(request, 'apps/usuarios/cadastro.html', {'form':data})

    else:
        return render(request, 'apps/usuarios/cadastro.html')
