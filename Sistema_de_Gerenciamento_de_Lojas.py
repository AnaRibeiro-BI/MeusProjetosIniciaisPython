# Sistema de Gerenciamento de Loja
# produtos = []
# while True:
#     print("\n ----- MENU -----")
#     print("Digite a opção desejada abaixo:")
#     print("Opção 1 - Cdastrar Produto")
#     print("Opção 2 - Listar Produtos")
#     print("Opção 3 - Buscar Produtos")
#     print("Opção 4 - Calcular total da compra")
#     print("Opção 5 - Exibir Categorias únicas")
#     print("Opção 6 - Sair")
    
#     opção = input("Escolha uma opção: ")
    
#     if opção == "1": 
#         nome = input("Nome do Produto: ")
#         preço = input("Preço do Produto: ")
#         categoria = input("Categoria do Produto: ")
#         if preço.strip() != "" and nome.strip() != "":
#             # .strip para remover espaços em branco, tabulações, quebras de linha e outros caracteres específicos do início e do fim de uma string, retornando uma nova string sem esses caracteres
#             produtos.append({"nome": nome, "preço": float(preço), "categoria": categoria})
#         print("Produto cadastrado com sucesso!")
#     else: 
#             print("Dados inválidos, tente novamente.")
            
#             elif opção == "2":
#             if produtos: 
#                 print("\n 📦 Produtos Cadastrados:")
#                 for p in produtos:
#                     print(f"{p['nome']} - R${p['preço']} - {p['categoria']}")
#             else: 
#                 print("Nenhum produto cadastrado.")
    
#             elif opção == "3":
#             if produtos:
#                 busca = input("Digite o nome do produto cadastrado: ")
#             Encontrado = False
#             for p in produtos: 
#                 if p['nome'].lower() == busca.lower():
#                     print("Encontrado: {p['nome']} - R${p['preço']} - {p['categoria']}")
#                     Encontrado = True
#                     break
#             if not Encontrado:
#                 print("Produto não encontrado.")
#             else: 
#                 print("Nenhum produto cadastrado ainda.")

#             elif opção == "4":
#             if produtos:
#                 total = 0
#                 itens_comprados = []
#                 print("\n🛒 CALCULADORA DE COMPRAS")                    # lista para rastrear itens
#                 item = input("Digite o produto (ou'fim' para encerrar): ")
#                 while True:
#                     item = input("Produto").strip()
#                     if item.lower() == "fim":
#                         break
#                 produto_encontrado = False
#                 for p in produtos: 
#                     if p["nome"].lower() == item.lower() :
#                         total += p["preço"]
#                         itens_comprados.append(p["nome"])
#                         print(f"✅ {p['nome']} adicionado - R\${p['preço']:.2f}")
#                         produto_encontrado = True
#                         break

#                         if not produto_encontrado:
#                     print(f"❌ Produto '{item}' não encontrado.")

#                     if total > 100: 
#                         print(f"\nDesconto de 10% aplicado! (compra acima de R\$100)")
#                         total *= 0.9                    #  aplicar 10% de desconto
                
#                 print(f"\n📋 RESUMO DA COMPRA:")
#                 print(f"Itens: {', '.join(itens_comprados)}")
#                 print(f"💰 Total da compra: R\${total:.2f}")
            
#             else:
#                 print("Nenhum produto cadastrado ainda.")

#             elif opção == "5":
#             if produtos:
#                 categorias = set()  # Usa set para evitar duplicatas
#             for p in produtos:
#                 categorias.add(p['categoria'])
            
#             print("\n�� CATEGORIAS ÚNICAS:")
#             for categoria in sorted(categorias):
#                 print(f"• {categoria}")
#             else:
#                 print("Nenhum produto cadastrado ainda.")
    
#             elif opção == "6":
#             print("Saindo... Até logo! 👋")
#             break
    
