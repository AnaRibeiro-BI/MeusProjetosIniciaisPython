import sqlite3
import datetime

DB_NAME = "pj_sistema_restaurante/restaurante.db"

def conectar_db():
    # Retorna uma nova conexão com o banco de dados.
    conexao = sqlite3.connect(DB_NAME)
    return conexao

def criar_tabela():
    # Cria toda as tabelas

    conexao = None
    try:
        conexao = conectar_db()
        cursor = conexao.cursor()

        print("Criando tabelas...")

        # Tabela de produtos
        cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL UNIQUE,
                        valor REAL NOT NULL)""")
        
        # Tabela de Atendentes
        cursor.execute("""CREATE TABLE IF NOT EXISTS atendentes (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nome TEXT NOT NULL)""")
        
        #Tabela de Mesas
        cursor.execute("""CREATE TABLE IF NOT EXISTS mesas (
                       id_mesa INTEGER PRIMARY KEY AUTOINCREMENT, 
                       status TEXT NOT NULL DEFAULT 'livre')""")
        
        #Tabela de Pedidos
        cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos (
                       id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, 
                       id_mesa INTEGER NOT NULL, 
                       id_atendente INTEGER NOT NULL,
                       data_hora_abertura TIMESTAMP NOT NULL,
                       data_hora_fechamento TIMESTAMP,
                       status TEXT NOT NULL DEFAULT 'aberto',
                       valor_total REAL DEFAULT 0.0,
                       FOREIGN KEY (id_mesa) REFERENCES mesas (id_mesa),
                       FOREIGN KEY (id_atendente) REFERENCES atendentes (id))""")
        
        # Tabela de Itens
        cursor.execute("""CREATE TABLE IF NOT EXISTS itens (
                       id_item INTEGER PRIMARY KEY AUTOINCREMENT, 
                       id_pedido INTEGER NOT NULL,
                       id_produto INTEGER NOT NULL,
                       quantidade INTEGER NOT NULL,
                       FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
                       FOREIGN KEY (id_produto) REFERENCES produtos (id))""")
        
        conexao.commit()
        print("Tabelas criadas com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao criar as tabelas: {erro}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    print("Inicializando banco de dados...")
    criar_tabela()