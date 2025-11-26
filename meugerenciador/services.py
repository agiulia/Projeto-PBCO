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

import storage as s
from datetime import datetime

def inserir_projetos(lista):
    uid = input("Digite o ID do dono do projeto: ")
    nome = input("Digite o nome do projeto: ")
    descricao = input("Faça uma leve descrição do projeto: ")

    while True:
        try:
            inicio = datetime.strptime(input("Digite a data de início (DD/MM/AAAA): "), "%d/%m/%Y").date()
            fim = datetime.strptime(input("Digite a data de fim (DD/MM/AAAA): "), "%d/%m/%Y").date()
            break
        except:
            print("Erro: Formato inválido! Use DD/MM/AAAA")

    projeto = {
        "id": uid,
        "nome": nome,
        "descricao": descricao,
        "inicio": inicio,
        "fim": fim
    }

    lista.append(projeto)
    s.gravar_projetos(lista)
    print("Projeto inserido com sucesso!")

def listar_projetos(lista):
    if not lista:
        print("\nNão há projetos cadastrados.\n")
        return
    print("\n=== Lista de Projetos ===\n")
    for item in lista:
        print(f"ID: {item['id']}\nNome: {item['nome']}\nDescrição: {item['descricao']}\nData Início: {item['inicio'].strftime('%d/%m/%Y')}\nData Fim: {item['fim'].strftime('%d/%m/%Y')}\n")

def buscar_projetos(lista):
    busca = input("Digite o nome ou ID do projeto: ")
    encontrados = [p for p in lista if p['nome'] == busca or p['id'] == busca]
    if not encontrados:
        print("Nenhum projeto encontrado.")
        return
    for item in encontrados:
        print(f"ID: {item['id']}\nNome: {item['nome']}\nDescrição: {item['descricao']}\nData Início: {item['inicio'].strftime('%d/%m/%Y')}\nData Fim: {item['fim'].strftime('%d/%m/%Y')}\n")

def atualizar_projetos(lista):
    termo = input("Digite o ID do projeto que deseja atualizar: ").strip()
    projeto = next((p for p in lista if p['id'] == termo), None)

    if not projeto:
        print("Projeto não encontrado!")
        return

    print("O que deseja atualizar?")
    print("[1] Nome\n[2] Descrição\n[3] Data Início\n[4] Data Fim")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        projeto['nome'] = input("Digite o novo nome: ").strip()
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
                print("Formato inválido!")
    elif opcao == "4":
        while True:
            nova_data = input("Digite a nova data de fim (DD/MM/AAAA): ").strip()
            try:
                datetime.strptime(nova_data, "%d/%m/%Y")
                projeto['fim'] = nova_data
                break
            except ValueError:
                print("Formato inválido!")
    else:
        print("Opção inválida!")
        return

    s.gravar_projetos(lista)
    print("Projeto atualizado com sucesso!")
    
def remover_projetos (projeto):
    remover = input('Digite o nome do projeto que voce gostaria de remover:').lower().strip()
    if remover in projeto['nome']:
        indice_remover = projeto['nome'].index(remover)
        for i in projeto:
             del projeto['nome'][i][indice_remover]
        print('projeto removido com sucesso')
    else:
         print('projeto não encontrado')

def limpar_projetos(lista):
    resposta = input("Você quer excluir todos os projetos permanentemente? (SIM/NÃO): ").strip().upper()
    if resposta == "SIM":
        lista.clear()
        s.gravar_projetos(lista)
        print("Todos os projetos foram removidos.")
    else:
        print("Ação cancelada.")


def VERIFICAR_ATRASO(tarefa):
    if tarefa['prazo'] < datetime.now().date() and tarefa['status'] != "CONCLUÍDA":
        return True
    else:
        return False

def inserir_tarefas(TAREFAS):
    título_tarefa = input("\nDigite o título da tarefa que deseja adicionar: ").upper()
    while (título_tarefa == "" or título_tarefa in TAREFAS):
        if (título_tarefa in TAREFAS):
            título_tarefa = input("\n>>> ERRO! Tarefa já existente.\nDigite outro título para a tarefa: ")
        else:
            título_tarefa = input("\n>>> ERRO! O nome está vazio.\nDigite algo válido para o título da tarefa: ")
    status_tarefa = input(f"Informe os status da tarefa (Pendente, Em andamento ou Concluída): ").upper()
    while (status_tarefa != "PENDENTE" and status_tarefa != "EM ANDAMENTO" and status_tarefa != "CONCLUÍDA" and status_tarefa != "CONCLUIDA"):
        status_tarefa = input(f">>> ERRO! Tente novamente.\nInforme os status da tarefa novamente com 'Pendente', 'Em andamento' ou 'Concluída': ").upper()
    if (status_tarefa == "EM ANDAMENTO"):
        status_tarefa = "Em andamento"
    elif (status_tarefa == "PENDENTE"):
        status_tarefa = "Pendente"
    else:
        status_tarefa = "Concluída"
    responsável_tarefa = input("Digite o nome do responsável pela tarefa: ")
    prazo_texto = input("Digite o prazo dessa tarefa no formato DD/MM/AAAA: ")
    while True:
        try:
            prazo_tarefa = datetime.strptime(prazo_texto, "%d/%m/%Y").date()
            break
        except ValueError:
            print(">>> Data inválida! Tente novamente.\n")
            prazo_texto = input("Digite o prazo dessa tarefa no formato DD/MM/AAAA: ")
    TAREFAS[título_tarefa] = {
        "status": status_tarefa,
        "responsável": responsável_tarefa,
        "prazo": prazo_tarefa
    }
    s.gravar_tarefas(TAREFAS)
    print("Tarefa salva.\n")

