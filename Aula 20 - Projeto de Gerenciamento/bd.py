import sqlite3
import datetime

#cria o banco de dados para o restautante
conexao = sqlite3.connect("restaurante.db")

# Obtém a data e hora atuais
agora = datetime.datetime.now()

cursor = conexao.cursor()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nome TEXT, valor REAL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS itens (
               id_item INTEGER PRIMARY KEY AUTOINCREMENT,
               id_produto INTEGER, 
               quantidade INTEGER,
               valor_unitario REAL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos (
               id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, 
               data_hora_abertura TIMESTAMP,
               data_hora_fechamento TIMESTAMP,
               status TEXT,
               id_item INTEGER,
               id_atendente INTEGER,
               valor_total REAL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS atendentes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT)""") 

except sqlite3.Error as erro:
    print(f"Erro no banco: {erro}")
               
conexao.commit()
conexao.close()

               