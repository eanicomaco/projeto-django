import unicodedata
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def sanitiza_info(info):
    # Remover caracteres especiais e acentos
    info_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', info) if unicodedata.category(c) != 'Mn')
    # Substituir espaços por underscores
    info_sem_acentos = info_sem_acentos.replace(' ', '_')
    # Converter para minúsculas
    info_sanitizado = info_sem_acentos.lower()
    return info_sanitizado

def validar_username(username):
    errors = []
    if ' ' in username or not username.isalnum():
        errors.append('O nome de usuário não pode conter espaços ou carácteres especiais.')
    return errors

def validar_senha(senha1, senha2):
    errors = []
    if senha1 != senha2:
        errors.append('As senhas não conferem.')
    return errors

def validar_username_em_uso(username):
    errors = []
    if User.objects.filter(username=username).exists():
        errors.append('O nome de usuário já está em uso.')
    return errors

def validar_email(email):
    errors = []
    try:
        EmailValidator(email)
    except ValidationError as e:
        errors.append(str(e))
    return errors
