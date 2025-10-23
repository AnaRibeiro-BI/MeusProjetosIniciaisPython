import sqlite3

# Conexão com o banco
conexao = sqlite3.connect("restaurante.db")

# Função para criar a tabela produtos
def tabela_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_produto TEXT NOT NULL,
            valor_unitario_produto REAL NOT NULL
        );
    """)
    conexao.commit()

# Função para criar a tabela atendentes
def tabela_atendentes(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atendentes (
            id_atendente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_atendente TEXT NOT NULL
        );
    """)
    conexao.commit()

# Função para criar a tabela mesas
def tabela_mesas(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mesas (
            id_mesa INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_mesa INTEGER NOT NULL,
            capacidade_mesa INTEGER,
            status_mesa TEXT
        );
    """)
    conexao.commit()

# Função para criar a tabela pedidos
def tabela_pedidos(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora_abertura DATETIME,
            data_hora_fechamento DATETIME,
            status_pedido TEXT,
            id_atendente INTEGER,
            valor_total REAL,
            forma_pagamento TEXT,
            id_mesa INTEGER,
            FOREIGN KEY (id_atendente) REFERENCES atendentes(id_atendente),
            FOREIGN KEY (id_mesa) REFERENCES mesas(id_mesa)
        );
    """)
    conexao.commit()

# Função para criar a tabela itens_pedido
def tabela_itens_pedido(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_pedido (
            id_item INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pedido INTEGER,
            id_produto INTEGER,
            quantidade_item INTEGER,
            valor_unitario_item REAL,
            valor_total_item REAL,
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
        );
    """)
    conexao.commit()

# Função para criar tabela em formato de lista (Python)
def criar_tabela(dados, colunas):
    tabela = []
    tabela.append(colunas)
    for linha in dados:
        tabela.append(linha)
    return tabela

# Criar todas as tabelas
tabela_produtos(conexao)
tabela_atendentes(conexao)
tabela_mesas(conexao)
tabela_pedidos(conexao)
tabela_itens_pedido(conexao)

conexao.close()
