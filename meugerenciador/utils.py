import json
import storage as s

def inserir_usuarios():
    while True:
        usuario = {}

        uid = input("Digite o ID do usuário: ")
        usuario['id'] = uid
        nome = input("Digite o nome: ")
        if not nome:
            print("Por favor, insira um nome.")
            continue
        usuario['nome'] = nome
        email = input("Digite o e-mail: ")
        usuarios_existentes = s.ler_usuario()
        if any(u.get('e-mail') == email for u in usuarios_existentes):
            print("Este valor já está registrado no sistema.\n")
            continue
        usuario['e-mail'] = email
        usuario['perfil'] = input("Digite o perfil do usuário: ")
        if usuario['perfil'] != "admin" and usuario['perfil'] != "funcionário"
            print("Valor inválido. Tente novamente.")
            continue
        s.gravar_usuario(usuario)
        print("Usuário adicionado com sucesso!\n")
        break

def listar_usuarios():
    lista_usuarios = s.ler_usuario()
    if not lista_usuarios:
        print("\nNão há usuários registrados no sistema.\n")
        return
    print("\n=== Lista de Usuários ===\n")
    for item in lista_usuarios:
        print(f"ID: {item['id']}\nNome: {item['nome']}\nE-mail: {item['e-mail']}\nPerfil: {item['perfil']}")

def buscar_usuarios():
    b = input("Digite alguma informação do usuário que deseja encontrar: ")
    lista_usuarios = s.ler_usuario()
    if lista_usuarios == []:
        print("Não há usuários registrados no sistema.")
    else:
        for i in lista_usuarios:
            for chave in i.keys():
                if b == i[chave]:
                    print(f"\nid: {i['id']}\nNome: {i['nome']}\nE-mail: {i['e-mail']}\nPerfil: {i['perfil']}")

def atualizar_usuarios():
    email = input("Digite o e-mail do usuário que deseja atualizar: ")
    lista_usuarios = s.ler_usuario()

    usuario = next((u for u in lista_usuarios if u.get('e-mail') == email), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    print("O que deseja alterar?\n[1] ID\n[2] Nome\n[3] E-mail\n[4] Perfil")
    opcao = input("\nOpção: ")

    if opcao == "1":
        usuario['id'] = input("Digite o novo ID: ")
    elif opcao == "2":
        usuario['nome'] = input("Digite o novo nome: ")
    elif opcao == "3":
        novo_email = input("Digite o novo e-mail: ")
        if any(u.get('e-mail') == novo_email for u in lista_usuarios if u is not usuario):
            print("Este e-mail já está registrado. Tente novamente.\n")
            return
        usuario['e-mail'] = novo_email
    elif opcao == "4":
        novo_perfil = input("Digite o novo perfil:").lower()
        if novo_perfil != "admin" and novo_perfil != "funcionário"
            print("Valor inválido. Tente novamente.")
            return
        usuario['perfil'] = novo_perfil
    else:
        print("Opção inválida.")
        return

    s.gravar_usuarios(lista_usuarios)
    print(f"\nUsuário atualizado com sucesso!\nID: {usuario['id']}\nNome: {usuario['nome']}\nE-mail: {usuario['e-mail']}\n")

def remover_usuarios():
    email = input("Digite o e-mail do usuário que deseja remover: ")
    lista_usuarios = s.ler_usuario()
    novos_usuarios = [u for u in lista_usuarios if u.get('e-mail') != email]
    if len(novos_usuarios) == len(lista_usuarios):
        print("Usuário não encontrado.")
        return
    s.gravar_usuarios(novos_usuarios)
    print(f"Usuário com e-mail '{email}' removido com sucesso!")

def limpar_usuarios():
    while True:
        i = input("Você quer excluir todos os dados permanentemente?").upper()
        if i == "SIM":
            novos_usuarios = []
            s.gravar_usuarios(novos_usuarios)
            print("Arquivo limpo com sucesso!")
            break
        elif i == "NÃO":
            print("Operação cancelada.")
            break
        else:
            print("Opção Inválida. Tente novamente.\n")
            continue