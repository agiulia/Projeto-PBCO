import storage as s
from datetime import datetime
import re

def validar_uid(x, lista_usuarios):
    if any(u.get('id') == x for u in lista_usuarios):
        return False
    return True

def validar_nome(nome):
    if not nome or len(nome) < 3:
        return False
    return True

def validar_email(email, lista_usuarios):
    if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email) or any(u.get('e-mail') == email for u in lista_usuarios):
        return False
    return True

def validar_perfil(opcao):
    return opcao in ("1", "2", "3")

def validar_lista(lista_usuarios):
        return bool(lista_usuarios)

def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, '%d/%m/%Y')
        return True
    except ValueError:
        return False