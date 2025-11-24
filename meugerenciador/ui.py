import utils as u
import time

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
            time.sleep(2)

def menu_projetos():
    while True:
        print ("\n=== projeto ===\n""[1] Inserir projeto\n""[2] Listar todos os projetos\n[3] Buscar projeto\n[4] Atualizar dados de um projeto\n[5] Remover um projeto\n[6] Remover TODOS os projetos\n[0] Sair")
        menu=(input('digite sua opção: '))
        if menu=='1':
            u.inserir_projetos()
        elif menu=='2':
            u.listar_projetos()
        elif menu =='3':
            u.buscar_projetos ()
        elif menu=='4':
            u.atualizar_projetos ()
        elif menu=='5':
            u.remover_projetos()
        elif menu== '6':
            u.limpar_projetos()
        if menu=='0':
            break



def menu():
    while True:
        print("\n=== MENU ===\nQue parte deseja acessar?\n[1] Usuários\n[2] Projetos\n[3] Tarefas\n")
        o = input("\nOpção: ")
        if (o == "1"):
            print(menu_usuarios())
        elif (o =="2" ):
            print(menu_projetos)
            continue
        elif (o == "3"):
            print("Estamos trabalhando nisso no momento.")
        else:
            print("Valor Inválido.")
            time.sleep(2)
            continue