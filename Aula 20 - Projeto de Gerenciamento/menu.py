# Menu principal do Sistema de Gerenciamento do Restaurante
from functions import *
from bd import criar_conexao, criar_tabelas

def menu(): # Exibe o menu principal e retorna a opção escolhida
    print("-"*50)
    print("🍽️  SISTEMA DE GERENCIAMENTO DO RESTAURANTE")
    print("-"*50)
    print("1.  📝 Cadastrar Produto")
    print("2.  🔍 Buscar Produto")
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
    print("-"*50)
    return input("👉 Escolha uma opção: ").strip()

def main(): # Função principal do sistema
    
    print("🔄 Inicializando sistema...")
    if criar_tabelas():
        print("✅ Sistema inicializado com sucesso!")
    else:
        print("❌ Erro ao inicializar sistema!")
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
                    
                valor = float(input("Valor: R\$ "))
                if valor <= 0:
                    print("❌ Valor deve ser maior que zero!")
                    continue
                    
                categoria = input("Categoria: ").strip()
                if not categoria:
                    print("❌ Categoria não pode estar vazia!")
                    continue
                
                if cadastrar_produto(nome, valor, categoria):
                    print("✅ Produto cadastrado com sucesso!")
                else:
                    print("❌ Erro ao cadastrar produto!")
                    
            except ValueError:
                print("❌ Valor inválido! Digite um número.")
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")

        elif opcao == "2":  
            print("\n🔍 BUSCAR PRODUTO")
            nome = input("Digite o nome do produto: ").strip()
            if not nome:
                print("❌ Nome não pode estar vazio!")
                continue
            
            produto = buscar_produto(nome)
            if produto:
                print(f"✅ Produto encontrado: {produto}")
            else:
                print("❌ Produto não encontrado.")

        elif opcao == "3": 
            print("\n📋 LISTA DE PRODUTOS")
            produtos = listar_produtos()
            if produtos:
                print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {'Valor':<10}")
                print("-" * 55)
                for produto in produtos:
                    print(f"{produto.id:<5} {produto.nome:<20} {produto.categoria:<15} R$ {produto.valor:<8.2f}")
            else:
                print("❌ Nenhum produto cadastrado.")

        elif opcao == "4":  # ✅ CORREÇÃO: Buscar por NOME em vez de ID
            print("\n🗑️ REMOVER PRODUTO")
            produtos = listar_produtos()
            if not produtos:
                print("❌ Nenhum produto cadastrado!")
                continue
                
            # Mostrar produtos disponíveis
            print("\nProdutos disponíveis:")
            print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {'Valor':<10}")
            print("-" * 55)
            for produto in produtos:
                print(f"{produto.id:<5} {produto.nome:<20} {produto.categoria:<15} R\$ {produto.valor:<8.2f}")
            
            # buscar por NOME em vez de ID
            nome_produto = input("\nDigite o NOME do produto que deseja remover: ").strip()
            if not nome_produto:
                print("❌ Nome não pode estar vazio!")
                continue
            
            # Buscar o produto pelo nome para obter o ID
            produto_encontrado = None
            for produto in produtos:
                if produto.nome.lower() == nome_produto.lower():  # Comparação case-insensitive
                    produto_encontrado = produto
                    break
            
            if produto_encontrado:
                # Confirmar remoção
                print(f"\n�� Produto encontrado:")
                print(f"ID: {produto_encontrado.id}")
                print(f"Nome: {produto_encontrado.nome}")
                print(f"Categoria: {produto_encontrado.categoria}")
                print(f"Valor: R\$ {produto_encontrado.valor:.2f}")
                
                confirmacao = input("\n⚠️  Tem certeza que deseja remover este produto? (s/n): ").strip().lower()
                if confirmacao in ['s', 'sim', 'y', 'yes']:
                    if remover_produto(produto_encontrado.id):  # Usar o ID encontrado
                        print("✅ Produto removido com sucesso!")
                    else:
                        print("❌ Erro ao remover produto.")
                else:
                    print("❌ Remoção cancelada.")
            else:
                print(f"❌ Produto '{nome_produto}' não encontrado.")
                # Sugestão de produtos similares
                print("\n💡 Produtos disponíveis:")
                for produto in produtos:
                    print(f"   • {produto.nome}")

        elif opcao == "5":  
            print("\n✏️ ATUALIZAR PRODUTO")
            produtos = listar_produtos()
            if not produtos:
                print("❌ Nenhum produto cadastrado!")
                continue
                
            # Mostrar produtos disponíveis
            print("\nProdutos disponíveis:")
            print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {'Valor':<10}")
            print("-" * 55)
            for produto in produtos:
                print(f"{produto.id:<5} {produto.nome:<20} {produto.categoria:<15} R$ {produto.valor:<8.2f}")
            
            try:
                id_produto = int(input("\nDigite o ID do produto que deseja atualizar: "))
                
                print("\nO que deseja atualizar?")
                print("1 - Nome do produto")
                print("2 - Valor do produto")
                print("3 - Categoria do produto")
                print("4 - Todos os campos")
                
                escolha = input("Digite a opção (1/2/3/4): ").strip()
                
                novo_nome = None
                novo_valor = None
                nova_categoria = None
                
                if escolha == "1":
                    novo_nome = input("Digite o novo nome: ").strip()
                    if not novo_nome:
                        print("❌ Nome não pode estar vazio!")
                        continue
                        
                elif escolha == "2":
                    try:
                        novo_valor = float(input("Digite o novo valor: R$ "))
                        if novo_valor <= 0:
                            print("❌ Valor deve ser maior que zero!")
                            continue
                    except ValueError:
                        print("❌ Valor inválido!")
                        continue
                        
                elif escolha == "3":
                    nova_categoria = input("Digite a nova categoria: ").strip()
                    if not nova_categoria:
                        print("❌ Categoria não pode estar vazia!")
                        continue
                        
                elif escolha == "4":
                    novo_nome = input("Digite o novo nome: ").strip()
                    nova_categoria = input("Digite a nova categoria: ").strip()
                    try:
                        novo_valor = float(input("Digite o novo valor: R$ "))
                        if novo_valor <= 0:
                            print("❌ Valor deve ser maior que zero!")
                            continue
                    except ValueError:
                        print("❌ Valor inválido!")
                        continue
                else:
                    print("❌ Opção inválida!")
                    continue

                
                if atualizar_produto(id_produto, novo_nome, nova_categoria, novo_valor):
                    print("✅ Produto atualizado com sucesso!")
                else:
                    print("❌ Produto não encontrado ou erro ao atualizar!")
                    
            except ValueError:
                print("❌ ID inválido! Digite um número.")

        elif opcao == "6":  
            print("\n🍽️ REALIZAR PEDIDO")
            
            # Verificar se há produtos cadastrados
            produtos = listar_produtos()
            if not produtos:
                print("❌ Nenhum produto cadastrado! Cadastre produtos primeiro.")
                continue
            
            # Verificar se há atendentes cadastrados
            atendentes = listar_atendentes()
            if not atendentes:
                print("❌ Nenhum atendente cadastrado! Cadastre atendentes primeiro.")
                continue
            
            # Verificar se há mesas cadastradas
            mesas = listar_mesas()
            if not mesas:
                print("❌ Nenhuma mesa cadastrada! Cadastre mesas primeiro.")
                continue
            
            # Mostrar mesas livres
            mesas_livres = [m for m in mesas if not m.ocupada]
            if not mesas_livres:
                print("❌ Nenhuma mesa livre disponível!")
                continue
                
            print("\n🪑 Mesas livres:")
            for mesa in mesas_livres:
                print(f"Mesa {mesa.numero} - Capacidade: {mesa.capacidade} pessoas")
            
            try:
                numero_mesa = int(input("\nNúmero da mesa: "))
                
                # Verificar se a mesa existe e está livre
                mesa_escolhida = None
                for mesa in mesas_livres:
                    if mesa.numero == numero_mesa:
                        mesa_escolhida = mesa
                        break
                
                if not mesa_escolhida:
                    print("❌ Mesa não encontrada ou já está ocupada!")
                    continue
                
                # Mostrar atendentes
                print("\n👥 Atendentes disponíveis:")
                for atendente in atendentes:
                    print(f"ID: {atendente.id} - {atendente.nome}")
                
                id_atendente = int(input("\nID do atendente: "))
                
                # Verificar se atendente existe
                atendente_encontrado = False
                for atendente in atendentes:
                    if atendente.id == id_atendente:
                        atendente_encontrado = True
                        break
                
                if not atendente_encontrado:
                    print("❌ Atendente não encontrado!")
                    continue
                
                # Mostrar produtos disponíveis
                print("\n📋 Produtos disponíveis:")
                print(f"{'Nome':<20} {'Categoria':<15} {'Valor':<10}")
                print("-" * 50)
                for produto in produtos:
                    print(f"{produto.nome:<20} {produto.categoria:<15} R$ {produto.valor:<8.2f}")
                
                # Coletar itens do pedido
                itens_pedido = []
                print("\n🛒 Adicionar itens ao pedido:")
                
                while True:
                    nome_produto = input("Nome do produto (ou 'finalizar' para terminar): ").strip()
                    if nome_produto.lower() in ['finalizar', 'fim', 'sair']:
                        break
                    
                    # Verificar se produto existe
                    produto_encontrado = False
                    for produto in produtos:
                        if produto.nome.lower() == nome_produto.lower():
                            produto_encontrado = True
                            break
                    
                    if not produto_encontrado:
                        print("❌ Produto não encontrado! Tente novamente.")
                        continue
                    
                    try:
                        quantidade = int(input("Quantidade: "))
                        if quantidade <= 0:
                            print("❌ Quantidade deve ser maior que zero!")
                            continue
                        
                        itens_pedido.append((nome_produto, quantidade))
                        print(f"✅ {quantidade}x {nome_produto} adicionado ao pedido!")
                        
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
                    print(f"\n📋 Itens do Pedido {id_pedido}:")
                    print(f"{'Produto':<20} {'Categoria':<15} {'Qtd':<5} {'Valor Unit':<12} {'Subtotal':<10}")
                    print("-" * 70)
                    total_pedido = 0
                    for item in itens:
                        subtotal = item.calcular_subtotal()
                        total_pedido += subtotal
                        print(f"{item.nome_produto:<20} {item.categoria if hasattr(item, 'categoria') else 'N/A':<15} {item.quantidade:<5} R\$ {item.valor_unitario:<10.2f} R\$ {subtotal:<8.2f}")
                    print("-" * 70)
                    print(f"{'TOTAL DO PEDIDO:':<50} R\$ {total_pedido:<8.2f}")
                else:
                    print("❌ Nenhum item encontrado para este pedido.")
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
            print("\n💰 FECHAR MESA")
            
            # Mostrar mesas ocupadas
            mesas = listar_mesas()
            mesas_ocupadas = [m for m in mesas if m.ocupada]
            
            if not mesas_ocupadas:
                print("❌ Nenhuma mesa ocupada para fechar!")
                continue
            
            print("\n🪑 Mesas ocupadas:")
            for mesa in mesas_ocupadas:
                print(f"Mesa {mesa.numero} - Capacidade: {mesa.capacidade} pessoas")
            
            try:
                numero_mesa = int(input("\nNúmero da mesa para fechar: "))
                
                # Verificar se a mesa está realmente ocupada
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
            print("\n📈 RELATÓRIO DE VENDAS")
            relatorio = relatorio_vendas()
            if relatorio:
                print("✅ Relatório gerado com sucesso!")
            else:
                print("❌ Erro ao gerar relatório.")

        elif opcao == "14":  
            print("\n📊 RELATÓRIO DETALHADO")
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
    print("🍽️ Bem-vindo ao Sistema de Gerenciamento do Restaurante!")
    main()