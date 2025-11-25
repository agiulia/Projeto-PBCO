import services as srv
import time

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
    sucesso, resultado = srv.listar_usuarios_service()

    if not sucesso:
        print("\nNão há usuários registrados no sistema.\n")
        time.sleep(2)
        return

    print("\n=== Lista de Usuários ===\n")
    for item in resultado:
        print(f"ID: {item['id']}\nNome: {item['nome']}\nE-mail: {item['e-mail']}\nPerfil: {item['perfil']}\n")

    print("\nUsuários listados com sucesso.\n")
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
            srv.listar_usuarios()
        elif o == "3":
            srv.buscar_usuarios()
        elif o == "4":
            srv.atualizar_usuarios()
        elif o == "5":
            srv.remover_usuarios()
        elif o == "6":
            srv.limpar_usuarios()
        else:
            print("\nValor inválido. Tente novamente.")
            time.sleep(2)

def menu_projetos():
    while True:
        print ("\n=== PROJETOS ===\n""[1] Inserir projeto\n""[2] Listar todos os projetos\n[3] Buscar projeto\n[4] Atualizar dados de um projeto\n[5] Remover um projeto\n[6] Remover TODOS os projetos\n[0] Sair")
        o = input("\nOpção: ")
        if o == '0':
            break
        elif o =='1':
            srv.inserir_projetos()
        elif o =='2':
            srv.listar_projetos()
        elif o =='3':
            srv.buscar_projetos ()
        elif o =='4':
            srv.atualizar_projetos ()
        elif o =='5':
            srv.remover_projetos()
        elif o == '6':
            srv.limpar_projetos()
        else:
            print("\nValor inválido. Tente novamente.")
            time.sleep(2)

def menu():
    while True:
        print("\n=== MENU ===\nQue parte deseja acessar?\n[1] Usuários\n[2] Projetos\n[3] Tarefas\n")
        o = input("\nOpção: ")
        if (o == "1"):
            print(menu_usuarios())
        elif (o =="2" ):
            print(menu_projetos())
        elif (o == "3"):
            print("Estamos trabalhando nisso no momento.")
        else:
            print("Valor Inválido.")
            time.sleep(2)
            continue