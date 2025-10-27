import bd # Importa o módulo bd

class Produto:
    def __init__(self, id, nome, valor):
        self.id = id
        self.nome = nome
        self.valor = valor

class Item:
    def __init__(self, id_item, id_pedido, id_produto, quantidade):
        self.id_item = id_item
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, id_pedido, id_mesa, id_atendente, status):
        self.id_pedido = id_pedido
        self.id_mesa = id_mesa
        self.id_atendente = id_atendente
        self.status = status

def cadastar_produto(nome, valor):
    conexao = None
    try:
        conexao = bd.conectar_db()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, valor) VALUES (?, ?)", (nome, valor))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
        return False
    finally:
        if conexao:
            conexao.close()
        
def buscar_produto(nome):
    conexao = None
    try:
        conexao = bd.conectar_db()
        cursor = conexao.cursor()
        # Usar LIKE para buscar nomes parciais
        cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", (f'%{nome}%',))
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Erro ao buscar: {e}")
        return[]
    finally:
        if conexao:
            conexao.close()

def listar_produto():
    conexao = None
    try:
        conexao = bd.conectar_db()
        cursor = conexao.cursor()
        cursor.execute("Select * FROM produtos")
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Erro ao listar: {e}")
    finally:
        if conexao:
            conexao.close()

def remover_produto(id):
    conexao = None
    try:
        conexao = bd.conectar_db()
        cursor =  conexao.cursor()
        cursor.execute("DELETE FROM produtos  WHERE id = ?", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            print(f"✅ Produto com ID '{id}' removido com sucesso!")
        else:
            print(f"🚫 Nenhum produto encontrado com ID '{id}'.")
        return True
    except Exception as e:
        print(f"Erro ao remover: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def listar_itens_pedido(id_pedido):
    conexao = None
    try:
        conexao = bd.conectar_db()
        cursor = conexao.cursor()
        sql = """SELECT i.id_item, p.nome, i.quantidade, p.valor, (i.quantidade * p.valor) AS valor_total_item
        FROM itens i 
        JOIN produtos p ON i.id_produto = p.id WHERE i.id_pedido = ?"""

        cursor.execute(sql, (id_pedido,))
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Erro ao listar itens: {e}")
        return []
    finally:
        if conexao: 
            conexao.close

