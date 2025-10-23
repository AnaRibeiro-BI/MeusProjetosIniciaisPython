from functions import *
from tabela import *
from bd import *

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
    print("10. Abrir Mesa")
    print("11. Listar Mesas")
    print("12. Fechar Mesa")
    print("13. Relatório de Vendas")
    print("0. Sair")
    return input("Escolha uma opção: ")

# Loop principal do sistema
def main():
    con = conection()  # conexão 
    while True: # inicia o loop para o menu
        opcao = menu() # define a variável opcao para chmar o menu

        if opcao == "0": # Sair do sistema
            print("Finalizando o Sistema. Até mais!")
            break

        elif opcao == "1": # 1 - Cadastrar Produto
            nome = input("Nome: ")
            valor = float(input("Valor: R$"))
            inserir_produto(con, nome, valor)
            print("✅ Produto cadastrado com sucesso!")

        elif opcao == "2": # 2 - Buscar Produto
            nome = input("Digite o nome do produto que deseja buscar: ")
            resultados = buscar_produto(con, nome)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("🚫 Produto não encontrado.")

        elif opcao == "3": # 3 - Listar Produtos
            produtos = listar_produtos(con)
            if produtos:
                for produto in produtos:
                    print(produto)
            else:
                print("🚫 Nenhum produto cadastrado.")

        elif opcao == "4": # 4 - Remover Produto
            nome_produto = input("Digite o nome do produto que deseja remover: ")
            sucesso = remover_produto(con, nome_produto)
            if sucesso:
                print("✅ Produto removido com sucesso!")
            else:
                print("🚫 Produto não encontrado.")

        elif opcao == "5": # 5 - Atualizar Produto
            nome_atual = input("Digite o nome do produto que deseja atualizar: ")
            print("O que deseja atualizar?")
            print("1 - Nome do produto")
            print("2 - Valor do produto")
            print("3 - Nome e valor do produto")
            escolha = input("Digite a opção (1/2/3): ")
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

            if escolha in ["1", "2", "3"]:
                sucesso = atualizar_produto(con, nome_atual, novo_nome, novo_valor)
                if sucesso:
                    print("✅ Produto atualizado com sucesso!")
                else:
                    print("🚫 Produto não encontrado ou erro ao atualizar!")

        elif opcao == "6": # 6 - Realizar Pedido
            produtos = listar_produtos(con)
            mesas = listar_mesas(con)
            id_mesa = int(input("Número da mesa: "))
            atendentes = listar_atendentes(con)
            id_atendente = int(input("ID do atendente: "))
            itens_pedido = []
            while True:
                nome_produto = input("Nome do produto (ou 'sair' para finalizar): ")
                if nome_produto.lower() == "sair":
                    break
                quantidade = int(input("Quantidade: "))
                itens_pedido.append((nome_produto, quantidade))

            sucesso = realizar_pedido(con, id_mesa, id_atendente, itens_pedido)
            if sucesso:
                print("✅ Pedido realizado com sucesso!")
            else:
                print("🚫 Erro ao realizar o pedido.")

        elif opcao == "7": # 7 - Listar Itens do Pedido
            id_pedido = int(input("ID do pedido: "))
            itens = listar_itens_pedido(con, id_pedido)
            if itens:
                for item in itens:
                    print(item)
            else:
                print("🚫 Nenhum item encontrado para este pedido.")

        elif opcao == "8": # 8 - Cadastrar Atendente
            nome_atendente = input("Nome do atendente: ")
            sucesso = cadastrar_atendente(con, nome_atendente)
            if sucesso:
                print("✅ Atendente cadastrado com sucesso!")
            else:
                print("🚫 Erro ao cadastrar atendente.")

        elif opcao == "9": # 9 - Listar Atendentes
            atendentes = listar_atendentes(con)
            if atendentes:
                for atendente in atendentes:
                    print(atendente)
            else:
                print("🚫 Nenhum atendente cadastrado.")

        elif opcao == "10": # 10 - Abrir Mesa
            numero_mesa = int(input("Número da mesa: "))
            sucesso = abrir_mesa(con, numero_mesa)
            if sucesso:
                print("✅ Mesa aberta com sucesso!")
            else:
                print("🚫 Erro ao abrir mesa.")

        elif opcao == "11": # 11 - Listar Mesas
            mesas = listar_mesas(con)
            if mesas:
                for mesa in mesas:
                    print(mesa)
            else:
                print("🚫 Nenhuma mesa cadastrada.")

        elif opcao == "12": # 12 - Fechar Mesa
            numero_mesa = int(input("Número da mesa: "))
            sucesso = fechar_mesa(con, numero_mesa)
            if sucesso:
                print("✅ Mesa fechada com sucesso!")
            else:
                print("🚫 Erro ao fechar mesa.")

        elif opcao == "13": # 13 - Relatório de Vendas
            print("1 - Relatório Simples")
            print("2 - Relatório Detalhado")
            escolha_relatorio = input("Digite a opção (1/2): ")
            if escolha_relatorio == "1":
                print(relatorio_vendas(con))
            elif escolha_relatorio == "2":
                print(relatorio_vendas_detalhado(con))
            else:
                print("🚫 Opção inválida!")

        else:
            print("🚫 Opção inválida! Tente novamente.")

    con.close() # Fechar conexão ao sair

# Executar o sistema
# if __name__ == "__main__":
#     main()