import sqlite3

def criar_conexao():
    # Cria e retorna uma conexão com o banco de dados
    try:
        conexao = sqlite3.connect("restaurante.db")
        return conexao
    except sqlite3.Error as erro:
        print(f"🚫 Erro ao conectar com o banco: {erro}")
        return None

def criar_tabelas(): # cria todas as tabelas necessárias
    conexao = criar_conexao()
    if not conexao:
        return False

    cursor = conexao.cursor()
        # Criação das tabelas, caso ainda não existam
    

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT, 
                valor REAL
            )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens (
                id_item INTEGER PRIMARY KEY AUTOINCREMENT,
                id_produto INTEGER, 
                quantidade INTEGER,
                valor_unitario REAL
            )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, 
                data_hora_abertura TIMESTAMP,
                data_hora_fechamento TIMESTAMP,
                status TEXT,
                id_item INTEGER,
                id_atendente INTEGER,
                valor_total REAL
            )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS atendentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
        """)

    conexao.commit()
    print("✅ Banco de dados e tabelas verificados/criados com sucesso!")
    return conexao

conexao = sqlite3.connect("restaurante.db")
conexao.close()  # fechar a conexao com o banco