#     else:
#     print("Opção inválida! Tente novamente.")
produtos = []
# Cria a lista chamada produtos
while True:
    print("\n ----- MENU -----")
    print("Digite a opção desejada abaixo:")
    print("Opção 1 - Cadastrar Produto")
    print("Opção 2 - Listar Produtos")
    print("Opção 3 - Buscar Produtos")
    print("Opção 4 - Calcular total da compra")
    print("Opção 5 - Exibir Categorias únicas")
    print("Opção 6 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1": 
        nome = input("Nome do Produto: ")
        preco = input("Preço do Produto: ")
        categoria = input("Categoria do Produto: ")
        
        if preco.strip() != "" and nome.strip() != "":
 # .strip para remover espaços em branco, tabulações, quebras de linha e outros caracteres específicos do início e do fim de uma string, retornando uma nova string sem esses caracteres
            try:
#  A instrução try em Python serve para executar um bloco de código que pode gerar um erro (uma exceção) sem interromper o programa. Ela é utilizada em conjunto com a instrução except, que define o que deve ser feito quando o erro acontece, permitindo um tratamento de erros adequado, mantendo o programa em execução e apresentando mensagens informativas em vez de paragens abruptas
                preco_float = float(preco)
                produtos.append({ "nome": nome, "preco": preco_float, "categoria": categoria})
                print("Produto cadastrado com sucesso! ✅")
            except ValueError:
# .except utilizado em conjunto com .try para, caso exista algum erro no bloco
                print("Preço inválido! Digite apenas números. ❌")
        else: 
            print("Dados inválidos, tente novamente. ❌")
    
    elif opcao == "2":
        if produtos: 
            print("\n📦 Produtos Cadastrados:")
            for p in produtos:
                print(f"{p['nome']} - R\${p['preco']:.2f} - {p['categoria']}")
        else: 
            print("Nenhum produto cadastrado ainda.")
    
    elif opcao == "3":
        if produtos:
            busca = input("Digite o nome do produto cadastrado: ")
            encontrado = False
# A variável encontrado = False é como uma "memória" que lembra se achamos o que estávamos procurando. É chamada de FLAG ou variável de controle
# A ORDEM da variavel encontrado = False importa? Tecnicamente, NÃO importa para o funcionamento básico, MAS importa para boas práticas e clareza do código
            for p in produtos: 
                if p['nome'].lower() == busca.lower():
                    print(f"Encontrado: {p['nome']} - R\${p['preco']:.2f} - {p['categoria']}")
                    encontrado = True
                    break
                    
            if not encontrado:
                print("Produto não encontrado.")
        else:
            print("Nenhum produto cadastrado ainda.")

    elif opcao == "4":
        if produtos:
            total = 0
            itens_comprados = []
            
            print("\n🛒 CALCULADORA DE COMPRAS")
            print("Digite os produtos que deseja comprar (ou 'fim' para encerrar):")
            
            while True:
                item = input("Produto: ").strip()
                
                if item.lower() == "fim":
                    break
                
                produto_encontrado = False
                for p in produtos: 
                    if p["nome"].lower() == item.lower():
                        total += p["preco"]
                        itens_comprados.append(p["nome"])
                        print(f"✅ {p['nome']} adicionado - R\${p['preco']:.2f}")
                        produto_encontrado = True
                        break
                
                if not produto_encontrado:
                    print(f"❌ Produto '{item}' não encontrado.")
            
            if total > 100: 
                print(f"\n🎉 Desconto de 10% aplicado! (compra acima de R\$100)")
                total *= 0.9
            
            print(f"\n📋 RESUMO DA COMPRA:")
            if itens_comprados:
                print(f"Itens: {', '.join(itens_comprados)}")
                print(f"💰 Total da compra: R\${total:.2f}")
            else:
                print("Nenhum item foi comprado.")
                
        else:
            print("Nenhum produto cadastrado ainda.")
    
    elif opcao == "5":
        if produtos:
            categorias = set()
            for p in produtos:
                categorias.add(p['categoria'])
            
            print("\n🏷️ CATEGORIAS ÚNICAS:")
            for categoria in sorted(categorias):
                print(f"• {categoria}")
        else:
            print("Nenhum produto cadastrado ainda.")
    
    elif opcao == "6":
        print("Saindo... Até logo! 👋")
        break
    
    else:
        print("Opção inválida! Tente novamente.")