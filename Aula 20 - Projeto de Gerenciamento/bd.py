import sqlite3

def criar_conexao():
    try:
        conexao = sqlite3.connect("restaurante.db")
        return conexao
    except sqlite3.Error as erro:
        print(f"🚫 Erro ao conectar com o banco: {erro}")
        return None

def criar_tabelas(): # cria todas as tabelas necessárias
    conexao = criar_conexao()
    if not conexao:
        print("❌ Não foi possível estabelecer conexão com o banco de dados.")
        return False

    cursor = conexao.cursor()

    try:
        print("🔄 Tentando criar/verificar tabelas...")

        # Tabela produtos 
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE,
                    valor REAL NOT NULL
                )
            """)
        print("✅ Tabela PRODUTOS criada com sucesso.")

        # Tabela atendentes 
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS atendentes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE
                )
            """)
        print("✅ Tabela ATENDERS criada com sucesso.")

        # Tabela mesas 
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS mesas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero INTEGER NOT NULL UNIQUE,
                    capacidade INTEGER NOT NULL,
                    ocupada BOOLEAN DEFAULT FALSE,
                    id_pedido_atual INTEGER DEFAULT NULL
                )
            """)
        print("✅ Tabela mesas criadacom sucesso.")

        # Tabela pedidos (referencia atendentes e mesas)
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS pedidos (
                    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_hora_abertura TIMESTAMP NOT NULL,
                    data_hora_fechamento TIMESTAMP DEFAULT NULL,
                    status TEXT NOT NULL,
                    id_atendente INTEGER NOT NULL,
                    numero_mesa INTEGER NOT NULL,
                    valor_total REAL DEFAULT 0.0,
                    FOREIGN KEY (id_atendente) REFERENCES atendentes (id),
                    FOREIGN KEY (numero_mesa) REFERENCES mesas (numero)
                )
            """)
        print("✅ Tabela PEDIDOS criada com sucesso.")

        # Tabela itens_pedido (referencia pedidos e produtos)
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS itens_pedido (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_pedido INTEGER NOT NULL,
                    id_produto INTEGER NOT NULL,
                    quantidade INTEGER NOT NULL,
                    valor_unitario REAL NOT NULL,
                    FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
                    FOREIGN KEY (id_produto) REFERENCES produtos (id)
                )
            """)
        print("✅ Tabela ITENS PEDIDO criada criada com sucesso.")


        conexao.commit()
        print("✅ Todas as tabelas foram verificadas e criadas com sucesso!")
        return True
    except sqlite3.Error as erro:
        print(f"🚫 Erro ao criar tabelas: {erro}")
        conexao.rollback() # Em caso de erro, desfaz as alterações
        return False
    finally:
        if conexao:
            conexao.close()