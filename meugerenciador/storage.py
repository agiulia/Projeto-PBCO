import os
import json

c = 'C:/meugerenciador/data/usuarios.json'
def ler_usuario():
    if not os.path.exists(c):
        return []
    try:
        with open(c, 'r', encoding = 'utf-8') as arq:
            dados = json.load(arq)
    except json.JSONDecodeError:
        dados = []
    return dados

def gravar_usuario(x):
    os.makedirs(os.path.dirname(c), exist_ok = True)

    lista_usuarios = ler_usuario()
    lista_usuarios.append(x)
    
    with open(c, 'w', encoding = 'utf-8') as arq:
        json.dump(lista_usuarios, arq, indent = 4, ensure_ascii = False)

def gravar_usuarios(lista):
    os.makedirs(os.path.dirname(c), exist_ok=True)
    with open(c, 'w', encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4, ensure_ascii=False)