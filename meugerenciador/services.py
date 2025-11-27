import storage as s
import services as srv
import models as m
import utils as u
import time
from datetime import datetime

def inserir_usuario(uid, nome, email, perfil_opcao): 
    lista = s.ler_usuarios()

    if not u.validar_uid(uid, lista):
        return False, "\nID já está em uso.\n"

    if not u.validar_nome(nome):
        return False, "\nNome inválido (mínimo 3 caracteres).\n"

    if not u.validar_email(email, lista):
        return False, "\nE-mail inválido ou já registrado.\n"

    perfil = u.validar_perfil(perfil_opcao)
    if perfil is None:
        return False, "\nPerfil inválido.\n"

    usuario = m.novo_usuario(uid, nome, email, perfil)

    lista.append(usuario)
    s.gravar_usuarios(lista)

    return True, "\nUsuário inserido com sucesso!\n"

def listar_usuarios():
    lista_usuarios = s.ler_usuarios()

    if u.validar_lista(lista_usuarios):
        return False, "Não há usuários registrados no sistema."

    return True, lista_usuarios

def buscar_usuarios(email):
    lista_usuarios = s.ler_usuarios()

    if not u.validar_lista(lista_usuarios):
        return False, "Não há usuários registrados no sistema."

    usuario = next((item for item in lista_usuarios if item.get('e-mail') == email), None)

    if usuario is None:
        return False, "Usuário não encontrado."

    return True, usuario

def atualizar_usuarios(email, campo, novo_valor):
    lista = s.ler_usuarios()

    if not u.validar_lista(lista):
        return False, "Não há usuários registrados."

    usuario = next((x for x in lista if x.get("e-mail") == email), None)

    if not usuario:
        return False, "Usuário não encontrado."

    if campo == "id":
        if not u.validar_uid(novo_valor, lista):
            return False, "ID já existente."
        usuario["id"] = novo_valor

    elif campo == "nome":
        if not u.validar_nome(novo_valor):
            return False, "Nome inválido."
        usuario["nome"] = novo_valor

    elif campo == "email":
        if not u.validar_email(novo_valor, lista):
            return False, "E-mail inválido ou já existe."
        usuario["e-mail"] = novo_valor

    elif campo == "perfil":
        if not u.validar_perfil(novo_valor):
            return False, "Perfil inválido."
        usuario["perfil"] = novo_valor

    else:
        return False, "Campo inválido."

    s.gravar_usuarios(lista)
    return True, usuario

def remover_usuarios(email):
    lista_usuarios = s.ler_usuarios()
    novos_usuarios = [u for u in lista_usuarios if u.get('e-mail') != email]
    if len(novos_usuarios) == len(lista_usuarios):
        return False, f"Usuário com e-mail '{email}' não encontrado."
    else:
        s.gravar_usuarios(novos_usuarios)
        return True, "Usuário com e-mail '{email}' removido com sucesso!"

def limpar_usuarios(confirmacao):
    if confirmacao == "NÃO":
        return False, "Operação cancelada."
    if confirmacao == "SIM":
        s.gravar_usuarios([])
        return True, "Arquivo limpo com sucesso!"
    return False, "Confirmação inválida."

def inserir_projetos(lista):
    while True:
        id_projeto = input("\nDigite o ID do projeto: ").strip()
        if any(p['id'] == id_projeto for p in lista):
            print(">>> ERRO! ID já existe. Escolha outro.")
        elif id_projeto == "":
            print(">>> ERRO! ID não pode ser vazio.")
        else:
            break

    while True:
        nome = input("Digite o nome do projeto: ").strip()
        if nome == "":
            print(">>> ERRO! nome não pode ser vazio.")
        elif any(p['nome'].lower() == nome.lower() for p in lista):
            print(">>> ERRO! Nome do projeto já existe. Escolha outro.")
        else:
            break

    descricao = input("Faça uma leve descrição do projeto: ").strip()

    while True:
        inicio = input("Digite a data de início (DD/MM/AAAA): ").strip()
        try:
            inicio_dt = datetime.strptime(inicio, "%d/%m/%Y").date()
            break
        except ValueError:
            print(">>> ERRO! Formato inválido! Use DD/MM/AAAA")

    while True:
        try:
            fim_str = input("Digite a data de fim (DD/MM/AAAA): ").strip()
            fim = datetime.strptime(fim_str, "%d/%m/%Y").date()

            if fim < inicio_dt:
                print("Erro: A data de fim não pode ser ANTERIOR à data de início!")
                continue

            break
        except ValueError:
            print(">>>ERRO! Formato inválido! Use DD/MM/AAAA")

    inicio_formatado = inicio_dt.strftime("%d/%m/%Y")
    fim_formatado = fim.strftime("%d/%m/%Y")

    projeto = m.novo_projeto(id_projeto, nome, descricao, inicio_formatado, fim_formatado)
    lista.append(projeto)
    s.gravar_projetos(lista)
    print("Projeto inserido com sucesso!")

