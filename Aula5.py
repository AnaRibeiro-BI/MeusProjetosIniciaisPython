# MODIFICANDO LISTAS
# frutas = ["maça", "banana", "laranja"]
# print(frutas)
# frutas.append("uva")
# print(frutas)
# frutas.pop(3)
# print(frutas)
# frutas.insert(3, "jaca")
# print(frutas)
# frutas.remove("banana")
# print(frutas)
# frutas[1] = "abacaxi"
# print(frutas),

# ------------------------ EXERCÍCIO 1 --------------------------
# Criando listas de animais
# animais = ["cachorro", "gato", "papagaio", "coelho", "rato"]
# print(animais)
# se eu eu quiser imprimir minha lista, também posso usar o seguinte código:
# for animal in animais:
#     print(animal)
# removendo o terceiro animal
# animais.remove("rato")
# print(animais)
# # ou
# animais.pop(3)
# print(animais)

# ------------------------EXERCÍCIO 2 --------------------
# CRIANDO LISTA VAZIA
# nomes = []
# # recebendo os nomes
# for i in range(3):
#     nome = input("Digite um nome: ")
#     nomes.append(nome)
# # Imprimindo a lista completa
# print("\nLista de Nomes:")
# print(nomes)
# # Imprimindo cada nome
# print("\nNomes na Lista: ")
# for nome in nomes:
#     print(nome)
# --------------------- EXERCÍCIO 3 ----------------------
# Organizador de mochila
# criando a lista inicial com os itens da mochila
# mochila = ["camiseta", "calça", "meia", "caderno", "estojo"]

# ----------------------- PRÁTICA SUPERVISIONADA ------------------
# Criar uma lista de notas e realizar cálculos estatísticos
notas = [7.5, 9.5, 6.5, 8, 10, 7, 6] 
# calculando a média
media = sum(notas) / len(notas)
# encontrando a maior e a menor nota
maior_nota = max(notas)
menor_nota = min(notas)
# exibindo resultados
print(f"\nMenor das notas: {media:.1f}")
print(f"\nMaior nota: {maior_nota}")
print(f"\nMenor nota: {menor_nota}")
resultado = ("Aprovado", "Recuperação", "Reprovado")
if media >= 7:
    resultado = "aprovado"
elif media >5 and media <7:
    resultado = "recuperação"
else:
    resultado = "reprovado"
print("Seu resultado é", resultado)