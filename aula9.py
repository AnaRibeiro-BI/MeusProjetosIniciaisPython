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
# def media(n1, n2, n3, n4):
#     return (n1 + n2 + n3 + n4) / 4

# nomealuno = input("Qual o nome do aluno: ")

# if __name__ == '__main__':

#     n1=float(input("Digite a nota da N1: "))
#     n2=float(input("Digite a nota da n2: "))
#     n3=float(input("Digite a nota da n3: "))
#     n4=float(input("Digite a nota da n4: "))

#     r=media(n1, n2, n3, n4)
#     print(f"A média do(a) aluno(a) {nomealuno} foi de {r:.2f} e suas notas foram  {n1}, {n2}, {n3} e {n4}")

# -------------------------------------------- Exercício 2
# Mensagem Personalizada - Crie uma função mensagem_personalizada(nome, curso) que imprima "Olá, [nome]" Bem vindo ao curso de [curso]."
# def mensagem_personalizada(nome, curso):
#     return 
# print("Oi, {nome}! Seja bem vindo ao curso de {curso}")

# nome = input("Digite o nome do aluno: ")
# curso = input("Digite o curso do aluno: ")

# if __name__ == '__main__': 
#     print(f"Oi, {nome}! Seja bem vindo ao curso de {curso}!")

# -------------------------------------------- Exercício 3
# Criando funções úteis

    # cálculo de área de retângulo (base*altura)
# def area_retangulo(b,h):
#     return (b * h)
# b = float(input("Digite a base do retângulo: "))
# h = float(input("Digite a altura do retângulo: "))
# r = b * h

# if __name__ == '__main__': 
#     print(f"A área do seu retângulo é de {r}")

    # função para converter Celsius para Fahrenheit
# def conversor_temp(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input("Digite a temperatura em Celsius: "))
# r = (celsius * 9/5) + 32

# if __name__ == '__main__': 
#     print(f"A temperatura em Fahreheit é de {r}.")

    # função de saudação baseada no horário
# def saudacao_horario(nome, hora):
#     if 5<= hora < 12: 
#         return (f"Boa tarde, {nome}!")
#     elif 12<= hora < 18:
#         return (f"Boa noite, {nome}!")
#     else: 
#         return ("Horário inválido.")

# nome = input("Digite o seu nome: ")
# hora = int(input("Digite apenas a hora: "))
# msg = ({saudacao_horario}, {nome})

# if __name__ == '__main__': 
    # print(f"{msg}")      está com erro. continuar
