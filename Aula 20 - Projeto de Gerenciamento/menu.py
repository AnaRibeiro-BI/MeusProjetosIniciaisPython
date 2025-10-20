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
            valor = Aluno(nome, idade)
            inserir_produto(conection(), nome, valor)
            print("✅ Produto cadastrado com sucesso!")

elif opcao == "2":
    nome = input("Digite o nome produto que deseja buscar: ")
    resultados = buscar_produto(conection(), nome) # resultados recebe a lista de produtos encontrados
    # busca o produto pelo nome fazendo conecção com o banco de dados (connection()) e passando o nome do produto a ser buscado
    if resultados:
        for r in resultados: # r para cada resultao encontrado
                    print(r) # imprime o resultado

elif opcao 3 == "3": 
    produtos = listar_produtos(conection())
    if produtos:
        for produto in produtos:
            print(produto) 




else:
    print("🚫 Nenhum produto encontrado.")