def listar_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print("\nA lista está vazia!\n")
    else:
        print()
        print("-" * 30)

        for título, dados in TAREFAS.items():
            print(f"Tarefa: {título}")
            print(f"Status: {dados['status']}")
            print(f"Responsável: {dados['responsável']}")

            if VERIFICAR_ATRASO(dados):
                print(f"Prazo: {dados['prazo']} (Atrasada)")
            else:
                print(f"Prazo: {dados['prazo']}")
            print("-" * 30)

        print()


def buscar_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print(
            "\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
    else:
        título_tarefa = input(
            "\nDigite o título da tarefa que deseja buscar informações: ")

        if (título_tarefa not in TAREFAS):
            print("ERRO! Tarefa não encontrada!\n")

        else:
            tarefa = TAREFAS[título_tarefa]
            print("\n>>>>> RESULTADOS ENCONTRADOS <<<<<")
            print(f"{'-' * 30}\nTarefa: {título_tarefa}")
            print(f"Status: {tarefa['status']}")
            print(f"Responsável: {tarefa['responsável']}")

            if (VERIFICAR_ATRASO(tarefa)):
                print(f"Prazo: {tarefa['prazo']} (Atrasada)\n{'-' * 30}\n")
            else:
                print(f"Prazo: {tarefa['prazo']}\n{'-' * 30}\n")

def atualizar_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print("\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
    else:
        título_tarefa = input("\nDigite o título da tarefa que deseja alterar os dados: ")

        if (título_tarefa not in TAREFAS):
            print("ERRO! Tarefa não encontrada!\n")
        else:
            tarefa = TAREFAS[título_tarefa]

            print("\n>>>>> PARCIAL <<<<<")
            print(f"{'-' * 30}\nTarefa: {título_tarefa}")
            print(f"Status: {tarefa['status']}")
            print(f"Responsável: {tarefa['responsável']}")

            if (VERIFICAR_ATRASO(tarefa)):
                print(f"Prazo: {tarefa['prazo']} (Atrasada)\n{'-' * 30}\n")
            else:
                print(f"Prazo: {tarefa['prazo']}\n{'-' * 30}\n")

            print("O que você deseja atualizar?\n[1] Título Tarefa\n[2] Status Tarefa\n[3] Responsável da Tarefa\n[4] Prazo da Tarefa")
            escolha = input("Opção: ")

            if (escolha == '1'):
                novo_título = input("\nDigite o novo título da tarefa: ")
                if (novo_título != ''):
                    TAREFAS[novo_título] = tarefa.copy()
                    del TAREFAS[título_tarefa]
                    print("Título atualizado com sucesso!\n")
                else:
                    print("O nome está vazio. Digite algo válido!\n")

            elif (escolha == '2'):
                novo_status = input("\nDigite a atualização do status da tarefa: ").upper()
                while (novo_status not in ["PENDENTE", "EM ANDAMENTO", "CONCLUÍDA"]):
                    novo_status = input(">>> ERRO! Status inválido. Digite novamente: ").upper()

                tarefa["status"] = novo_status
                print("Status atualizado com sucesso!\n")

            elif (escolha == '3'):
                novo_resp = input("\nDigite o novo responsável pela tarefa: ")
                tarefa["responsável"] = novo_resp
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

            else:
                print("\n>>> ERRO! Por favor, digite uma opção válida de 1 a 4 <<<\n")
        s.gravar_tarefas(TAREFAS)


def remover_tarefas(TAREFAS):
    if (TAREFAS == {}):
        print(
            "\nA lista de tarefas está vazia! Portanto, não há opções possíveis aqui\n")
    else:
        título_tarefa=input(
            "\nDigite o título da tarefa que deseja remover: ")

        if (título_tarefa in TAREFAS):
            del TAREFAS[título_tarefa]
            print()
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