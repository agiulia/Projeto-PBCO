import os
import json
from pathlib import Path
from datetime import datetime, date

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
        with open(c1, 'r', encoding='utf-8') as arq:
            return json.load(arq)
    except:
        return []

def gravar_usuarios(lista):
    os.makedirs(os.path.dirname(c1), exist_ok=True)
    with open(c1, 'w', encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4, ensure_ascii=False)

def ler_projetos():
    try:
        with open(c2, "r", encoding="utf-8") as arq:
            projetos_json = json.load(arq)
    except FileNotFoundError:
        return []

    projetos = []

    for p in projetos_json:
        projetos.append({
            "id": p["id"],
            "nome": p["nome"],
            "descricao": p["descricao"],
            "inicio": datetime.strptime(p["inicio"], "%d/%m/%Y").date() if "/" in p["inicio"] else datetime.strptime(p["inicio"], "%Y-%m-%d").date(),
            "fim": datetime.strptime(p["fim"], "%d/%m/%Y").date() if "/" in p["fim"] else datetime.strptime(p["fim"], "%Y-%m-%d").date()
        })

    return projetos

def gravar_projetos(projetos):
    projetos_json = []

    for proj in projetos:
        projetos_json.append({
            "id": proj["id"],
            "nome": proj["nome"],
            "descricao": proj["descricao"],
            "inicio": proj["inicio"].strftime("%Y-%m-%d") if isinstance(proj["inicio"], date) else proj["inicio"],
            "fim": proj["fim"].strftime("%Y-%m-%d") if isinstance(proj["fim"], date) else proj["fim"]
        })

    with open(c2, 'w', encoding='utf-8') as arq:
        json.dump(projetos_json, arq, indent=4, ensure_ascii=False)

def ler_tarefas():
    if not os.path.exists(c3):
        return {}
    try:
        with open(c3, 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            tarefas = {}
            for k, v in dados.items():
                try:
                    prazo = datetime.strptime(v.get("prazo", ""), "%Y-%m-%d").date()
                except:
                    prazo = None
                tarefas[k] = {
                    "id": v.get("id", k),
                    "projeto_id": v.get("projeto_id", "N/A"),  
                    "status": v.get("status", "pendente"),
                    "responsável_id": v.get("responsável", "N/A"),
                    "prazo": prazo
                }
            return tarefas
    except:
        return {}

def gravar_tarefas(tarefas):
    tarefas_json = {}
    for k, v in tarefas.items():
        tarefas_json[k] = {
            "id": v.get("id", k),
            "projeto_id": v.get("projeto_id", "N/A"),
            "status": v.get("status", "pendente"),
            "responsável": v.get("responsável", "N/A"),
            "prazo": v.get("prazo").strftime("%Y-%m-%d") if isinstance(v.get("prazo"), (datetime, date)) else str(v.get("prazo", ""))
        }
    with open(c3, 'w', encoding='utf-8') as arq:
        json.dump(tarefas_json, arq, indent=4, ensure_ascii=False)