# import sqlite3
# #importando bilbioteca sqlite3
# banco = sqlite3.connect('primeiro_banco_de_dados.db')
# #criando o primeiro banco de dados
# cursor = banco.cursor()    #cursor é um comando específico de banco de dados o qual executa os comandos SQL
# #se não definir o cursor, não é possível executar comandos SQL
# cursor.execute("CREATE TABLE pessoas (nome TEXT, idade INTEGER, email TEXT)")
# cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES ('Maria', 40, 'maria_123@gmail.com')")
# banco.commit()
# cursor.execute('SELECT * FROM pessoas')
# print(cursor.fetchall())  #fetchall() retorna todas as linhas da tabela

# ----------------------------------------------------
# Exercício 1
# import sqlite3
# conexao = sqlite3.connect('loja.db')
# cursor = conexao.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL)")

# produtos = [
#     ('Camisa', 29.99),
#     ('Calça', 49.99),
#     ('Tênis', 89.99),
#     ('Lápis', 5.88),
#     ('Meia', 12.99),
#     ('Caderno', 10.00)
# ] # Inserindo múltiplos registros
# cursor.executemany("INSERT INTO produtos (nome, preco) VALUES (?, ?)", produtos)
# conexao.commit() # Salvando as alterações no banco de dados
# # Executando uma consulta SELECT
# cursor.execute("SELECT * FROM produtos")
# # Recuperando todos os resultados
# for linha in cursor.fetchall():
#     print(linha)
# # Ou recuperando um por um
# linha = cursor.fetchone()
# if linha:
#     print(linha)
# -----------------------------------------------------
# Exercício 2
# import sqlite3
# # Conectar ao banco de dados
# conexao = sqlite3.connect("sistema.db" )
# cursor = conexao.cursor()
# # Criar tabela de usuários
# cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, cargo TEXT)")
# # Inserir uma lista de novos usuários
# usuarios = [
#     ('Ana', 'ana.barros@go.senac.br', 'supervisora técnica'),
#     ('Rossana', 'rossana.gomes@go.senac.br', 'assessora de área'),
#     ('Camila', 'camila.alves@go.senac.br', 'assistente administrativa'),
#     ('Lionísio', 'lionisio.pereira@go.senac.br', 'gerente de operações finalísticas')
# ]
# cursor.executemany("INSERT INTO usuarios (nome, email, cargo) VALUES (?, ?, ?)", usuarios)
# conexao.commit() # Salvando as alterações no banco de dados
# # Executando uma consulta SELECT
# cursor.execute("SELECT * FROM usuarios")
# # Recuperando todos os resultados
# for linha in cursor.fetchall():
#     print(linha)
# linha = cursor.fetchone()
# if linha:
#     print(linha)
# ------------------------------------------------------
# Exercício 3
# Apaga o banco de dados, se já existir
import os
if os.path.exists("loja.db"):
    os.remove("loja.db")
# Cria um novo banco de dados e insere dados nas tabelas clientes e pedidos
import sqlite3
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")  # Habilita verificação de chave estrangeira
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT UNIQUE, telefone TEXT)")

clientes = [
    ('João Silva', 'joao.silva@gmail.com', '1234-5678'),
    ('Maria Oliveira', 'maria.oliveira@gmail.com', '9876-5432'),
    ('Pedro Santos', 'pedro.santos@gmail.com', '5555-5555'),
    ('Ana Costa', 'ana.costa@gmail.com', '4444-4444'),
    ('Lucas Lima', 'lucas.lima@gmail.com', '7777-7777')
]
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        produto TEXT,
        valor REAL,
        data TEXT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')
pedidos = [
    (1, 'Camisa', 29.99, '2023-10-01'),
    (2, 'Calça', 49.99, '2023-10-02'),
    (3, 'Tênis', 89.99, '2023-10-03'),
    (4, 'Lápis', 5.88, '2023-10-04'),
    (5, 'Meia', 12.99, '2023-10-05'),
    (6, 'Caderno', 10.00, '2023-10-06')
]
cursor.executemany("INSERT OR IGNORE INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", clientes) 
#ao invés de inserir na tabela de clientes, insere ou ignora caso o email já exista
cursor.executemany("INSERT INTO pedidos (cliente_id, produto, valor, data) VALUES (?, ?, ?, ?)", pedidos)
conexao.commit() # Salvando as alterações no banco de dados

# CONSULTA FORMATADA: CLIENTES
cursor.execute("SELECT * FROM clientes") # Executando uma consulta SELECT
resultados = cursor.fetchall() # Recuperando todos os resultados

# para a consulta aparecer como tabela 
# Cabeçalho formatado
print(f"{'ID':<4} {'Nome':<20} {'Email':<30} {'Telefone':<15}")
print("-" * 75)
# Linhas formatadas
for linha in resultados:
    id_, nome, email, telefone = linha
    print(f"{id_:<4} {nome:<20} {email:<30} {telefone:<15}")

print("\n Pedidos: ")
cursor.execute("SELECT * FROM pedidos")
resultados = cursor.fetchall()
print(f"{'ID':<4} {'Cliente ID':<12} {'Produto':<20} {'Valor':<10} {'Data':<12}")
print("-" * 75)
for linha in resultados:
    id_, cliente_id, produto, valor, data = linha
    print(f"{id_:<4} {cliente_id:<12} {produto:<20} {valor:<10} {data:<12}")