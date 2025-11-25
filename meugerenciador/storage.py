import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

c1 = DATA_DIR / "usuarios.json"
c2 = DATA_DIR / "projetos.json"
c3 = DATA_DIR / "tarefas.json"

def ler_usuarios():
    if not os.path.exists(c1):
        return []
    try:
        with open(c1, 'r', encoding = 'utf-8') as arq:
            dados = json.load(arq)
    except json.JSONDecodeError:
        dados = []
    return dados

def gravar_usuarios(lista):
    os.makedirs(os.path.dirname(c1), exist_ok=True)
    with open(c1, 'w', encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4, ensure_ascii=False)

def ler_projetos():
    if not os.path.exists(c2):
        return []
    try:
        with open(c2, 'r', encoding = 'utf-8') as arq:
            dados = json.load(arq)
    except json.JSONDecodeError:
        dados = []
    return dados

def gravar_projetos(lista):
    os.makedirs(os.path.dirname(c2), exist_ok=True)
    with open(c2, 'w', encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4, ensure_ascii=False)