from functions import *
from bd import criar_tabelas

def menu():
    print("-"*50)
    print("🍽️  SISTEMA DE GERENCIAMENTO DO RESTAURANTE")
    print("-"*50)
    print("1.  📝 Cadastrar Produto")
    print("2.  �� Buscar Produto")
    print("3.  📋 Listar Produtos")
    print("4.  🗑️ Remover Produto")
    print("5.  ✏️ Atualizar Produto")
    print("6.  🍽️ Realizar Pedido")
    print("7.  📄 Listar Itens do Pedido")
    print("8.  ✏️ Cadastrar Atendente")
    print("9.  👥 Listar Atendentes")
    print("10. 🪑 Cadastrar Mesa")
    print("11. 📊 Listar Mesas")
    print("12. 💰 Fechar Mesa")
    print("13. 📈 Relatório de Vendas")
    print("14. 📊 Relatório Detalhado")
    print("0.  🚪 Sair")
    return input("👉 Escolha uma opção: ").strip()

def main():
    print("🔄 Inicializando sistema...")
    if criar_tabelas():
        print("✅ Sistema inicializado com sucesso!")
    else:
        print("❌ Erro ao inicializar sistema! Verifique o log.")
        return

    while True:
        opcao = menu()

        if opcao == "1":
            print("\n📝 CADASTRAR PRODUTO")
            try:
                nome = input("Nome do produto: ").strip()
                if not nome:
                    print("❌ Nome não pode estar vazio!")
                    continue

                valor = float(input("Valor: R$ "))
                if valor <= 0:
                    print("❌ Valor deve ser maior que zero!")
                    continue

                # categoria = input("Categoria: ").strip()
                # if not categoria:
                #     print("❌ Categoria não pode estar vazia!")
                #     continue

                if cadastrar_produto(nome, valor): # 'categoria' removido
                    print("✅ Produto cadastrado com sucesso!")
                else:
                    print("❌ Erro ao cadastrar produto!")

            except ValueError:
                print("❌ Valor inválido! Digite um número.")
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")

        elif opcao == "2":
            print("\n🔍 BUSCAR PRODUTO")
            termo_busca = input("Digite o nome ou parte do nome do produto: ").strip()
            if not termo_busca:
                print("❌ Termo de busca não pode estar vazio!")
                continue

            produto = buscar_produto(termo_busca)
            if produto:
                print(f"✅ Produto encontrado: {produto}")
            else:
                print(f"❌ Produto com o termo '{termo_busca}' não encontrado.")

        elif opcao == "3":
            print("\n📋 LISTA DE PRODUTOS")
            produtos = listar_produtos()
            if produtos:
                print(f"{'ID':<5} {'Nome':<20} {'Valor':<10}") # 'Categoria' removido
                print("-" * 40) # Ajustado o tamanho da linha
                for produto in produtos:
                    print(f"{produto.id:<5} {produto.nome:<20} R$ {produto.valor:<8.2f}") # 'produto.categoria' removido
            else:
                print("❌ Nenhum produto cadastrado.")

        elif opcao == "4":
            print("\n🗑️ REMOVER PRODUTO")
            produtos = listar_produtos()
            if not produtos:
                print("❌ Nenhum produto cadastrado!")
                continue

            print("\nProdutos disponíveis:")
            print(f"{'ID':<5} {'Nome':<20} {'Valor':<10}") # 'Categoria' removido
            print("-" * 40) # Ajustado o tamanho da linha
            for produto in produtos:
                print(f"{produto.id:<5} {produto.nome:<20} R$ {produto.valor:<8.2f}") # 'produto.categoria' removido

            try:
                id_produto_remover = int(input("\nDigite o ID do produto que deseja remover: "))

                produto_a_remover = None
                for p in produtos:
                    if p.id == id_produto_remover:
                        produto_a_remover = p
                        break

                if not produto_a_remover:
                    print("❌ Produto com o ID informado não encontrado!")
                    continue

                print(f"\n⚠️  Produto encontrado: {produto_a_remover.nome}") # 'categoria' removido
                confirmacao = input("Tem certeza que deseja remover este produto? (s/n): ").strip().lower()
                if confirmacao in ['s', 'sim', 'y', 'yes']:
                    if remover_produto(id_produto_remover):
                        print("✅ Produto removido com sucesso!")
                    else:
                        print("❌ Erro ao remover produto.")
                else:
                    print("❌ Remoção cancelada.")
            except ValueError:
                print("❌ ID inválido! Digite um número.")
            except Exception as e:
                print(f"❌ Erro inesperado ao remover produto: {e}")

        elif opcao == "5":
            print("\n✏️ ATUALIZAR PRODUTO")
            produtos = listar_produtos()
            if not produtos:
                print("❌ Nenhum produto cadastrado!")
                continue

            print("\nProdutos disponíveis:")
            print(f"{'ID':<5} {'Nome':<20} {'Valor':<10}") # 'Categoria' removido
            print("-" * 40) # Ajustado o tamanho da linha
            for produto in produtos:
                print(f"{produto.id:<5} {produto.nome:<20} R$ {produto.valor:<8.2f}") # 'produto.categoria' removido

            try:
                id_produto = int(input("\nDigite o ID do produto que deseja atualizar: "))

                produto_existente = None
                for p in produtos:
                    if p.id == id_produto:
                        produto_existente = p
                        break

                if not produto_existente:
                    print("❌ Produto com o ID informado não encontrado!")
                    continue

                print("\nO que deseja atualizar?")
                print("1 - Nome do produto")
                print("2 - Valor do produto")
                # '3 - Categoria do produto' removido
                print("3 - Todos os campos") # Opção 4 virou 3

                escolha = input("Digite a opção (1/2/3): ").strip() 

                novo_nome = None
                novo_valor = None
                # 'nova_categoria' removido

                if escolha == "1":
                    novo_nome = input(f"Digite o novo nome (atual: {produto_existente.nome}): ").strip()
                    if not novo_nome:
                        print("❌ Nome não pode estar vazio! Mantendo o nome atual.")
                        novo_nome = produto_existente.nome
                        continue

                elif escolha == "2":
                    try:
                        novo_valor_str = input(f"Digite o novo valor (atual: R$ {produto_existente.valor:.2f}): R$ ").strip()
                        if novo_valor_str:
                            novo_valor = float(novo_valor_str)
                            if novo_valor <= 0:
                                print("❌ Valor deve ser maior que zero! Mantendo o valor atual.")
                                novo_valor = produto_existente.valor
                                continue
                    except ValueError:
                        print("❌ Valor inválido! Mantendo o valor atual.")
                        novo_valor = produto_existente.valor
                        continue

                elif escolha == "3": # Agora esta é a opção para atualizar todos os campos
                    novo_nome = input(f"Digite o novo nome (atual: {produto_existente.nome}): ").strip()
                    # 'nova_categoria' removido
                    try:
                        novo_valor_str = input(f"Digite o novo valor (atual: R$ {produto_existente.valor:.2f}): R$ ").strip()
                        if novo_valor_str:
                            novo_valor = float(novo_valor_str)
                            if novo_valor <= 0:
                                print("❌ Valor deve ser maior que zero! Mantendo o valor atual.")
                                novo_valor = produto_existente.valor
                                continue
                    except ValueError:
                        print("❌ Valor inválido! Mantendo o valor atual.")
                        novo_valor = produto_existente.valor
                        continue

                    if not novo_nome: novo_nome = produto_existente.nome
                    if novo_valor is None: novo_valor = produto_existente.valor

                else:
                    print("❌ Opção inválida!")
                    continue

                if atualizar_produto(id_produto, novo_nome, novo_valor): # 'nova_categoria' removido
                    print("✅ Produto atualizado com sucesso!")
                else:
                    print("❌ Erro ao atualizar o produto.")

            except ValueError:
                print("❌ ID inválido! Digite um número.")
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")

        elif opcao == "6":
            print("\n🍽️ REALIZAR PEDIDO")

            produtos = listar_produtos()
            if not produtos:
                print("❌ Nenhum produto cadastrado! Cadastre produtos primeiro.")
                continue

            atendentes = listar_atendentes()
            if not atendentes:
                print("❌ Nenhum atendente cadastrado! Cadastre atendentes primeiro.")
                continue

            mesas = listar_mesas()
            if not mesas:
                print("❌ Nenhuma mesa cadastrada! Cadastre mesas primeiro.")
                continue

            mesas_livres = [m for m in mesas if not m.ocupada]
            if not mesas_livres:
                print("❌ Nenhuma mesa livre disponível!")
                continue

            print("\n Mesas livres:")
            for mesa in mesas_livres:
                print(f"Mesa {mesa.numero} - Capacidade: {mesa.capacidade} pessoas")

            try:
                numero_mesa = int(input("\nNúmero da mesa: "))

                mesa_escolhida = None
                for mesa in mesas_livres:
                    if mesa.numero == numero_mesa:
                        mesa_escolhida = mesa
                        break

                if not mesa_escolhida:
                    print("❌ Mesa não encontrada ou já está ocupada!")
                    continue

                print("\n👥 Atendentes disponíveis:")
                for atendente in atendentes:
                    print(f"ID: {atendente.id} - {atendente.nome}")

                id_atendente = int(input("\nID do atendente: "))

                atendente_encontrado = False
                for atendente in atendentes:
                    if atendente.id == id_atendente:
                        atendente_encontrado = True
                        break

                if not atendente_encontrado:
                    print("❌ Atendente não encontrado!")
                    continue

                print("\n📋 Produtos disponíveis:")
                print(f"{'Nome':<20} {'Valor':<10}") # 'Categoria' removido
                print("-" * 30) # Ajustado o tamanho da linha
                for produto in produtos:
                    print(f"{produto.nome:<20} R$ {produto.valor:<8.2f}") # 'produto.categoria' removido

                itens_pedido = []
                print("\n🛒 Adicionar itens ao pedido:")

                while True:
                    nome_produto = input("Nome do produto (ou 'finalizar' para terminar): ").strip()
                    if nome_produto.lower() in ['finalizar', 'fim', 'sair']:
                        break

                    produto_encontrado_no_loop = None
                    for produto in produtos:
                        if produto.nome.lower() == nome_produto.lower():
                            produto_encontrado_no_loop = produto
                            break

                    if not produto_encontrado_no_loop:
                        print("❌ Produto não encontrado! Tente novamente.")
                        continue

                    try:
                        quantidade = int(input("Quantidade: "))
                        if quantidade <= 0:
                            print("❌ Quantidade deve ser maior que zero!")
                            continue

                        itens_pedido.append((produto_encontrado_no_loop.nome, quantidade))
                        print(f"✅ {quantidade}x {produto_encontrado_no_loop.nome} adicionado ao pedido!")

                    except ValueError:
                        print("❌ Quantidade inválida! Digite um número.")

                if not itens_pedido:
                    print("❌ Nenhum item adicionado ao pedido!")
                    continue

                id_pedido = realizar_pedido(numero_mesa, id_atendente, itens_pedido)
                if id_pedido:
                    print(f"✅ Pedido {id_pedido} realizado com sucesso!")
                else:
                    print("❌ Erro ao realizar o pedido.")

            except ValueError:
                print("❌ Valor inválido! Digite um número.")

        elif opcao == "7":
            print("\n📄 LISTAR ITENS DO PEDIDO")
            try:
                id_pedido = int(input("ID do pedido: "))

                itens = listar_itens_pedido(id_pedido)
                if itens:
                    print(f"\n Itens do Pedido {id_pedido}:")
                    print(f"{'Produto':<25} {'Qtd':<5} {'Valor Unit':<12} {'Subtotal':<10}") # 'Categoria' removido, ajustado Produto para 25
                    print("-" * 60) # Ajustado o tamanho da linha
                    total_pedido = 0
                    for item in itens:
                        subtotal = item.calcular_subtotal()
                        total_pedido += subtotal
                        print(f"{item.nome_produto:<25} {item.quantidade:<5} R$ {item.valor_unitario:<10.2f} R$ {subtotal:<8.2f}") # 'item.categoria' removido
                    print("-" * 60) # Ajustado o tamanho da linha
                    print(f"{'TOTAL DO PEDIDO:':<43} R$ {total_pedido:<8.2f}") # Ajustado para alinhar
                else:
                    print("❌ Nenhum item encontrado para este pedido ou pedido não existe.")
            except ValueError:
                print("❌ ID inválido! Digite um número.")

        elif opcao == "8":
            print("\n👤 CADASTRAR ATENDENTE")
            nome_atendente = input("Nome do atendente: ").strip()
            if not nome_atendente:
                print("❌ Nome não pode estar vazio!")
                continue

            if cadastrar_atendente(nome_atendente):
                print("✅ Atendente cadastrado com sucesso!")
            else:
                print("❌ Erro ao cadastrar atendente.")

        elif opcao == "9":
            print("\n👥 LISTA DE ATENDENTES")
            atendentes = listar_atendentes()
            if atendentes:
                print(f"{'ID':<5} {'Nome':<25} {'Status':<10}")
                print("-" * 45)
                for atendente in atendentes:
                    status = "Ativo" if atendente.ativo else "Inativo"
                    print(f"{atendente.id:<5} {atendente.nome:<25} {status:<10}")
            else:
                print("❌ Nenhum atendente cadastrado.")

        elif opcao == "10":
            print("\n🪑 CADASTRAR MESA")
            try:
                numero = int(input("Número da mesa: "))
                if numero <= 0:
                    print("❌ Número da mesa deve ser maior que zero!")
                    continue

                capacidade = int(input("Capacidade (pessoas): "))
                if capacidade <= 0:
                    print("❌ Capacidade deve ser maior que zero!")
                    continue

                if cadastrar_mesa(numero, capacidade):
                    print("✅ Mesa cadastrada com sucesso!")
                else:
                    print("❌ Erro ao cadastrar mesa (talvez já exista uma mesa com este número).")
            except ValueError:
                print("❌ Valores inválidos! Digite números.")

        elif opcao == "11":
            print("\n🪑 LISTA DE MESAS")
            mesas = listar_mesas()
            if mesas:
                print(f"{'Número':<8} {'Capacidade':<12} {'Status':<10}")
                print("-" * 35)
                for mesa in mesas:
                    status = "Ocupada" if mesa.ocupada else "Livre"
                    print(f"{mesa.numero:<8} {mesa.capacidade:<12} {status:<10}")
            else:
                print("❌ Nenhuma mesa cadastrada.")

        elif opcao == "12":
            print("\n FECHAR MESA")

            mesas = listar_mesas()
            mesas_ocupadas = [m for m in mesas if m.ocupada]

            if not mesas_ocupadas:
                print("❌ Nenhuma mesa ocupada para fechar!")
                continue

            print("\n Mesas ocupadas:")
            for mesa in mesas_ocupadas:
                print(f"Mesa {mesa.numero} - Capacidade: {mesa.capacidade} pessoas")

            try:
                numero_mesa = int(input("\nNúmero da mesa para fechar: "))

                mesa_encontrada = False
                for mesa in mesas_ocupadas:
                    if mesa.numero == numero_mesa:
                        mesa_encontrada = True
                        break

                if not mesa_encontrada:
                    print("❌ Mesa não encontrada ou não está ocupada!")
                    continue

                if fechar_mesa(numero_mesa):
                    print("✅ Mesa fechada com sucesso!")
                else:
                    print("❌ Erro ao fechar mesa.")
            except ValueError:
                print("❌ Número inválido! Digite um número.")

        elif opcao == "13":
            print("\n RELATÓRIO DE VENDAS")
            relatorio = relatorio_vendas()
            if relatorio:
                print("✅ Relatório gerado com sucesso!")
            else:
                print("❌ Erro ao gerar relatório.")

        elif opcao == "14":
            print("\n RELATÓRIO DETALHADO")
            relatorio = relatorio_vendas_detalhado()
            if relatorio:
                print("✅ Relatório detalhado gerado com sucesso!")
            else:
                print("❌ Erro ao gerar relatório detalhado.")

        elif opcao == "0":
            print("\n👋 Finalizando o Sistema. Até mais!")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Gerenciamento do Restaurante!")
    main()