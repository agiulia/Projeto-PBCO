import services as srv
import utils as u
import storage as s
import time
import reports as r

def ms_iu():
    uid = input("Digite o ID do usuário: ").strip()
    nome = input("Digite o nome: ").strip()
    email = input("Digite o e-mail: ").strip()

    print("Selecione o perfil:")
    print("[1] Admin\n[2] User\n[3] Campo vazio")
    perfil_opcao = input("Opção: ").strip()

    ok, msg = srv.inserir_usuario(uid, nome, email, perfil_opcao)
    print(msg)
    time.sleep(2)

def ms_lu():
    sucesso, resultado = srv.listar_usuarios()

    if not sucesso:
        print("\nNão há usuários registrados no sistema.\n")
        time.sleep(2)
        return

    print("\n=== Lista de Usuários ===\n")
    for item in resultado:
        print(f"ID: {resultado['id']}")
        print(f"Nome: {resultado['nome']}")
        print(f"E-mail: {resultado['email']}")
        print(f"Perfil: {resultado['perfil']}\n")

    print("\nUsuários listados com sucesso.\n")
    time.sleep(2)

def ms_bu():
    b = input("Digite o e-mail do usuário que deseja encontrar: ").strip()
    sucesso, resultado = srv.buscar_usuarios(b)

    if not sucesso:
        print(f"\n{resultado}\n")  
        time.sleep(2)
        return

    usuario = resultado 

    print("\n=== Usuário Encontrado ===\n")
    print(f"ID: {usuario['id']}\nNome: {usuario['nome']}\nE-mail: {usuario['email']}\nPerfil: {usuario['perfil']}")

    print("Busca concluída com sucesso.\n")
    time.sleep(2)

def ms_au():
    email = input("Digite o e-mail do usuário que deseja atualizar: ")

    print("\nO que deseja alterar?")
    print("[1] ID\n[2] Nome\n[3] E-mail\n[4] Perfil")
    opcao = input("\nOpção: ")

    campos = {
        "1": "id",
        "2": "nome",
        "3": "email",
        "4": "perfil"
    }

    if opcao not in campos:
        print("Opção inválida.")
        time.sleep(2)
        return

    campo = campos[opcao]

    if campo == "perfil":
        print("\nSelecione o novo perfil:")
        print("[1] Admin\n[2] User\n[3] Campo vazio")
        v = input("\nOpção: ")
        novo_valor = {"1": "admin", "2": "user", "3": ""}.get(v)
        if novo_valor is None:
            print("Perfil inválido.")
            time.sleep(2)
            return
    else:
        novo_valor = input(f"Digite o novo valor para {campo}: ")

    sucesso, resposta = srv.atualizar_usuarios(email, campo, novo_valor)

    if not sucesso:
        print(resposta)
        time.sleep(2)
        return

    usuario = resposta
    print("\nUsuário atualizado com sucesso!")
    print(f"ID: {usuario['id']}\nNome: {usuario['nome']}\nE-mail: {usuario['email']}\nPerfil: {usuario['perfil']}")
    time.sleep(2)

def ms_ru():
    email = input("Digite o e-mail do usuário que deseja remover: ")
    x, resultado = srv.remover_usuarios(email)
    print(resultado)
    time.sleep(2)

def ms_lru():
    while True:
        resposta = input("Você quer excluir todos os dados permanentemente? (SIM/NÃO): ").strip().upper()

        confirmacao = u.validar_confirmacao(resposta)

        if confirmacao is None:
            print("Opção inválida. Tente novamente.\n")
            time.sleep(2)
            continue

        x, mensagem = srv.limpar_usuarios(confirmacao)
        print(mensagem)
        time.sleep(2)
        break

def mostrar_resumo_projetos():
    resumo = r.resumo_projetos()

    print("\n=== RESUMO POR PROJETO ===\n")

    if not resumo:
        print("Não há tarefas registradas.\n")
        time.sleep(2)
        return

    for projeto, dados in resumo.items():
        print(f"\n>>> Projeto: {projeto}")
        print(f"Total de tarefas: {dados['total']}")
        print(f"Percentual concluído: {dados['percentual_concluido']:.2f}%")
        print("Status:")
        for status, qtd in dados["status"].items():
            print(f"  - {status}: {qtd}")
        print("-" * 30)

    time.sleep(2)


def mostrar_produtividade_usuarios():
    print("\n=== PRODUTIVIDADE POR USUÁRIO ===\n")

    data_ini = input("Data inicial (dd/mm/yyyy): ").strip()
    data_fim = input("Data final (dd/mm/yyyy): ").strip()

    if not u.parse_date(data_ini) or not u.parse_date(data_fim):
        print("\nDatas inválidas. Tente novamente.\n")
        time.sleep(2)
        return

    resultado = r.produtividade_usuarios(data_ini, data_fim)

    if "erro" in resultado:
        print(resultado["erro"])
        time.sleep(2)
        return

    if not resultado:
        print("\nNenhuma tarefa concluída no período informado.\n")
        time.sleep(2)
        return

    print("\nTarefas concluídas por usuário:\n")
    for usuario, qtd in resultado.items():
        print(f"{usuario}: {qtd}")

    time.sleep(2)

