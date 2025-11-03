import storage as s
import time
import re

def inserir_usuarios():
    while True:
        usuario = {}

        uid = input("Digite o ID do usuário: ")
        usuario['id'] = uid

        nome = input("Digite o nome: ")
        if not nome or len(nome) < 3:
            print("Por favor, insira um nome com no mínimo 3 caracteres.")
            time.sleep(2)
            continue
        usuario['nome'] = nome

        email = input("Digite o e-mail: ")

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("Formato de e-mail inválido. Tente novamente.\n")
            time.sleep(2)
            continue

        usuarios_existentes = s.ler_usuario()
        if any(u.get('e-mail') == email for u in usuarios_existentes):
            print("Este valor já está registrado no sistema.\n")
            time.sleep(2)
            continue
        usuario['e-mail'] = email

        print("Selecione o novo perfil:\n[1] Admin\n[2] User\n[3] Campo vazio")
        perfil = input("\nOpção: ")
        if perfil == "1":
            usuario['perfil'] = "admin"
        elif perfil == "2":
            usuario['perfil'] = "user"
        elif perfil == "3":
            usuario['perfil'] = ""
        else:
            print("Valor inválido. Tente novamente.\n")
            time.sleep(2)
            continue
        
        s.gravar_usuario(usuario)
        print("Usuário adicionado com sucesso!\n")
        time.sleep(2)
        break

def listar_usuarios():
    lista_usuarios = s.ler_usuario()
    if not lista_usuarios:
        print("\nNão há usuários registrados no sistema.\n")
        time.sleep(2)
        return
    print("\n=== Lista de Usuários ===\n")
    for item in lista_usuarios:
        print(f"ID: {item['id']}\nNome: {item['nome']}\nE-mail: {item['e-mail']}\nPerfil: {item['perfil']}\n")
    time.sleep(2)
    return

def buscar_usuarios():
    b = input("Digite alguma informação do usuário que deseja encontrar: ")
    lista_usuarios = s.ler_usuario()

    if not lista_usuarios:
        print("Não há usuários registrados no sistema.")
        time.sleep(2)
        return
    
    encontrado = any(b in i.values() for i in lista_usuarios)

    if not encontrado:
        print("Usuário não encontrado.")
    else:
        for i in lista_usuarios:
            for chave in i.keys():
                if b == i[chave]:
                    print(f"\n=== Informações Usuário ===\nID: {i['id']}\nNome: {i['nome']}\nE-mail: {i['e-mail']}\nPerfil: {i['perfil']}")

    time.sleep(2)
    return

def atualizar_usuarios():
    email = input("Digite o e-mail do usuário que deseja atualizar: ")
    lista_usuarios = s.ler_usuario()

    usuario = next((u for u in lista_usuarios if u.get('e-mail') == email), None)

    if not usuario:
        print("Usuário não encontrado.")
        time.sleep(2)
        return

    print("O que deseja alterar?\n[1] ID\n[2] Nome\n[3] E-mail\n[4] Perfil")
    o = input("\nOpção: ")

    if o == "1":
        usuario['id'] = input("Digite o novo ID: ")
    elif o == "2":
        usuario['nome'] = input("Digite o novo nome: ")
    elif o == "3":
        novo_email = input("Digite o novo e-mail: ")
        if any(u.get('e-mail') == novo_email for u in lista_usuarios if u is not usuario):
            print("Este e-mail já está registrado. Tente novamente.\n")
            return
        usuario['e-mail'] = novo_email
    elif o == "4":
        print("Selecione o novo perfil:\n[1] Admin\n[2] User\n[3] Campo vazio")
        novo_perfil = input("\nOpção: ")
        if novo_perfil == "1":
            novo_perfil = "admin"
        elif novo_perfil == "2":
            novo_perfil = "user"
        elif novo_perfil == "3":
            novo_perfil = ""
        else:
            print("Valor inválido. Tente novamente.")
            time.sleep(2)
            return
        usuario['perfil'] = novo_perfil
    else:
        print("Opção inválida.")
        time.sleep(2)
        return

    s.gravar_usuarios(lista_usuarios)
    print(f"\nUsuário atualizado com sucesso!\nID: {usuario['id']}\nNome: {usuario['nome']}\nE-mail: {usuario['e-mail']}\n")
    time.sleep(2)

def remover_usuarios():
    email = input("Digite o e-mail do usuário que deseja remover: ")
    lista_usuarios = s.ler_usuario()
    novos_usuarios = [u for u in lista_usuarios if u.get('e-mail') != email]
    if len(novos_usuarios) == len(lista_usuarios):
        print("Usuário não encontrado.")
        time.sleep(2)
        return
    
    s.gravar_usuarios(novos_usuarios)
    print(f"Usuário com e-mail '{email}' removido com sucesso!")
    time.sleep(2)

def limpar_usuarios():
    while True:
        i = input("Você quer excluir todos os dados permanentemente?").upper()
        if i == "SIM":
            novos_usuarios = []
            s.gravar_usuarios(novos_usuarios)
            print("Arquivo limpo com sucesso!")
            time.sleep(2)
            break
        elif i == "NÃO":
            print("Operação cancelada.")
            time.sleep(2)
            break
        else:
            print("Opção Inválida. Tente novamente.\n")
            time.sleep(2)
            continue