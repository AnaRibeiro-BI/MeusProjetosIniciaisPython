from functions import *
from tabela import *
from bd import criar_conexao


def menu():
    print("\n===== Menu - Gerenciamento do Restaurante =====")
    print("1. Cadastrar Produto")
    print("2. Buscar Produto")
    print("3. Listar Produtos")
    print("4. Remover Produto")
    print("5. Atualizar Produto")
    print("6. Realizar Pedido")
    print("7. Listar Itens do Pedido")
    print("8. Cadastrar Atendente")
    print("9. Listar Atendentes")
    print("10. Cadastrar Mesa")
    print("11. Abrir Mesa")
    print("12. Listar Mesas")
    print("13. Fechar Mesa")
    print("14. Relatório de Vendas")
    print("0. Sair")
    return input("Escolha uma opção: ").strip()

def main():
    while True:
        opcao = menu()

if opcao == "1": # 1 - Cadastrar Produto
        print("\n📝 CADASTRAR PRODUTO")
        nome = input("Nome: ")
        valor = float(input("Valor: R$"))
        categoria = input("Categoria: ")
        cadastrar_produto(criar_conexao(), nome, valor, categoria)
        print("✅ Produto cadastrado com sucesso!")

elif opcao == "2": # 2 - Buscar Produto
        print("\n📋 LISTA DE PRODUTOS")
        nome = input("Digite o nome do produto que deseja buscar: ")
        resultados = buscar_produto(criar_conexao(), nome)
        if resultados:
            for r in resultados:
                print(r)
        else:
            print("🚫 Produto não encontrado.")

elif opcao == "3": # 3 - Listar Produtos
        print("\n🔍 BUSCAR PRODUTO")
        produtos = listar_produtos(criar_conexao())
        if produtos:
            for produto in produtos:
                print(produto)
        else:
            print("🚫 Nenhum produto cadastrado.")

elif opcao == "4": # 4 - Remover Produto
    print("\n🗑️ REMOVER PRODUTO")
    produtos = listar_produtos()
    if not produtos:
        print("🚫 Nenhum produto cadastrado!")
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    sucesso = remover_produto(criar_conexao(), nome_produto)
    if sucesso:
        print("✅ Produto removido com sucesso!")
    else:
        print("🚫 Produto não encontrado.")

elif opcao == "5": # 5 - Atualizar Produto
        nome_atual = input("Digite o nome do produto que deseja atualizar: ")
        print("O que deseja atualizar?")
        print("1 - Nome do produto")
        print("2 - Valor do produto")
        print("3 - Categoria do produto")
        escolha = input("Digite a opção (1/2/3): ")
        novo_nome = None
        novo_valor = None
        nova_categoria = None
        if escolha == "1":
            novo_nome = input("Digite o novo nome do produto: ")
        elif escolha == "2":
                novo_valor = float(input("Digite o novo valor do produto: R$"))
        elif escolha == "3":
            novo_nome = input("Digite a nova categoria do produto: ")
        else:
            print("🚫 Opção inválida!")

        if escolha in ["1", "2", "3"]:
            sucesso = atualizar_produto(criar_conexao(), nome_atual, novo_nome, novo_valor, nova_categoria)
            if sucesso:
                print("✅ Produto atualizado com sucesso!")
            else:
                print("🚫 Produto não encontrado ou erro ao atualizar!")

