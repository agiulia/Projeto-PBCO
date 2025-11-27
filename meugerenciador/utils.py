import storage as s
from datetime import datetime
import re

def validar_uid(x, lista):
    if any(u.get('id') == x for u in lista):
        return False
    return True

def validar_nome(nome):
    if not nome or len(nome) < 3:
        return False
    return True

def validar_email(email, lista_usuarios):
    if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email) or any(u.get('email') == email for u in lista_usuarios):
        return False
    return True

def validar_perfil(opcao):
    perfis = {"1": "Admin", "2": "User", "3": ""}
    return perfis.get(opcao)

def validar_lista(lista_usuarios):
    return len(lista_usuarios) > 0

def validar_confirmacao(valor):
    if valor in ("SIM", "NÃO"):
        return valor
    return None

def validar_data(data_texto):
    try:
        return datetime.strptime(data_texto, '%d/%m/%Y').date()
    except:
        return None
