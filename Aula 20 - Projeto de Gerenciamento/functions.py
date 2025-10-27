# Funções para manipulação dos dados no banco de dados SQLite para o Sistema de Gerenciamento do Restaurante
from bd import criar_conexao
from classes import *
from datetime import datetime


def cadastrar_produto(nome, valor, categoria):  # Cadastra um novo produto no banco de dados
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:  # try/except/finally para tratamento de erros
        cursor = conexao.cursor() 
        cursor.execute(
            "INSERT INTO produtos (nome, valor, categoria) VALUES (?, ?, ?)", 
            (nome, valor, categoria)
        )
        conexao.commit()
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
        return True
    except Exception as e:
        print(f"🚫 Erro ao cadastrar produto: {e}")
        return False
    finally:
        conexao.close()  

def buscar_produto(nome): # Busca um produto pelo nome
    conexao = criar_conexao()
    if not conexao:
        return None  # Retorna None se não encontrar o produto
    
    try:
        cursor = conexao.cursor()  
        cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,)) #busca pelo nome do produto
        resultado = cursor.fetchone()
        if resultado:
            produto = Produto(resultado[0], resultado[1], resultado[3], resultado[2])  
            return produto
        return None  
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
        return None
    finally:
        conexao.close()  

def listar_produtos(): # Lista todos os produtos cadastrados
    conexao = criar_conexao()
    if not conexao:
        return []
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()
        produtos = []
        
        for resultado in resultados:
            produto = Produto(resultado[0], resultado[1], resultado[3], resultado[2])  
            produtos.append(produto)
        
        return produtos 
    except Exception as e:
        print(f" Erro ao listar produtos: {e}")
        return []
    finally:
        conexao.close()  

def remover_produto(nome): # Remove um produto pelo nome
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
        
        if cursor.rowcount > 0:
            conexao.commit()
            print("✅ Produto removido com sucesso!")
            return True
        else:
            print("🚫 Produto não encontrado!")
            return False
    except Exception as erro:
        print(f"🚫 Erro ao remover produto: {erro}")
        return False  
    finally:
        conexao.close()  

def atualizar_produto(nome, novo_nome=None, nova_categoria=None, novo_valor=None): # Atualiza um produto existente
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:
        cursor = conexao.cursor()
        
        # Buscar produto atual
        cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome))
        produto_atual = cursor.fetchone()
        
        if not produto_atual:
            print("🚫 Produto não encontrado!")
            return False
        
        # Usar valores atuais se novos valores não foram fornecidos
        nome = novo_nome if novo_nome else produto_atual[1]
        valor = novo_valor if novo_valor else produto_atual[2] 
        categoria = nova_categoria if nova_categoria else produto_atual[3]
        
        cursor.execute(
            "UPDATE produtos SET nome = ?, valor = ?, categoria = ? WHERE id = ?",  
            (nome, valor, categoria, id_produto)
        )
        
        conexao.commit()
        print("✅ Produto atualizado com sucesso!")
        return True
    except Exception as erro:
        print(f"🚫 Erro ao atualizar produto: {erro}")
        return False
    finally:
        conexao.close()

def cadastrar_atendente(nome): # Cadastra um novo atendente
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO atendentes (nome) VALUES (?)", (nome,))
        conexao.commit()
        print(f"✅ Atendente '{nome}' cadastrado com sucesso!")
        return True
    except Exception as erro:
        print(f"🚫 Erro ao cadastrar atendente: {erro}")
        return False
    finally:
        conexao.close()

def listar_atendentes(): # Lista todos os atendentes
    conexao = criar_conexao()
    if not conexao:
        return []
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM atendentes")
        resultados = cursor.fetchall()
        atendentes = []
        
        for resultado in resultados:
            atendente = Atendente(resultado[0], resultado[1], True)  # id, nome, ativo=True por padrão
            atendentes.append(atendente)
        
        return atendentes
    except Exception as erro:
        print(f"🚫 Erro ao listar atendentes: {erro}")
        return []
    finally:
        conexao.close()