def listar_projetos(lista):
    if not lista:
        print("\n>>> ERRO! Não há projetos cadastrados.\n")
        return

    print("\n=== Lista de Projetos ===\n")
    print("-" * 30)
    for item in lista:
        print(f"ID: {item['id']}")
        print(f"Nome: {item['nome']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Data Início: {item['inicio']}")
        print(f"Data Fim: {item['fim']}\n")
        print("-" * 30)
    print()

def buscar_projetos(lista):
    while True:
        termo = input("Digite o nome ou ID do projeto: ").strip()
        if termo == "":
            print(">>> ERRO! Entrada vazia. Tente novamente.\n")
        else:
            break  

    encontrados = [
        p for p in lista
        if termo.lower() in p['nome'].lower() or termo == p['id']
    ]

    if not encontrados:
        print(">>> ERRO! Nenhum projeto encontrado com esse nome ou ID.\n")
        return

    for item in encontrados:
        print("\n=== Projeto Encontrado ===")
        print("-" * 30)
        print(f"ID: {item['id']}")
        print(f"Nome: {item['nome']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Data Início: {item['inicio']}")
        print(f"Data Fim: {item['fim']}\n")
        print("-" * 30)
    print()

def atualizar_projetos(lista):
    termo = input("Digite o ID do projeto que deseja atualizar: ").strip()
    projeto = next((p for p in lista if p['id'] == termo), None)

    if not projeto:
        print(">>>ERRO! Projeto não encontrado.\n")
        return

    print("O que deseja atualizar?")
    print("[1] Nome\n[2] Descrição\n[3] Data Início\n[4] Data Fim")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        while True:
            novo_nome = input("Digite o novo nome: ").strip()
            if any(p['nome'].lower() == novo_nome.lower() and p != projeto for p in lista):
                print(">>>ERRO! Nome já existe. Escolha outro.")
            elif (novo_nome == ""):
                print(">>> ERRO! Nome não pode ser vazio.")
            else:
                projeto['nome'] = novo_nome
                break
    elif opcao == "2":
        projeto['descricao'] = input("Digite a nova descrição: ").strip()
    elif opcao == "3":
        while True:
            nova_data = input("Digite a nova data de início (DD/MM/AAAA): ").strip()
            try:
                datetime.strptime(nova_data, "%d/%m/%Y")
                projeto['inicio'] = nova_data
                break
            except ValueError:
                print(">>>ERRO! Formato de data inválido!")
    elif opcao == "4":
        while True:
            nova_data = input("Digite a nova data de fim (DD/MM/AAAA): ").strip()
            try:
                datetime.strptime(nova_data, "%d/%m/%Y")
                projeto['fim'] = nova_data
                break
            except ValueError:
                print(">>> ERRO! Formato de data inválido!")
    else:
        print(">>> ERRO! Por favor, digite uma opção válida de 1 a 4 <<<\n")
        return

    s.gravar_projetos(lista)
    print("Projeto atualizado com sucesso!")

def remover_projetos(lista):
    termo = input("Digite o ID do projeto que deseja remover: ").strip()
    projeto = next((p for p in lista if p['id'] == termo), None)

    if not projeto:
        print("Projeto não encontrado!")
        return

    lista.remove(projeto)
    s.gravar_projetos(lista)
    print("Projeto removido com sucesso!\n")

def limpar_projetos(lista):
    confirm = input("Você quer remover todos os projetos permanentemente? (SIM/NÃO): ").strip().upper()
    if confirm == "SIM":
        lista.clear()
        s.gravar_projetos(lista)
        print("Todos os projetos foram removidos!")
    else:
        print("Ação cancelada!")


def VERIFICAR_ATRASO(tarefa):
    if tarefa['prazo'] < datetime.now().date() and tarefa['status'] != "CONCLUÍDA":
        return True
    else:
        return False

