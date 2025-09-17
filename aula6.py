# # ---------------------------- EXERCÍCIO 1 --------------------------------
# livro = {"título": "python para iniciantes",
#          "autor": "Ana Silva",
#          "ano": "2023"}
# # imprimir as informações
# print(f"título:{livro['título']}")
# # f para não precisar colocar aspas em cada palavra
# print(f"Autor:{livro['autor']}")
# print(f"ano: {livro['ano']}")

# # formato alternativo 
# print("\nInformações do Livro: ")
# # \n para pular a linha
# for chave, valor in livro.items ():
#     print(f"{chave}: {valor}")
# declara a variável chave e a variável valor -> grava as chaves do dicionário na nova variável chave, e os valores das variáveis do dicionário na variável valor
# após usa a fórmula .items() para concatenar as chaves e seus respectivos valores do dicionário livro e printar na tela

# -----------------------------EXERCÍCIO 2 --------------------------------
# Criando agenda de contatos
agenda = {"João": "(11) 99999-1111",
          "Maria": "(11) 99991-1111",
          "Pedro": "(11) 99911-1111"}

# exibindo todos os contatos
print("\nAgenda de Contatos:")
print("-" * 20) 
# no print acima é solicitado que sejam colocados 20 tracinhos (-), usando a fórmula tracinho (-) * (vezes) 20
for nome, telefone in agenda.items ():
    print(f"{nome}: {telefone}")