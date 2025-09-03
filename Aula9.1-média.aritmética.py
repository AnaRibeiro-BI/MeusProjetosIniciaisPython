def cabecalho():
    print("\n --------------------- Relatório Final ---------------------")
    print(f"{'Nome': <15}{'N1':<8}{'N2':<8}{'N3':<8}{'N4':<8}{'Média':<8}{'Situação'}")
    print("-" * 55)

Relatório = []
# cria uma lista vazia chamada relatório que será utilizada depois de ser definido a média, a nota e o nome do aluno

while True:
    Nome = input("Qual o nome do aluno: (ou digite 'sair' para encerrar): ")
    if Nome.lower() == 'sair': 
        break

    notas = [] 
    # cria uma lista vazia de notas para cada aluno informado no nome
    for nota in range(1,5): 
     # Limita o while com range de 4 alunos
        nota = float(input(f"Digite a {nota} nota de {Nome}: "))
# aqui o código entende que cada nota de cada aluno será individualmente informado
        notas.append(nota)

# def Média(n1, n2, n3, n4):
#     return (n1 + n2 + n3 + n4) / 4            => não é possível utilizar esse método porque não definimos as variáveis N1, N2, N3 e N4 nesse código. 
# Mas é possível utilizar esse método se definir essas variáveis.
    def Média(notas):
        return sum(notas) / len(notas)
# Aqui define-se a função Média de forma que irá utilizar a soma de cada nota dividido pela quantidade de notas informadas.
    
    m = Média(notas)
    Situação = "Aprovado" if m <= 6 else "Reprovado"

    Relatório.append([Nome, notas[0], notas[1], notas[2], notas[3], round(m,2), Situação])

cabecalho()
for Nome in Relatório: 
    print(f"{Nome[0]: <15}{Nome[1]: <8}{Nome[2]:<8}{Nome[3]: <8}{Nome[4]:<8}{Nome[5]: <10}{Nome[6]}")
# o <15 e <10 define o tamanho da tabela a exibir os títulos, nesse caso será de 15mm e 10mm -> é como se estivéssemos ajustando a tabela no excel.