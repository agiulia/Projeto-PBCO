import utils as u

def menu_usuarios():
    while True:
        print("\n=== USUÁRIOS ===\n[1] Inserir usuário\n[2] Listar todos os usuários\n[3] Buscar usuário\n[4] Atualizar dados de um usuário\n[5] Remover um usuário\n[6] Remover TODOS os usuários\n[0] Sair")
        i = input("\nOpção: ")
        if i == "0":
            break
        elif i == "1":
            u.inserir_usuarios()
        elif i == "2":
            u.listar_usuarios()
        elif i == "3":
            u.buscar_usuarios()
        elif i == "4":
            u.atualizar_usuarios()
        elif i == "5":
            u.remover_usuarios()
        elif i == "6":
            u.limpar_usuarios()
        else:
            print("\nValor inválido. Tente novamente.")


def menu():
    while True:
        print("\n=== MENU ===\nQue parte deseja acessar?\n[1] Usuários\n[2] Projetos\n[3] Tarefas\n")
        o = input("\nOpção: ")
        if (o == "1"):
            print(menu_usuarios())
        elif (o == "2"):
            print("Estamos trabalhando nisso no momento.")
            continue
        elif (o == "3"):
            print("Estamos trabalhando nisso no momento.")
        else:
            print("Valor Inválido.")
            continue

menu()