def inserir_tarefas(TAREFAS):
    while True:
        tarefa_id = input("\nDigite o ID da tarefa: ").strip()
        if any(t['id'] == tarefa_id for t in TAREFAS.values()):
            print("Erro: ID já existe. Escolha outro.")
        elif tarefa_id == "":
            print("Erro: ID não pode ser vazio.")
        else:
            break
    título_tarefa = input("Digite o título da tarefa que deseja adicionar: ").upper()
    while (título_tarefa == "" or título_tarefa in TAREFAS):
        if (título_tarefa in TAREFAS):
            título_tarefa = input("\n>>> ERRO! Tarefa já existente.\nDigite outro título para a tarefa: ").upper()
        else:
            título_tarefa = input("\n>>> ERRO! O nome está vazio.\nDigite algo válido para o título da tarefa: ").upper()
    projetos = s.ler_projetos()
    projeto_id = input("Digite o ID do projeto ao qual essa tarefa pertence: ")

    if not any(p['id'] == projeto_id for p in projetos):
        print(">> ERRO! Projeto não encontrado! Não é possível adicionar a tarefa.\n")
        return False
    
    status_tarefa = input(f"Informe os status da tarefa (Pendente, Em andamento ou Concluída): ").upper()
    while (status_tarefa != "PENDENTE" and status_tarefa != "EM ANDAMENTO" and status_tarefa != "CONCLUÍDA" and status_tarefa != "CONCLUIDA"):
        status_tarefa = input(f">>> ERRO! Tente novamente.\nInforme os status da tarefa novamente com 'Pendente', 'Em andamento' ou 'Concluída': ").upper()
    if (status_tarefa == "EM ANDAMENTO"):
        status_tarefa = "Em andamento"
    elif (status_tarefa == "PENDENTE"):
        status_tarefa = "Pendente"
    else:
        status_tarefa = "Concluída"
    while True:
        responsável_id = input("Digite o ID do responsável pela tarefa: ")
        if responsável_id == "":
            print(">>> ERRO! ID do responsável não pode ser vazio.")

        elif not (any(u['id'] == responsável_id for u in s.ler_usuarios())):
            print(">>> ERRO! Responsável não encontrado. Tente novamente.")
        
        else:
            break
    prazo_texto = input("Digite o prazo dessa tarefa no formato DD/MM/AAAA: ")
    while True:
        try:
            prazo_tarefa = datetime.strptime(prazo_texto, "%d/%m/%Y").date()
            break
        except ValueError:
            print(">>> Data inválida! Tente novamente.\n")
            prazo_texto = input("Digite o prazo dessa tarefa no formato DD/MM/AAAA: ")
    TAREFAS[título_tarefa] = {
        "id": tarefa_id,
        "projeto_id": projeto_id,
        "status": status_tarefa,
        "responsável_id": responsável_id,
        "prazo": prazo_tarefa
    }
    s.gravar_tarefas(TAREFAS)
    print("Tarefa salva.\n")

def listar_tarefas(TAREFAS):
    if TAREFAS == {}:
        print("\nA lista está vazia!\n")
        return

    print("\n" + "-" * 30)

    for titulo, dados in TAREFAS.items():

        print(f"Tarefa: {titulo}")
        print(f"Projeto ID: {dados['projeto_id']}")
        print(f"Status: {dados['status']}")
        print(f"Responsável: {dados.get('responsável_id', '—')}")

        if VERIFICAR_ATRASO(dados):
            print(f"Prazo: {dados['prazo']} (Atrasada)")
        else:
            print(f"Prazo: {dados['prazo']}")

        print("-" * 30)

    print()

