import storage as s
from datetime import datetime
import utils as u

def verificar_atraso(tarefa):
    prazo = u.validar_data(tarefa.get("prazo", ""))

    if prazo and prazo < datetime.now().date() and tarefa['status'] != "CONCLUÍDA":
        return True
    
    return False
    
def resumo_projetos():
    tarefas = s.ler_tarefas()
    resumo = {}

    for t in tarefas:
        projeto = t.get("projeto", "sem projeto")
        status = t.get("status", "desconhecido").lower()

        if projeto not in resumo:
            resumo[projeto] = {
                "total": 0,
                "status": {},
                "percentual_concluido": 0.0
            }

        resumo[projeto]["total"] += 1
        resumo[projeto]["status"][status] = resumo[projeto]["status"].get(status, 0) + 1

        return resumo

def produtividade_usuarios(data_inicial, data_final):
    tarefas = s.ler_tarefas()
    dt_inicio = u.validar_data(data_inicial)
    dt_fim = u.validar_data(data_final)

    if not dt_inicio or not dt_fim:
        return {}

    resultado = {}

    for t in tarefas.values():
        status = t.get("status", "").lower()
        if status not in ("concluída", "concluida"):
            continue

        data_conclusao = u.validar_data(t.get("data_conclusao", ""))
        if not data_conclusao:
            continue

        if dt_inicio <= data_conclusao <= dt_fim:
            usuario = t.get("responsavel", "Desconhecido")
            resultado[usuario] = resultado.get(usuario, 0) + 1

    return resultado
    
def tarefas_atrasadas():
    tarefas = s.ler_tarefas()
    return [t for t in tarefas if verificar_atraso(t)]