def cadastrar_mesa(numero, capacidade): # Cadastra uma nova mesa
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:
        cursor = conexao.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER UNIQUE,
                capacidade INTEGER,
                ocupada BOOLEAN DEFAULT FALSE,
                id_pedido_atual INTEGER DEFAULT NULL
            )
        """)
        
        cursor.execute(
            "INSERT INTO mesas (numero, capacidade, ocupada) VALUES (?, ?, ?)",
            (numero, capacidade, False) # False = presume que já existe a mesa e que ela está livre
        )
        conexao.commit()
        print(f"✅ Mesa {numero} cadastrada com sucesso!")
        return True
    except Exception as erro:
        print(f"🚫 Erro ao cadastrar mesa: {erro}")
        return False
    finally:
        conexao.close()

def listar_mesas(): # lista todas as mesas
    conexao = criar_conexao()
    if not conexao:
        return []
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT numero, capacidade, ocupada FROM mesas")
        resultados = cursor.fetchall()
        mesas = []
        
        for resultado in resultados:
            mesa = Mesa(resultado[0], resultado[1], bool(resultado[2]))
            mesas.append(mesa)
        
        return mesas
    except Exception as erro:
        print(f" Erro ao listar mesas: {erro}")
        return []
    finally:
        conexao.close()

def realizar_pedido(numero_mesa, id_atendente, lista_itens): #  Realiza um novo pedido e lista_itens deve ser uma lista de tuplas: [('nome_produto', quantidade), ...]
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:
        cursor = conexao.cursor() 
        
        # criação da tabela itens_pedido se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER,
                id_produto INTEGER,
                quantidade INTEGER,
                valor_unitario REAL,
                FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
                FOREIGN KEY (id_produto) REFERENCES produtos (id)
            )
        """)
        
        cursor.execute(
            "INSERT INTO pedidos (id_atendente, numero_mesa, data_hora_abertura, status, valor_total) VALUES (?, ?, ?, ?, ?)",
            (id_atendente, numero_mesa, datetime.now(), "Aberto", 0.0)  
        )
        id_pedido = cursor.lastrowid
        
        valor_total = 0.0
        

        for nome_produto, quantidade in lista_itens: 
            # Buscar produto
            cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome_produto,))
            produto = cursor.fetchone()
            
            if not produto:
                print(f"🚫 Produto '{nome_produto}' não encontrado!")
                continue
            
            valor_unitario = produto[2]  # valor do produto
            subtotal = quantidade * valor_unitario
            valor_total += subtotal
            
            cursor.execute(
                "INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, valor_unitario) VALUES (?, ?, ?, ?)",
                (id_pedido, produto[0], quantidade, valor_unitario)
            )
        
        # Atualizar valor total do pedido
        cursor.execute(
            "UPDATE pedidos SET valor_total = ? WHERE id_pedido = ?", 
            (valor_total, id_pedido)
        )
        
        # Marcar mesa como ocupada
        cursor.execute(
            "UPDATE mesas SET ocupada = 1, id_pedido_atual = ? WHERE numero = ?",
            (id_pedido, numero_mesa)
        )
        
        conexao.commit()  
        print(f"✅ Pedido {id_pedido} realizado com sucesso! Total: R$ {valor_total:.2f}")
        return id_pedido
        
    except Exception as erro:
        print(f" Erro ao realizar pedido: {erro}")
        return False # Mesa começa LIVRE (não ocupada)
    finally:
        conexao.close()

def listar_itens_pedido(id_pedido): # Lista todos os itens de um pedido
    conexao = criar_conexao()
    if not conexao:
        return []
    
    try:
        cursor = conexao.cursor() 
        cursor.execute("""
            SELECT ip.quantidade, p.nome, p.categoria, ip.valor_unitario
            FROM itens_pedido ip
            JOIN produtos p ON ip.id_produto = p.id
            WHERE ip.id_pedido = ?
        """, (id_pedido,))  
        
        resultados = cursor.fetchall()
        itens = []
        
        for resultado in resultados:
            item = ItemPedido(
                id_produto=0,  
                nome_produto=resultado[1],
                quantidade=resultado[0],
                valor_unitario=resultado[3]
            )
            itens.append(item)
        
        return itens
    except Exception as erro:
        print(f"🚫 Erro ao listar itens do pedido: {erro}")
        return []
    finally:
        conexao.close()  

def fechar_mesa(numero): # Fecha o pedido associado à mesa e libera a mesa
    conexao = criar_conexao()
    if not conexao:
        return False  
    
    try:
        cursor = conexao.cursor()  
        cursor.execute("""
            SELECT m.id, m.id_pedido_atual, p.status
            FROM mesas m
            LEFT JOIN pedidos p ON m.id_pedido_atual = p.id_pedido
            WHERE m.numero = ?
        """, (numero,))
        
        resultado = cursor.fetchone()
        if not resultado:
            print(f"🚫 Mesa '{numero}' não encontrada.")
            return False
        
        
        id_mesa, id_pedido, status_pedido = resultado
        
        if id_pedido is None:
            print(f"🚫 A mesa '{numero}' não possui pedido associado para fechar.")
            return False

       
        cursor.execute("""
            SELECT SUM(ip.quantidade * ip.valor_unitario) AS total_pedido
            FROM itens_pedido ip
            WHERE ip.id_pedido = ?
        """, (id_pedido,))
        
        linha_total = cursor.fetchone()
        total_pedido = linha_total[0] if linha_total[0] else 0.0  
        cursor.execute("""
            UPDATE pedidos
            SET status = ?, data_hora_fechamento = ?, valor_total = ?
            WHERE id_pedido = ?
        """, ("Fechado", datetime.now(), total_pedido, id_pedido))
        
        # Libera a mesa
        cursor.execute("""
            UPDATE mesas
            SET ocupada = ?, id_pedido_atual = ?
            WHERE numero = ?
        """, (False, None, numero))

        conexao.commit()
        print(f"✅ Pedido da mesa '{numero}' fechado com sucesso! Valor total: R$ {total_pedido:.2f}")
        return True

    except Exception as e:
        try:
            conexao.rollback()
        except Exception:
            pass
        print(f"🚫 Erro ao fechar a mesa '{numero}': {e}") 
        return False
    finally:  # finally para garantir fechamento
        conexao.close()

