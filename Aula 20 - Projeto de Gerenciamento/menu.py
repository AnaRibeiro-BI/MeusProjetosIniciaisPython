def menu():
    print("Menu - Gerenciamento do Restaurante")
    print("1. Cadastrar Produto")
    print("2. Buscar Produto")
    print("3. Listar Produtos")
    print("4. Remover Produto")
    print("5. Atualizar Produto")
    print("6. Realizar Pedido")
    print("7. Listar Itens do Pedido")
    print("8. Cadastrar Atendente")
    print("9. Listar Atendentes")
    print("10. Abrir Mesa")
    print("11. Listar Mesas")
    print("12. Fechar Mesa")
    print("13. Relatório de Vendas")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

if opcao == "1":
            nome = input("Nome: ")
            valor = float(input("Valor: R$"))
            inserir_produto(conection(), nome, valor) # chama a função inserir_produto passando a conexão com o banco de dados (conection()), nome e valor do produto
            print("✅ Produto cadastrado com sucesso!")

elif opcao == "2":
    nome = input("Digite o nome produto que deseja buscar: ")
    resultados = buscar_produto(conection(), nome) # resultados recebe a lista de produtos encontrados
    # busca o produto pelo nome fazendo conecção com o banco de dados (connection()) e passando o nome do produto a ser buscado
    if resultados:
        for r in resultados: # r para cada resultao encontrado
                    print(r) # imprime o resultado
    elif not resultados:
        print("🚫 Produto não encontrado.")

elif opcao 3 == "3": 
    produtos = listar_produtos(conection()) # lista todos os produtos cadastrados no banco de dados
    if produtos:
        for produto in produtos:
            print(produto) 
    elif not resultados:
        print("🚫 Nenhum produto cadastrado.")

elif opcao == "4":
    nome_produto = int(input("Digite o nome do produto que deseja remover: "))
    sucesso = remover_produto(conection(), nome_produto)
    if sucesso:
        print("✅ Produto removido com sucesso!")
    else:
        print("🚫 Produto não encontrado.")

elif opcao == "5": # Atualizar Produto
    produtos = listar_produtos(conection()) # Lista todos os produtos cadastrados
    nome_atual = input("Digite o nome do produto que deseja atualizar: ")
    print("O que deseja atualizar?")
    print("1 - Nome do produto")
    print("2 - Valor do produto")
    print("3 - Nome e valor do produto")
    escolha = input("Digite a opção (1/2/3): ")

    # Inicializa variáveis com None para evitar erros caso não sejam atribuídos valores
    novo_nome = None
    novo_valor = None

    if escolha == "1":
        novo_nome = input("Digite o novo nome do produto: ")
    elif escolha == "2":
        novo_valor = float(input("Digite o novo valor do produto: R$"))
    elif escolha == "3":
        novo_nome = input("Digite o novo nome do produto: ")
        novo_valor = float(input("Digite o novo valor do produto: R$"))
    else:
        print("🚫 Opção inválida!")
        escolha = None
    # Só chama a função se a escolha foi válida
    if escolha in ["1", "2", "3"]: # dicionário de opções válidas
        sucesso = atualizar_produto(conection(), nome_atual, novo_nome, novo_valor) # chama a função atualizar_produto passando a conexão com o banco de dados (conection()), nome atual, novo nome e novo valor
        if sucesso:
            print("✅ Produto atualizado com sucesso!")
        else:
            print("🚫 Produto não encontrado ou erro ao atualizar!")

elif opcao == "6": # Realizar Pedido
    produtos = listar_produtos(conection()) # Lista todos os produtos cadastrados
    id_mesa = int(input("Número da mesa: "))
    id_atendente = int(input("ID do atendente: "))
    itens_pedido = []
    while True:
        nome_produto = input("Nome do produto (ou 'sair' para finalizar): ")
        if nome_produto.lower() == "sair":
            break
        quantidade = int(input("Quantidade: "))
        itens_pedido.append((nome_produto, quantidade))
    sucesso = realizar_pedido(conection(), id_mesa, id_atendente, itens_pedido)
    if sucesso:
        print("✅ Pedido realizado com sucesso!")
    else:
        print("🚫 Erro ao realizar o pedido.")

