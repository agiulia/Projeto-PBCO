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

    if not u.validar_lista(lista_usuarios):
        return False, "Não há usuários registrados no sistema."

    return True, lista_usuarios

def buscar_usuarios():
    b = input("Digite alguma informação do usuário que deseja encontrar: ")
    lista_usuarios = s.ler_usuarios()

    if not lista_usuarios:
        print("Não há usuários registrados no sistema.")
        time.sleep(2)
        return
    
    encontrado = any(b == str(v) for i in lista_usuarios for v in i.values())

    if not encontrado:
        print("Usuário não encontrado.")
    else:
        for i in lista_usuarios:
            for chave in i.keys():
                if b == i[chave]:
                    print(f"\n=== Informações Usuário ===\nID: {i['id']}\nNome: {i['nome']}\nE-mail: {i['e-mail']}\nPerfil: {i['perfil']}")
    time.sleep(2)

def atualizar_usuarios():
    email = input("Digite o e-mail do usuário que deseja atualizar: ")
    lista_usuarios = s.ler_usuarios()

    usuario = next((u for u in lista_usuarios if u.get('e-mail') == email), None)

    if not usuario:
        print("Usuário não encontrado.")
        time.sleep(2)
        return

    print("O que deseja alterar?\n[1] ID\n[2] Nome\n[3] E-mail\n[4] Perfil")
    o = input("\nOpção: ")

    if o == "1":
        while True:
            uid = input("Digite o novo ID do usuário: ")
            if srv.validar_uid(uid, lista_usuarios):
                usuario['id'] = uid
                break
            print("Este ID já está em uso. Tente novamente.\n")
            time.sleep(2)
    elif o == "2":
        while True:
            nome = input("Digite o novo nome: ")
            if srv.validar_nome(nome):
                usuario['nome'] = nome
                break
            print("Nome inválido. Tente novamente.\n")
            time.sleep(2)
    elif o == "3":
        while True:
            novo_email = input("Digite o novo e-mail: ")
            if srv.validar_email(email, lista_usuarios):
                usuario['e-mail'] = email
                break
            print("E-mail inválido ou já registrado. Tente novamente.\n")
            time.sleep(2)
    elif o == "4":
        while True:
            print("Selecione o novo perfil:\n[1] Admin\n[2] User\n[3] Campo vazio")
            novo_perfil = input("\nOpção: ")
            if novo_perfil == "1":
                usuario['perfil'] = "admin"
                break
            elif novo_perfil == "2":
                usuario['perfil'] = "user"
                break
            elif novo_perfil == "3":
                usuario['perfil'] = ""
                break
            else:
                print("Valor inválido. Tente novamente.")
                time.sleep(2)
                continue
            
    else:
        print("Opção inválida.")
        time.sleep(2)
        return

    s.gravar_usuarios(lista_usuarios)
    print(f"\nUsuário atualizado com sucesso!\nID: {usuario['id']}\nNome: {usuario['nome']}\nE-mail: {usuario['e-mail']}\n")
    time.sleep(2)

def remover_usuarios():
    email = input("Digite o e-mail do usuário que deseja remover: ")
    lista_usuarios = s.ler_usuarios()
    novos_usuarios = [u for u in lista_usuarios if u.get('e-mail') != email]
    if len(novos_usuarios) == len(lista_usuarios):
        print("Usuário não encontrado.")
        time.sleep(2)
    else:
        s.gravar_usuarios(novos_usuarios)
        print(f"Usuário com e-mail '{email}' removido com sucesso!")
        time.sleep(2)

def limpar_usuarios():
    while True:
        i = input("Você quer excluir todos os dados permanentemente? (SIM/NÃO): ").strip().upper()
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

def inserir_projetos (projeto):
    while True :
        id=input('digite o ID do dono do projeto:').strip()
        if id  in projeto['ID']:
            print('ERRO!, Nome ja existente')
        elif id not in projeto['ID']:
            projeto['ID'].append (id)
            break


    while True:
        nome_projeto=input("digite o nome do projeto:").strip ().lower()
        if nome_projeto in projeto['nome']:
             print('ERRO!, Nome ja existente')
        elif nome_projeto not in projeto['nome']:
             projeto['nome'].append (nome_projeto)
             break
    while True:
        descriçao_projeto=input("faça uma leve descrição do  projeto:"). strip().lower()
        projeto['descriçao'].append (descriçao_projeto)
        print('Descrição do projeto inserida corretamente')
        break

       
    while True:
        try:
            data_inicio = input("de a data de início:").strip()
            data_fim= input("de a data de fim:").strip()
            data_inicio=datetime.strptime(data_inicio,"%d/%m/%Y")
            data_fim=datetime.strptime(data_fim,"%d/%m/%Y")
            if data_inicio> data_fim :
                print ('data iválida digite uma nova data')
            else:
                print ('data válida')
                print ('\n data adiconada com sucesso')
                break
        except ValueError:
                print ('Erro: Formato inválido! Use dd/mm/aaaa (ex: 25/12/2025)\n')

    projeto['data_inicio'].append(data_inicio)
    projeto['data_fim'].append (data_fim)
    return 'o projeto foi inserido corretamente'

