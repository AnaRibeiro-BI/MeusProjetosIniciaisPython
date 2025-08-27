# AULA 07 - Sistema de Gerenciamente de Loja
# Alunas:Yasmin e Ana Luyza

produtos = []
while True: 
    print("\n --- MENU ---")
    print("Opção 1 - Cadastro de Produto")
    print("Opção 2 - Listar Produto")
    print("Opção 3 - Buscar Produto")
    print("OPção 4 - Calcular o total da compra")
    print("Opção 5 - Exibir as Categorias")

    opção = input("Escolha uma opção:")

    if opção == "1":
        nome = input("Digite o nome do produto:")
        preço = float(input("Digite o preço do produto:"))
        categoria = input("Digite a categoria do produto:")
        if preço > 0 and nome != "":
           produtos.append({"nome": nome, "preço": preço, "categoria": categoria})
           print("Seu produto foi cadastrado")
        else: 
            print("Os dados não foram encontrados")

    elif opção == "2":
        for p in produtos: 
          print(f"{p['nome']} - R${p['preço']} - {p['categoria']}")
    
    elif opção == "3":
        busca= input("Digite o nome do produto: ")
        # encontrado= False 
        for p in produtos:
            if p["nome"].lower() == busca.lower():
                print (f"encontrado: {p['nome']} -R${p['preço']} -- {p['categoria']}")
            encontrado = True
        if not encontrado:
            print ("não foi possível encontrar o seu produto.")
    
    elif opção == "4":
        # total = p["preço"] 
        # while True:
        #item = input ("Digite o nome de produto desejado: ")
        ##if p ["nome"].lower() == item.lower():
        #             total = p["preço"] 
        #             total += p ["preço"] 
        #     # else:
        #     #     print ("error")
        # if total > 100:
        #        total *= 0.95
        #        if not total > 100: 
        #         print (f"O total da compra realizada é de: R$ {total: .2f}")
        total = 0
        while True: 
            item = input("Digite o nome do produto desejado [ou 'fim' para encerrar]:")
            if item.lower() == "fim":
                break 
        for p in produtos:
            if p["nome"].lower() == item.lower():
                Total += p["preço"]
                if Total > 100:
                    Total *= 0.9
        print(f"Total da compra realizada é de: R$ {Total: .2f}")
                
                
                 
        #         Total = float ({item} * p["preço"])
        # #     if total > 100:
        # #         total *= 0.95
        # # if not total > 100: 
            # print (f"O total da compra realizada é de: R$ {Total: .2f}")

         

    
        
    
   
