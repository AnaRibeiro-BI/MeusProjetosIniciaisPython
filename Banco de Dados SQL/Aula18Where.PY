import sqlite3 
# CONEXÃO COM O BANCO DE DADOS

conexão = sqlite3.connect("banco_teste.db")
cursor = conexão.cursor()

# from Aula18bd import clientes

# consulta usando Where
# idade = input("Digite a cidade que deseja buscar: ")
# cursor.execute("SELECT * FROM clientes WHERE cidade = ?", (cidade,)) # busca dentro do banco de dados o nome da cidade digitada pelo usuário


# outro exemplo com WHERE
#letra = input("Digite a letra do(s) nome(s) que deseja buscar: ")
# cursor.execute("SELECT * FROM clientes WHERE nome like ?", (letra + '%',)) # busca dentro do banco de dados o nome digitada pelo usuário
# cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'a%';") # nomes que começam com A
# a % siginifica que está iniciando com a letra escolhida

# usando operadores lógicos AND e OR para consultas
# cursor.execute("SELECT * FROM clientes WHERE cidade = 'Goiânia' AND nome LIKE 'A%';") # busca dentro do banco de dados o nome digitada pelo usuário

resultados = cursor.fetchall()  # Pega todos os resultados da consulta

print("\n Lista de clientes cadastrados:\n")
for linha in resultados: 
    print(linha) # Mostra os resultados da consulta