def listar_projetos():
    lista_projetos = s.ler_projetos()
    if not lista_projetos:
        print("\nNão há projetos registrados no sistema.\n")
        time.sleep(2)
        return
    print("\n=== Lista de Projetos ===\n")
    for item in lista_projetos:
        print(f"Nome: {item['nome']}\nDescrição: {item['descricao']}\nID Responsável: {item['id']}\nData Início: {item['inicial']}\nData Fim: {item['fim']}\n")
    time.sleep(2)

def buscar_projetos(projeto):
    while True:
        print ('como voce prefere buscar seu projeto: \n[1] por ID \n[2] por nome \n[3] por descrição \n[4] por data de início \n[5] por data de fim\n[0] sair da busca')
        menu_busca=input ('digite uma opção:')
        if(menu_busca=='1'):
            i=input('digite o ID que do projeto que voce deseja achar')
            if i in projeto['ID']:
                index_i=projeto['ID'].index (i)
                print ('projeto encontrado com seucesso')
                print (projeto['ID'][index_i])
                print (projeto['nome'][index_i])
                print (projeto['descrição'][index_i])
                print (projeto['data_inicio'][index_i])
                print (projeto['data_fim'][index_i])
                break
            else:
                print('projeto não encontrado digite novamente')


        elif (menu_busca=='2'):
            x=input('digite o nome do projeto que voce deseja buscar:').lower()
            if x in projeto['nome']:
                index_x=projeto['nome'].index(x)
                print ('projeto encontado com sucesso')
                print (projeto['ID'][index_x])
                print (projeto['nome'][index_x])
                print (projeto['descriçao'][index_x])
                print (projeto['data_inicio'][index_x])
                print (projeto['data_fim'][index_x])
                break
            else:
                print('ERRO!,projeto não encontrado')
               
        elif (menu_busca=='3'):
                y= input('digite a descrição do projeto que voce deseja buscar:').lower().strip()
                if y in projeto['descriçao']:
                    index_y=projeto['descriçao'].index(y)
                    print (projeto['ID'][index_y])
                    print (projeto['nome'][index_y])
                    print (projeto['descriçao'][index_y])
                    print (projeto['data_inicio'][index_y])
                    print (projeto['data_fim'][index_y])
                    break
                else:
                    print('Projeto não encontrado.')
                   
        elif (menu_busca=='4'):
                data_i= input('Informe o início do projeto que voce deseja buscar: ').strip()
                data_i=datetime.strptime(data_i,'%d/%m/%Y')
                while True :
                    if projeto['data_inicio'].count(data_i)>1 :
                        repetido=input('temos mais de um projeto com esse.Pderia dar alguma informasção única como nome ou ID por exemplo?(digite 1 para sim e 2 para não)').strip()
                        if repetido=='1':
                            print (buscar_projetos (projeto))
                            break
                        elif repetido=='2':
                            print('então não posso te ajudar. Desculpe')
                            break
                        else:
                            print('nenhuma opção válida foi digitada, peço que digite novamente.')
                if data_i in projeto['data_inicio']:
                    index_data_i=projeto['data_inicio'].index(data_i)
                    print ('projeto encontado com sucesso')
                    print (projeto['ID'][index_data_i])
                    print (projeto['nome'][index_data_i])
                    print (projeto['descriçao'][index_data_i])
                    print (projeto['data_inicio'][index_data_i])
                    print (projeto['data_fim'][index_data_i])
                    break
                else:
                    print('Projeto não encontrado. Tente novamente.')

        elif (menu_busca=='5'):
                data_f= input('de a data de fim do projeto:').strip()
                data_f=datetime.strptime(data_f,'%d/%m/%Y')
                while True :
                    if projeto['data_fim'].count(data_f)>1 :
                        repetido=input('temos mais de um projeto com esse.Pderia dar alguma informasção única como nome ou ID do dono do projeto por exemplo?(digite 1 para sim e 2 para não)').strip()
                        if repetido=='1':
                            print (buscar_projetos (projeto))
                            break
                        elif repetido=='2':
                            print('então não posso te ajudar. Desculpe')
                            break
                        else:
                            print('nenhuma opção válida foi digitada, peço que digite novamente.')


                if data_f in projeto['data_fim']:
                    index_data_f=projeto['data_fim'].index(data_f)
                    print ('projeto encontado com sucesso')
                    print (projeto['nome'][index_data_f])
                    print (projeto['descriçao'][index_data_f])
                    print (projeto['data_inicio'][index_data_f])
                    print (projeto['data_fim'][index_data_f])
                    break
                else:
                    print('ERRO!,projeto não encontrado')
                   
        elif(menu_busca=='0'):
             break
        else:
             print ('voce digitou nenhuma alternativa')
             
