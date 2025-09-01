# def div(i,j):
#     # função def de nome div que é uma divisão. Os parâmetros foram definidos em i e j, que são variáveis a serem declaradas posteriormente
#     if j==0:
#         print("O valor de j nunca pode ser igual a zero")
#     else:
#         return i/j

# if __name__ == '__main__':

#     i=float(input("Digite o primeiro número: "))
#     j=float(input("Digite o segundo número: "))

#     r=div(i,j)
#     print(f"A divisão de {i} por {j} é {r:.2f}")

# --------------------------------------------- Exercício 1
# Calculadora de Média - Criar uma função media(n1, n2)
def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

nomealuno = input("Qual o nome do aluno: ")

if __name__ == '__main__':

    n1=float(input("Digite a nota da N1: "))
    n2=float(input("Digite a nota da n2: "))
    n3=float(input("Digite a nota da n3: "))
    n4=float(input("Digite a nota da n4: "))

    r=media(n1, n2, n3, n4)
    print(f"A média do(a) aluno(a) {nomealuno} foi de {r:.2f} e suas notas foram  {n1}, {n2}, {n3} e {n4}")

# -------------------------------------------- Exercício 2