def calcular_total_pedido(): # Calcula o valor total de todos os pedidos realizados no dia atual
    conexao = criar_conexao()
    if not conexao:
        return 0.0 # entende resultado como float
    
    try:
        cursor = conexao.cursor()  
        hoje = datetime.now().date()
        
        cursor.execute("""
            SELECT SUM(ip.quantidade * ip.valor_unitario) AS total_dia
            FROM pedidos p
            JOIN itens_pedido ip ON p.id_pedido = ip.id_pedido
            WHERE DATE(p.data_hora_abertura) = ?
        """, (hoje,))
        
        linha_total = cursor.fetchone()
        total_dia = linha_total[0] if linha_total[0] else 0.0
        
        print(f"💰 Total de vendas de {hoje}: R$ {total_dia:.2f}") 
        return total_dia
    except Exception as e:
        print(f"�� Erro ao calcular total: {e}")
        return 0.0
    finally:
        conexao.close()  

def relatorio_vendas(): # gera um relatório simples de vendas do dia atual
    conexao = criar_conexao()
    if not conexao:
        return {}  # ✅ CORREÇÃO 48: Retorna {} em vez de []
    
    try:
        cursor = conexao.cursor()  
        hoje = datetime.now().date()
        
        # COUNT DISTINCT para evitar duplicatas
        cursor.execute("""
            SELECT COUNT(DISTINCT p.id_pedido) AS total_pedidos,
                   SUM(ip.quantidade * ip.valor_unitario) AS valor_total_vendido
            FROM pedidos p
            JOIN itens_pedido ip ON p.id_pedido = ip.id_pedido
            WHERE DATE(p.data_hora_abertura) = ?
        """, (hoje,))
        
        resultado = cursor.fetchone()
        total_pedidos = resultado[0] if resultado[0] else 0
        valor_total_vendido = resultado[1] if resultado[1] else 0.0

        print(f"\n📊 ===== Relatório de Vendas - {hoje} =====")
        print(f"Total de pedidos: {total_pedidos}")
        print(f"Valor total vendido: R$ {valor_total_vendido:.2f}")
        print("=" * 40)
        
        return {
            "total_pedidos": total_pedidos,
            "valor_total_vendido": valor_total_vendido
        }
    except Exception as e:
        print(f"🚫 Erro ao gerar relatório: {e}")
        return {}
    finally:
        conexao.close()

def relatorio_vendas_detalhado(): # Gera um relatório detalhado de vendas do dia atual
    conexao = criar_conexao()
    if not conexao:
        return {}  
    
    try:
        cursor = conexao.cursor()  
        hoje = datetime.now().date()
        
        cursor.execute("""
            SELECT COUNT(DISTINCT p.id_pedido) AS total_pedidos,
                   SUM(ip.quantidade * ip.valor_unitario) AS valor_total_vendido
            FROM pedidos p
            JOIN itens_pedido ip ON p.id_pedido = ip.id_pedido
            WHERE DATE(p.data_hora_abertura) = ? AND p.status = 'Fechado'
        """, (hoje,))
        
        resultado = cursor.fetchone()
        total_pedidos = resultado[0] if resultado[0] else 0
        valor_total_vendido = resultado[1] if resultado[1] else 0.0

        cursor.execute("""
            SELECT 
                pr.nome AS produto,
                SUM(ip.quantidade) AS quantidade_vendida,
                SUM(ip.quantidade * ip.valor_unitario) AS valor_total
            FROM pedidos p
            JOIN itens_pedido ip ON p.id_pedido = ip.id_pedido
            JOIN produtos pr ON ip.id_produto = pr.id
            WHERE DATE(p.data_hora_abertura) = ? AND p.status = 'Fechado'
            GROUP BY pr.id
            ORDER BY quantidade_vendida DESC
        """, (hoje,))
        
        produtos_vendidos = cursor.fetchall()

        # Exibição do relatório
        print(f"\n📊 ===== Relatório Detalhado de Vendas - {hoje} =====")
        print(f"Total de pedidos fechados: {total_pedidos}")
        print(f"Valor total vendido: R$ {valor_total_vendido:.2f}\n")
        print("Produtos mais vendidos:")
        print(f"{'Produto':<25} {'Qtd Vendida':<12} {'Valor Total':<12}")
        print("-" * 50)
        
        for produto, quantidade, valor in produtos_vendidos:
            print(f"{produto:<25} {quantidade:<12} R$ {valor:<11.2f}")
        
        print("=" * 50)
        
        return {
            "total_pedidos": total_pedidos,
            "valor_total_vendido": valor_total_vendido,
            "produtos_vendidos": produtos_vendidos
        }
    except Exception as e:
        print(f" Erro ao gerar relatório detalhado: {e}")
        return {}
    finally:
        conexao.close() 