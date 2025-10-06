import sqlite3
# CONEXÃO COM O BANCO DE DADOS

conexao = sqlite3.connect("banco_teste.db")
cursor = conexao.cursor()

# CONSULTAR E MOSTRAR RESULTADOS ESPECÍFICOS COM ORDER BY
# cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;") # Ordenar do maior para o menor (decrescente)
# cursor.execute("SELECT * FROM clientes ORDER BY nome ASC;") # Ordenar do menor para o maior (crescente)

# utilizando limit para limitar a quantidade de resultados
# cursor.execute("SELECT * FROM clientes ORDER BY id DESC LIMIT 3;")
cursor.execute("SELECT * FROM clientes ORDER BY id ASC LIMIT 3;") 


resultados = cursor.fetchall()  # Pega todos os resultados da consulta


print("\n Lista de clientes cadastrados ordenados do maior para o menor ID:\n")
for linha in resultados:
    print(linha) # Mostra os resultados da consulta