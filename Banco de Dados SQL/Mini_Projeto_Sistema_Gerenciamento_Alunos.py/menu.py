
from aluno import *
from function import *
from banco import *

def menu():
    while True:
        print("\n+----------------------+")
        print("|     === MENU ===     |")
        print("+----------------------+")
        print("| 1 - Cadastrar Aluno  |")
        print("| 2 - Listar Alunos    |")
        print("| 3 - Alterar Aluno     |")
        print("| 4 - Deletar Aluno    |")
        print("| 5 - Buscar Aluno    |")
        print("| 0 - Sair             |")
        print("+----------------------+")
        
        opcao = input("| Escolha uma opção:   |")
        

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            aluno = Aluno(nome, idade)
            inserir_aluno(conection(), aluno)
            print("✅ Aluno cadastrado!")

        elif opcao == "2":
            alunos = listar_alunos(conection())
            for a in alunos:
                print(a)
        
        elif opcao == "3": #alterar
            nome = input("Nome do aluno para editar: " )
            if alterar_aluno(conection(), nome):
                print ("Aluno editado com sucesso!" )
            else :
                print ("Aluno não encontrado." )
        
        elif opcao == "4": #deletar
            nome = input("Nome do aluno para deletar: " )
            if deletar_aluno(conection(), nome):
                print ("Aluno removido com sucesso!" )
            else :
                print ("Aluno não encontrado." )

        elif opcao == "5":
            nome = input("Nome do aluno: ")
            resultados = buscar_aluno(conection(), nome)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("Nenhum aluno encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")