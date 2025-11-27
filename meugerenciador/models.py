def novo_usuario(uid, nome, email, perfil):
    return {
        "id": uid,
        "nome": nome,
        "e-mail": email,
        "perfil": perfil
    }

def novo_projeto(uid, nome, descricao, inicio, fim):
    return {
        "id": uid,
        "nome": nome,
        "descricao": descricao,
        "inicio": inicio,
        "fim": fim
    }

def nova_tarefa(uid,titulo, projeto, responsavel, status, prazo):
    return {
        "id": uid,
        "titulo": titulo,
        "projeto": projeto,
        "responsavel": responsavel,
        "status": status,
        "prazo": prazo
    }