elif opcao == "6": # 6 - Realizar Pedido
    print("\n🍽️ REALIZAR PEDIDO")
    produtos = listar_produtos(criar_conexao())
    mesas = listar_mesas(criar_conexao())
    id_mesa = int(input("Número da mesa: "))    
    # Mostrar mesas livres
    mesas = listar_mesas()
    mesas_livres = [m for m in mesas if not m.ocupada]
    if not mesas_livres:
        print("🚫 Nenhuma mesa livre disponível!")
    for mesa in mesas_livres:
        print(mesa)
    
    # Mostrar atendentes
    atendentes = listar_atendentes(criar_conexao())
    atendentes = listar_atendentes()
    if not atendentes:
            print("🚫 Nenhum atendente cadastrado!")
    id_atendente = int(input("ID do atendente: "))
    for atendente in atendentes:
                print(atendente)

    itens_pedido = []
    while True:
            nome_produto = input("Nome do produto (ou 'sair' para finalizar): ")
            if nome_produto.lower() == "sair":
                break
            quantidade = int(input("Quantidade: "))
            itens_pedido.append((nome_produto, quantidade))
    sucesso = realizar_pedido(criar_conexao(), id_mesa, id_atendente, itens_pedido)
    if sucesso:
            print("✅ Pedido realizado com sucesso!")
    else:
            print("🚫 Erro ao realizar o pedido.")

elif opcao == "7": # 7 - Listar Itens do Pedido
        id_pedido = int(input("ID do pedido: "))
        itens = listar_itens_pedido(criar_conexao(), id_pedido)
        if itens:
            for item in itens:
                print(item)
        else:
            print("🚫 Nenhum item encontrado para este pedido.")

elif opcao == "8": # 8 - Cadastrar Atendente
        print("\n👤 CADASTRAR ATENDENTE")
        nome_atendente = input("Nome do atendente: ").strip()
        sucesso = cadastrar_atendente(criar_conexao(), nome_atendente)
        if sucesso:
            print("✅ Atendente cadastrado com sucesso!")
        else:
            print("🚫 Erro ao cadastrar atendente.")

elif opcao == "9": # 9 - Listar Atendentes
        print("\n👥 LISTA DE ATENDENTES")
        atendentes = listar_atendentes(criar_conexao())
        if atendentes:
            for atendente in atendentes:
                print(atendente)
        else:
            print("🚫 Nenhum atendente cadastrado.")

elif opcao == "10":  # Cadastrar Mesa
            print("\n🪑 CADASTRAR MESA")
            try:
                numero = int(input("Número da mesa: "))
                capacidade = int(input("Capacidade (pessoas): "))
                cadastrar_mesa(numero, capacidade)
            except ValueError:
                print("🚫 Valores inválidos!")

elif opcao == "11": # 10 - Abrir Mesa
        numero_mesa = int(input("Número da mesa: "))
        sucesso = abrir_mesa(criar_conexao(), numero_mesa)
        if sucesso:
            print("✅ Mesa aberta com sucesso!")
        else:
            print("🚫 Erro ao abrir mesa.")

elif opcao == "12": # 11 - Listar Mesas
        print("\n🪑 LISTA DE MESAS")
        mesas = listar_mesas(criar_conexao())
        if mesas:
            for mesa in mesas:
                print(mesa)
        else:
            print("🚫 Nenhuma mesa cadastrada.")

elif opcao == "13": # 12 - Fechar Mesa
        print("\n💰 FECHAR MESA")
        numero_mesa = int(input("Número da mesa: "))
        sucesso = fechar_mesa(criar_conexao(), numero_mesa)
        if sucesso:
            print("✅ Mesa fechada com sucesso!")
        else:
            print("🚫 Erro ao fechar mesa.")

elif opcao == "14": # 13 - Relatório de Vendas
        print("1 - Relatório Simples")
        print("2 - Relatório Detalhado")
        escolha_relatorio = input("Digite a opção (1/2): ")
        if escolha_relatorio == "1":
            print(relatorio_vendas(criar_conexao()))
        elif escolha_relatorio == "2":
            print(relatorio_vendas_detalhado(criar_conexao()))
        else:
            print("🚫 Opção inválida!")

elif opcao == "0": # Sair do sistema
        print("Finalizando o Sistema. Até mais!")
        criar_conexao.close() # Fechar conexão ao sair
else:
    print("🚫 Opção inválida! Tente novamente.")