# CRUD de Ativos de TI
# Ativos: Notebook/ Smart TV/ Smartphone/ Video Game/ Impressora / Etc

# Estrutura de dados
ativos = {}

def criar_ativo():
    identificador = input("Crie o ID único do dispositivo: ")
    if identificador in ativos:
        print("ID já existe!")
        return
    nome = input("Digite o nome do dispositivo: ")
    tipo = input("Digite o tipo (Notebook/ Smart TV/ Smartphone/ PC Gamer/ Video Game/ Impressora): ")
    responsavel = input("Digite o responsável: ")
    setor = input("Digite o setor/local: ")

    ativos[identificador] = {
        "nome": nome,
        "tipo": tipo,
        "responsavel": responsavel,
        "setor": setor,
        "vulnerabilidades": []
    }
    print("Ativo cadastrado com sucesso!")

def consultar_ativo():
    identificador = input("Digite o ID do ativo para consulta: ")
    if identificador in ativos:
        print(f"Dados do ativo {identificador}:")
        for chave, valor in ativos[identificador].items():
            if chave == "vulnerabilidades":
                print("Vulnerabilidades:")
                if valor:
                    for v in valor:
                        print(f" - Descrição: {v['descricao']} | Severidade: {v['severidade']} | Status: {v['status']}")
                else:
                    print("   Nenhuma vulnerabilidade cadastrada.")
            else:
                print(f"{chave.capitalize()}: {valor}")
    else:
        print("Ativo não encontrado.")

def listar_ativos():
    if ativos:
        print("Lista de ativos cadastrados:")
        for id, dados in ativos.items():
            print(f"ID: {id} | Nome: {dados['nome']} | Tipo: {dados['tipo']} | Responsável: {dados['responsavel']} | Setor: {dados['setor']}")
    else:
        print("Nenhum ativo cadastrado ainda!")

def atualizar_ativo():
    identificador = input("Digite o ID do ativo para atualizar: ")
    if identificador in ativos:
        campo = input("Digite o campo a atualizar (nome, tipo, responsavel, setor): ")
        valor = input("Digite o novo valor: ")
        ativos[identificador][campo] = valor
        print("Ativo atualizado com sucesso!")
    else:
        print("Ativo não encontrado.")

def deletar_ativo():
    identificador = input("Digite o ID do ativo para remover: ")
    if identificador in ativos:
        del ativos[identificador]
        print("Ativo removido com sucesso!")
    else:
        print("Ativo não encontrado.")

def cadastrar_vulnerabilidade(): # adicionado função para cadastrar vulnerabilidades aos ativos
    identificador = input("Digite o ID do ativo para adicionar vulnerabilidade: ")
    if identificador in ativos:
        descricao = input("Digite a descrição da vulnerabilidade: ")
        severidade = input("Digite a severidade (Baixa/Média/Alta/Crítica): ")
        status = input("Digite o status (Aberta/Em tratamento/Corrigida/Aceita como risco): ")

        vulnerabilidade = {
            "descricao": descricao,
            "severidade": severidade,
            "status": status
        }

        ativos[identificador]["vulnerabilidades"].append(vulnerabilidade)
        print("Vulnerabilidade cadastrada com sucesso!")
    else:
        print("Ativo não encontrado.")

def atualizar_vulnerabilidade():
    identificador = input("Digite o ID do ativo: ")
    if identificador in ativos:
        vulnerabilidades = ativos[identificador]["vulnerabilidades"]
        if not vulnerabilidades:
            print("Este ativo não possui vulnerabilidades cadastradas.")
            return

        print("Vulnerabilidades cadastradas:")
        for i, v in enumerate(vulnerabilidades, start=1):
            print(f"{i}. Descrição: {v['descricao']} | Severidade: {v['severidade']} | Status: {v['status']}")

        escolha = int(input("Digite o número da vulnerabilidade que deseja atualizar: "))
        if 1 <= escolha <= len(vulnerabilidades):
            campo = input("Digite o campo a atualizar (descricao, severidade, status): ")
            if campo in vulnerabilidades[escolha - 1]:
                novo_valor = input(f"Digite o novo valor para {campo}: ")
                vulnerabilidades[escolha - 1][campo] = novo_valor
                print("Vulnerabilidade atualizada com sucesso!")
            else:
                print("Campo inválido.")
        else:
            print("Número inválido.")
    else:
        print("Ativo não encontrado.")

def menu():
    while True:
        print("\n--- MENU ---\n")
        print("1. Criar ativo")
        print("2. Consultar ativo")
        print("3. Listar ativos")
        print("4. Atualizar ativo")
        print("5. Deletar ativo")
        print("6. Cadastrar vulnerabilidade")
        print("7. Atualizar vulnerabilidade")
        print("8. Sair\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_ativo()
        elif opcao == "2":
            consultar_ativo()
        elif opcao == "3":
            listar_ativos()
        elif opcao == "4":
            atualizar_ativo()
        elif opcao == "5":
            deletar_ativo()
        elif opcao == "6":
            cadastrar_vulnerabilidade()
        elif opcao == "7":
            atualizar_vulnerabilidade()
        elif opcao == "8":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")

# versão final!
menu()
