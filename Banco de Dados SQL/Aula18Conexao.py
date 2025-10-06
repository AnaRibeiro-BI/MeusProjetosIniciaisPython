import sqlite3

conexao = sqlite3.connect("banco_teste.db") #conecta com sql
cursor = conexao.cursor() #cria o cursor para executar os comandos no SQL
print("Conexão com o banco de dados 'banco_teste.db' estabelecida com sucesso!")

# CONSULTAR E MOSTRAR RESULTADOS ESPECÍFICOS
cursor.execute("SELECT nome, email FROM clientes;")

# CONSULTAR E MOSTRAR TODOS OS RESULTADOS NA TABELA
cursor.execute("SELECT * FROM clientes;")

resultados = cursor.fetchall()  # Pega todos os resultados da consulta

print("\n Lista de nomes e emails dos clientes cadastrados:\n") 
for linha in resultados:
    print(f"Nome: {linha[1]:<18} | Email: {linha[2]:<25}") # Formatação da tabela para alinhamento