def mostrar_tarefas_atrasadas():
    print("\n=== TAREFAS ATRASADAS ===\n")
    atrasadas = r.tarefas_atrasadas()

    if not atrasadas:
        print("Nenhuma tarefa atrasada.\n")
        time.sleep(2)
        return

    for t in atrasadas:
        print(f"Tarefa: {t.get('titulo', 'Sem título')}")
        print(f"Responsável: {t.get('responsavel', 'Não informado')}")
        print(f"Projeto: {t.get('projeto', 'Sem projeto')}")
        print(f"Prazo: {t.get('prazo', '-')}")
        print(f"Status atual: {t.get('status', '-')}")
        print("-" * 30)

    time.sleep(2)

def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===\n[1] Resumo por projeto\n[2] Produtividade por usuário\n[3] Tarefas atrasadas\n[0] Sair")

        o = input("Escolha uma opção: ")

        if o == "1":
            mostrar_resumo_projetos()
        elif o == "2":
            mostrar_produtividade_usuarios()
        elif o == "3":
            mostrar_tarefas_atrasadas()
        elif o == "0":
            break
        else:
            print("Opção inválida!")
            time.sleep(2)
    
def menu_usuarios():
    while True:
        print("\n=== USUÁRIOS ===\n[1] Inserir usuário\n[2] Listar todos os usuários\n[3] Buscar usuário\n[4] Atualizar dados de um usuário\n[5] Remover um usuário\n[6] Remover TODOS os usuários\n[0] Sair")
        o = input("\nOpção: ")
        if o == "0":
            break
        elif o == "1":
            ms_iu()
        elif o == "2":
            ms_lu()
        elif o == "3":
            ms_bu()
        elif o == "4":
            ms_au()
        elif o == "5":
            ms_ru()
        elif o == "6":
            srv.limpar_usuarios()
        else:
            print("\nValor inválido. Tente novamente.")
            time.sleep(2)

def menu_projetos():
    projetos = s.ler_projetos()

    while True:
        print ("\n=== PROJETOS ===\n""[1] Inserir projeto\n""[2] Listar todos os projetos\n[3] Buscar projeto\n[4] Atualizar dados de um projeto\n[5] Remover um projeto\n[6] Remover TODOS os projetos\n[0] Sair")
        o = input("\nOpção: ")
        if o == '0':
            break
        elif o =='1':
            srv.inserir_projetos(projetos)
        elif o =='2':
            srv.listar_projetos(projetos)
        elif o =='3':
            srv.buscar_projetos (projetos)
        elif o =='4':
            srv.atualizar_projetos (projetos)
        elif o =='5':
            srv.remover_projetos(projetos)
        elif o == '6':
            srv.limpar_projetos(projetos)
        else:
            print("\nValor inválido. Tente novamente.")
            time.sleep(2)

def menu_tarefas():
    tarefas = s.ler_tarefas()

    while True:
        print ("\n=== TAREFAS ===\n""[1] Inserir tarefa\n""[2] Listar todas as tarefas\n[3] Buscar tarefa\n[4] Atualizar dados de uma tarefa\n[5] Remover uma tarefa\n[6] Remover TODAS as tarefas\n[0] Sair")
        o = input("\nOpção: ")
        if o == '0':
            break
        elif o =='1':
            srv.inserir_tarefas(tarefas)
        elif o =='2':
            srv.listar_tarefas(tarefas)
        elif o =='3':
            srv.buscar_tarefas (tarefas)
        elif o =='4':
            srv.atualizar_tarefas (tarefas)
        elif o =='5':
            srv.remover_tarefas(tarefas)
        elif o == '6':
            srv.limpar_tarefas(tarefas)
        else:
            print("\nValor inválido. Tente novamente.")
            time.sleep(2)

def menu():
    while True:
        print("\n=== MENU ===\nQue parte deseja acessar?\n[1] Usuários\n[2] Projetos\n[3] Tarefas\n[4] Relatórios\n[0] Sair")
        o = input("\nOpção: ")
        if (o == "1"):
            menu_usuarios()
        elif (o =="2" ):
            menu_projetos()
        elif (o == "3"):
            menu_tarefas()
        elif (o == "4"):
            menu_relatorios()
        elif (o == "0"):
            print("Saindo do sistema.")
            time.sleep(2)
            break
        else:
            print("Valor Inválido.")
            time.sleep(2)
            continue