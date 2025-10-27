from menu import menu
import functions as fn

print(" 📊 Sistema de Gerênciamento de Restaurante")
while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- Cadastrar Produto ---")
        try:
            nome = input("Nome do produto: ")
            valor = float(input("Valor (R$): "))
            if fn.cadastrar_produto(nome, valor):
                print("✅ Produto cadastrado com sucesso!")
        except ValueError:
            print("🚫 Erro: Valor deve ser um número (ex: 10.50).")
        input("Pressione Enter para continuar...")

    elif opcao == "2":
        print("\n--- Buscar Produto ---")
        nome = input("Digite o nome produto que deseja buscar: ")
        resultados = fn.buscar_produto(nome)
        if resultados:
            print("Resultados encontrados:")
            for r in resultados: # r para cada resultado encontrado
                print(f"ID: {r[0]}, Nome: {r[1]}, Valor: R$ {r[2]:.2f}")
        else:
            print("🚫 Nenhum produto encontrado.")
        input("Pressione Enter para continuar...")

    elif opcao == "3":
        print("\n--- Listar Produtos ---")
        produtos = fn.listar_produtos()
        if produtos:
            for p in produtos:
                print(f"ID: {p[0]}, Nome: {p[1]}, Valor: R$ {p[2]:.2f}")
        else:
            print("🚫 Nenhum produto cadastrado.")
        input("Pressione Enter para continuar...")

    elif opcao == "4":
        print("\n--- Remover Produto ---")
        try:
            id_prod = int(input("ID do produto a remover: "))
            fn.remover_produto(id_prod)
        except ValueError:
            print("🚫 Erro: ID deve ser um número inteiro.")
        input("Pressione Enter para continuar...")

    elif opcao == "5":
        print("\n--- Editar Produto ---")
        try:
            nome_antigo = input("Nome do produto a editar: ")
            nome_novo = input("Novo nome: ")
            valor_novo = float(input("Novo valor (R$): "))
            fn.atualizar_produto(nome_antigo, nome_novo, valor_novo)
        except ValueError:
            print("🚫 Erro: Valor deve ser um número.")
        input("Pressione Enter para continuar...")

    elif opcao == "7":
        print("\n--- Listar Itens do Pedido ---")
        try:
            id_ped = int(input("ID do pedido: "))
            itens = fn.listar_itens_pedido(id_ped)
            if itens:
                print(f"Itens do Pedido {id_ped}:")
                valor_total_pedido = 0
                for i in itens:
                    # Formato: [ID Item, Nome Produto, Qtd, Valor Unit, Valor Total Item]
                    print(f"  - Item {i[0]}: {i[1]} (Qtd: {i[2]}) - R$ {i[3]:.2f} un. - Total: R$ {i[4]:.2f}")
                    valor_total_pedido += i[4]
                print(f"\nValor Total do Pedido: R$ {valor_total_pedido:.2f}")
            else:
                print("🚫 Nenhum item encontrado para este pedido.")
        except ValueError:
            print("🚫 Erro: ID deve ser um número inteiro.")
        input("Pressione Enter para continuar...")

    # Funções ainda não implementadas
    elif opcao in ("6", "8", "9", "10", "11", "12", "13"):
        print(f"\n⚠️ Opção {opcao} ainda não implementada.")
        input("Pressione Enter para continuar...")

    elif opcao == "0":
        print("✅ Saindo do sistema. Até logo!")
        break

    else:
        print("🚫 Opção inválida! Tente novamente.")
        input("Pressione Enter para continuar...")