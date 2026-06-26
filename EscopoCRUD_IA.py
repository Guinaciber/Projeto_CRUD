# CRUD de Ativos de TI
# Ativos: Notebook/ Smart TV/ Smartphone/ Video Game/ Impressora / Etc
#Escopo criado por IA

# Estrutura de dados
ativos = {}

# Funções CRUD
def criar_ativo():
    identificador = input("Crie o ID único do dispositivo: ")
    if identificador in ativos:
        print("ID já existe!")
        return
    nome = input("Digite o nome do dispositivo: ")
    tipo = input("Digite o tipo (Notebook/ Smart TV/ Smartphone/ Video Game/ Impressora): ")
    responsavel = input("Digite o responsável: ")
    setor = input("Digite o setor/local: ")
    vulnerabilidades = input("Digite vulnerabilidades (separadas por vírgula, ou deixe vazio): ").split(",")

    ativos[identificador] = {
        "nome": nome,
        "tipo": tipo,
        "responsavel": responsavel,
        "setor": setor,
        "vulnerabilidades": [v.strip() for v in vulnerabilidades if v.strip()]
    }
    print("Ativo cadastrado com sucesso!")

def consultar_ativo():
    identificador = input("Digite o ID do ativo para consulta: ")
    if identificador in ativos:
        print(f"Dados do ativo {identificador}: {ativos[identificador]}")
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

def menu():
    while True:
        print("\n--- MENU ---\n")
        print("1. Criar ativo")
        print("2. Consultar ativo")
        print('3. Listar ativos')
        print("4. Atualizar ativo")
        print("5. Deletar ativo")
        print("6. Sair\n")
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
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")

menu()
# criado branch de escopo. Tentativa 2!