def atualizar_projetos (projeto):
    print(buscar_projetos (projeto))
    while True:
        print('qual parte do seu projeto voce gostaria de atualizar?. \n[1] Nome, \n[2] descrição, \n[3] data de início, \n[4] data de fim \n[0] sair da atualização')
        atualizar_projeto = input('digite uma opção:')
        if (atualizar_projeto=='0'):
            break
        while True :    
            antigo_nome=input('digite o nome do projeto que voce deseja substituir').strip().lower()
            if(antigo_nome in projeto['nome']):
                index_x= projeto['nome'].index(antigo_nome)
                x1= input('digite o novo nome do projeto').strip().lower()
                projeto['nome'][index_x]=x1
                print ('nome do projeto substituido perfeitamente')
                break

            elif (atualizar_projeto== '2'):
                antiga_descricao=input('digite a   descrição  que voce deseja substituir:').strip().lower()
                if( antiga_descricao in projeto['descrição']):
                    index_d= projeto['descrição'].index(antiga_descricao)
                    x2= input('digite o novo nome da descrição').strip().lower()
                    projeto['descrição'][index_d]=x2
                    print ('descrição do projeto substituida perfeitamente')
                    break

                elif (atualizar_projeto== '3'):
                    antiga_data_i=input('digite a da data inicial  que voce deseja substituir:(formato DD/MM/AAAA)')
                    if( antiga_data_i in projeto['data_inicio']):
                        index_data_i= projeto['data_inicio'].index(antiga_data_i)
                        x3= input('digite a nova data inicial formato DD/MM/AAAA').strip()
                        x33=datetime.strptime(x3,"%d/%m/%Y")
                        projeto['data_inicio'][index_data_i]=x33
                        print ('data inicial do projeto substituida perfeitamente')
                        break
                elif atualizar_projeto == '4':
                    antiga_data_f = input('Digite a data final que deseja substituir (DD/MM/AAAA): ').strip()
   
                if antiga_data_f in projeto['data_fim']:
                    index_data_f = projeto['data_fim'].index(antiga_data_f)
                    projeto['data_fim'][index_data_f] = datetime.strptime(
                    input('Digite a nova data final (DD/MM/AAAA): ').strip(),"%d/%m/%Y")
                    print('Data final do projeto substituída perfeitamente!')
                    break
                else:
                    print('Data final não encontrada!')

def remover_projetos (projeto):
    remover = input('Digite o nome do projeto que voce gostaria de remover:').lower().strip()
    if remover in projeto['nome']:
        indice_remover = projeto['nome'].index(remover)
        for i in projeto:
             del projeto['nome'][i][indice_remover]
        print('projeto removido com sucesso')
    else:
         print('projeto não encontrado')

def limpar_projetos(projeto):
     for chave in projeto:
        projeto[chave].clear()

def VERIFICAR_ATRASO(tarefa):
    if tarefa['prazo'] < datetime.now().date() and tarefa['status'] != "CONCLUÍDA":
        return True
    else:
        return False

def inserir_tarefas(TAREFAS):
    título_tarefa = input(
        "\nDigite o título da tarefa que deseja adicionar: ")

    if (título_tarefa != ''):
        status_tarefa = input(
            f"Informe os status da tarefa (Pendente, Em andamento ou Concluída): ").upper()

        while (status_tarefa != "PENDENTE" and status_tarefa != "EM ANDAMENTO" and status_tarefa != "CONCLUÍDA"):
            status_tarefa = input(
                f"ERRO! Informe os status da tarefa novamente com 'Pendente', 'Em andamento' ou 'Concluída': ").upper()

        responsável_tarefa = input(
            "Digite o nome do responsável pela tarefa: ")
        prazo_texto = input(
            "Digite o prazo dessa tarefa no formato DD/MM/AAAA: ")

        while True:
            try:
                prazo_tarefa = datetime.strptime(
                    prazo_texto, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data inválida! Tente novamente.\n")
                prazo_texto = input(
                    "Digite o prazo dessa tarefa no formato DD/MM/AAAA: ")

        TAREFAS[título_tarefa] = {
            "status": status_tarefa,
            "responsável": responsável_tarefa,
            "prazo": prazo_tarefa
        }
        
        s.gravar_tarefas(TAREFAS)
        print("Tarefa salva.\n")
    else:
        print("O nome está vazio. Digite algo válido!\n")

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