def buscar_tarefas(TAREFAS):
    if TAREFAS == {}:
        print("\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
        return

    título_tarefa = input("\nDigite o título da tarefa que deseja buscar informações: ").upper()

    if título_tarefa not in TAREFAS:
        print("ERRO! Tarefa não encontrada!\n")
        return

    tarefa = TAREFAS[título_tarefa]

    print("\n>>>>> RESULTADOS ENCONTRADOS <<<<<")
    print(f"{'-' * 30}\nID da Tarefa: {tarefa.get('id', 'N/A')}")
    print(f"Tarefa: {título_tarefa}")
    print(f"Projeto ID: {tarefa['projeto_id']}")
    print(f"Status: {tarefa['status']}")
    print(f"Responsável ID: {tarefa.get('responsável_id', '—')}")

    if VERIFICAR_ATRASO(tarefa):
        print(f"Prazo: {tarefa['prazo']} (Atrasada)\n{'-' * 30}\n")
    else:
        print(f"Prazo: {tarefa['prazo']}\n{'-' * 30}\n")

def atualizar_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print("\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
    else:
        título_tarefa = input("\nDigite o título da tarefa que deseja alterar os dados: ").upper()
        if (título_tarefa not in TAREFAS):
            print("ERRO! Tarefa não encontrada!\n")
        else:
            tarefa = TAREFAS[título_tarefa]
            print("\n>>>>> PARCIAL <<<<<")
            print(f"{'-' * 30}\nID da Tarefa: {tarefa.get('id', 'N/A')}")
            print(f"Tarefa: {título_tarefa}")
            print(f"Projeto ID: {tarefa['projeto_id']}")
            print(f"Status: {tarefa['status']}")
            print(f"Responsável ID: {tarefa.get('responsável_id', '—')}")
            if (VERIFICAR_ATRASO(tarefa)):
                print(f"Prazo: {tarefa['prazo']} (Atrasada)\n{'-' * 30}\n")
            else:
                print(f"Prazo: {tarefa['prazo']}\n{'-' * 30}\n")

            print("O que você deseja atualizar?\n[1] Título Tarefa\n[2] Status Tarefa\n[3] ID do Responsável da Tarefa\n[4] Prazo da Tarefa\n[5] Projeto da Tarefa")
            escolha = input("Opção: ")
            if (escolha == '1'):
                novo_título = input("\nDigite o título da tarefa que deseja adicionar: ").upper()
                while (novo_título == "" or novo_título in TAREFAS):
                    if (novo_título in TAREFAS):
                        novo_título = input("\n>>> ERRO! Tarefa já existente.\nDigite outro título para a tarefa: ")
                    else:
                        novo_título = input("\n>>> ERRO! O nome está vazio.\nDigite algo válido para o título da tarefa: ")
                TAREFAS[novo_título] = tarefa.copy()
                del TAREFAS[título_tarefa]
                print("Título atualizado com sucesso!\n")

            elif (escolha == '2'):
                novo_status = input("\nDigite a atualização do status da tarefa: ").upper()
                while (novo_status not in ["PENDENTE", "EM ANDAMENTO", "CONCLUÍDA"]):
                    novo_status = input(">>> ERRO! Status inválido. Digite novamente: ").upper()

                tarefa["status"] = novo_status
                print("Status atualizado com sucesso!\n")

            elif (escolha == '3'):
                novo_resp = input("\nDigite o novo ID do responsável pela tarefa: ")
                tarefa["responsável_id"] = novo_resp
                print("Responsável atualizado com sucesso!\n")

            elif (escolha == '4'):
                while True:
                    prazo_texto = input("\nDigite o novo prazo (DD/MM/AAAA): ")
                    try:
                        novo_prazo = datetime.strptime(prazo_texto, "%d/%m/%Y").date()
                        break
                    except ValueError:
                        print(">>> Data inválida! Tente novamente.")

                tarefa["prazo"] = novo_prazo
                print("Prazo atualizado com sucesso!\n")

            elif (escolha == '5'):
                projetos = s.ler_projetos()
                projeto_id = input("Digite o ID do novo projeto ao qual essa tarefa pertence: ")

                if not any(p['id'] == projeto_id for p in projetos):
                    print(">>> ERRO! Projeto não encontrado! Não é possível atualizar a tarefa.\n")
                else:
                    print("Projeto atualizado com sucesso!\n")

            else:
                print("\n>>> ERRO! Por favor, digite uma opção válida de 1 a 6 <<<\n")
        s.gravar_tarefas(TAREFAS)


def remover_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print(
            "\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
    else:
        título_tarefa=input(
            "\nDigite o título da tarefa que deseja remover: ").upper()

        if (título_tarefa in TAREFAS):
            del TAREFAS[título_tarefa]
            print("Tarefa removida com sucesso!\n")
        else:
            print(
                "O título dessa tarefa não existe. Verifique se digitou corretamente ou se salvou com outro nome\n")
        s.gravar_tarefas(TAREFAS)


def limpar_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print(
            "\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
    else:
        escolha=input(
            "\nTem certeza que deseja seguir? Lembre-se TODAS AS TAREFAS serão excluídas PERMANENTEMENTE: ").upper()
        if (escolha == 'S' or escolha == 'SIM' or escolha == "SS"):
            TAREFAS.clear()
            print("\nTodos as tarefas foram removidas.\n")

        elif (escolha == 'N' or escolha == 'NÃO' or escolha == 'NAO' or escolha == 'NN'):
            print("OK, saindo dessa opção...\n")

        else:
            print("Vou entender isso como um 'não'. Mas, se você quiser realmente excluir todas as tarefas, volte aqui e escreva sim\n")
        s.gravar_tarefas(TAREFAS)