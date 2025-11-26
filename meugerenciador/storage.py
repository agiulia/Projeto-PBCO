import os
import json
from pathlib import Path
from datetime import datetime

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

def gravar_tarefas(tarefas):
    TAREFAS_json = {}
    for chave, valor in tarefas.items():
        TAREFAS_json[chave] = {
            "status": valor["status"],
            "responsável": valor["responsável"],
            "prazo": str(valor["prazo"])
        }
    with open(c3, "w", encoding="utf-8") as arq:
        json.dump(TAREFAS_json, arq, ensure_ascii=False, indent=4)

def ler_tarefas():
    try:
        with open(c3, "r") as arq:
            tarefas_json = json.load(arq)
            tarefas = {}
            for chave, valor in tarefas_json.items():
                tarefas[chave] = {
                    "status": valor["status"],
                    "responsável": valor["responsável"],
                    "prazo": datetime.strptime(valor["prazo"], "%Y-%m-%d").date()
                }
            return tarefas
    except FileNotFoundError:
        return {}