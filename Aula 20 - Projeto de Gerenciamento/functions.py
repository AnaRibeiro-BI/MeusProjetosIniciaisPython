# functions.py
from bd import criar_conexao
from classes import *
from datetime import datetime


# 'categoria' removido do parametro e do INSERT
def cadastrar_produto(nome, valor):
    conexao = criar_conexao()
    if not conexao:
        return False

    try:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, valor) VALUES (?, ?)",
            (nome, valor)
        )
        conexao.commit()
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
        return True
    except Exception as e:
        print(f"🚫 Erro ao cadastrar produto: {e}")
        return False
    finally:
        conexao.close()

def buscar_produto(termo_busca):
    conexao = criar_conexao()
    if not conexao:
        return None

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos WHERE LOWER(nome) LIKE ?", ('%' + termo_busca.lower() + '%',))
        resultado = cursor.fetchone()
        if resultado:
            # resultado é (id, nome, valor)
            # Produto(id, nome, valor)
            produto = Produto(resultado[0], resultado[1], resultado[2])
            return produto
        return None
    except Exception as e:
        print(f"🚫 Erro ao buscar produto: {e}")
        return None
    finally:
        conexao.close()

def listar_produtos():
    conexao = criar_conexao()
    if not conexao:
        return []

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()
        produtos = []

        for resultado in resultados:
            # resultado é (id, nome, valor)
            # Produto(id, nome, valor)
            produto = Produto(resultado[0], resultado[1], resultado[2])
            produtos.append(produto)

        return produtos
    except Exception as e:
        print(f"🚫 Erro ao listar produtos: {e}")
        return []
    finally:
        conexao.close()

def remover_produto(id_produto):
    conexao = criar_conexao()
    if not conexao:
        return False

    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

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

# 'nova_categoria' removido do parametro e do UPDATE
def atualizar_produto(id_produto, novo_nome=None, novo_valor=None):
    conexao = criar_conexao()
    if not conexao:
        return False

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
        produto_atual = cursor.fetchone() # resultado é (id, nome, valor)

        if not produto_atual:
            print("🚫 Produto não encontrado!")
            return False

        nome_final = novo_nome if novo_nome is not None else produto_atual[1]
        valor_final = novo_valor if novo_valor is not None else produto_atual[2]
        # 'categoria_final' e 'nova_categoria' removidos

        cursor.execute(
            "UPDATE produtos SET nome = ?, valor = ? WHERE id = ?",
            (nome_final, valor_final, id_produto)
        )

        conexao.commit()
        print("✅ Produto atualizado com sucesso!")
        return True
    except Exception as erro:
        print(f"�� Erro ao atualizar produto: {erro}")
        return False
    finally:
        conexao.close()

def cadastrar_atendente(nome):
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
        print(f"�� Erro ao cadastrar atendente: {erro}")
        return False
    finally:
        conexao.close()

def listar_atendentes():
    conexao = criar_conexao()
    if not conexao:
        return []

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM atendentes")
        resultados = cursor.fetchall()
        atendentes = []

        for resultado in resultados:
            atendente = Atendente(resultado[0], resultado[1], True)
            atendentes.append(atendente)

        return atendentes
    except Exception as erro:
        print(f"�� Erro ao listar atendentes: {erro}")
        return []
    finally:
        conexao.close()

def cadastrar_mesa(numero, capacidade):
    conexao = criar_conexao()
    if not conexao:
        return False

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO mesas (numero, capacidade, ocupada) VALUES (?, ?, ?)",
            (numero, capacidade, False)
        )
        conexao.commit()
        print(f"✅ Mesa {numero} cadastrada com sucesso!")
        return True
    except Exception as erro:
        print(f"🚫 Erro ao cadastrar mesa: {erro}")
        return False
    finally:
        conexao.close()

def listar_mesas():
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
        print(f"🚫 Erro ao listar mesas: {erro}")
        return []
    finally:
        conexao.close()

def realizar_pedido(numero_mesa, id_atendente, lista_itens):
    conexao = criar_conexao()
    if not conexao:
        return False

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO pedidos (id_atendente, numero_mesa, data_hora_abertura, status, valor_total) VALUES (?, ?, ?, ?, ?)",
            (id_atendente, numero_mesa, datetime.now(), "Aberto", 0.0)
        )
        id_pedido = cursor.lastrowid

        valor_total = 0.0

        for nome_produto, quantidade in lista_itens:
            cursor.execute("SELECT id, valor FROM produtos WHERE nome = ?", (nome_produto,))
            produto_info = cursor.fetchone()

            if not produto_info:
                print(f"🚫 Produto '{nome_produto}' não encontrado!")
                continue

            id_produto = produto_info[0]
            valor_unitario = produto_info[1]
            subtotal = quantidade * valor_unitario
            valor_total += subtotal

            cursor.execute(
                "INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, valor_unitario) VALUES (?, ?, ?, ?)",
                (id_pedido, id_produto, quantidade, valor_unitario)
            )

        cursor.execute(
            "UPDATE pedidos SET valor_total = ? WHERE id_pedido = ?",
            (valor_total, id_pedido)
        )

        cursor.execute(
            "UPDATE mesas SET ocupada = 1, id_pedido_atual = ? WHERE numero = ?",
            (id_pedido, numero_mesa)
        )

        conexao.commit()
        print(f"✅ Pedido {id_pedido} realizado com sucesso! Total: R$ {valor_total:.2f}")
        return id_pedido

    except Exception as erro:
        print(f"🚫 Erro ao realizar pedido: {erro}")
        return False
    finally:
        conexao.close()

def listar_itens_pedido(id_pedido):
    conexao = criar_conexao()
    if not conexao:
        return []

    try:
        cursor = conexao.cursor()
        # 'p.categoria' removido do SELECT
        cursor.execute("""
            SELECT ip.quantidade, p.nome, ip.valor_unitario, p.id
            FROM itens_pedido ip
            JOIN produtos p ON ip.id_produto = p.id
            WHERE ip.id_pedido = ?
        """, (id_pedido,))

        resultados = cursor.fetchall() # agora retorna (quantidade, nome, valor_unitario, id_produto)
        itens = []

        for resultado in resultados:
            item = ItemPedido(
                id_produto=resultado[3], # p.id
                nome_produto=resultado[1],
                quantidade=resultado[0],
                valor_unitario=resultado[2]
                # 'categoria' removido
            )
            itens.append(item)

        return itens
    except Exception as erro:
        print(f"🚫 Erro ao listar itens do pedido: {erro}")
        return []
    finally:
        conexao.close()

def fechar_mesa(numero):
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
            UPDATE pedidos
            SET status = ?, data_hora_fechamento = ?
            WHERE id_pedido = ?
        """, ("Fechado", datetime.now(), id_pedido))

        cursor.execute("""
            UPDATE mesas
            SET ocupada = ?, id_pedido_atual = ?
            WHERE numero = ?
        """, (False, None, numero))

        conexao.commit()

        cursor.execute("""
            SELECT SUM(ip.quantidade * ip.valor_unitario) FROM itens_pedido ip WHERE ip.id_pedido = ?
        """, (id_pedido,))
        total_pedido_fechado = cursor.fetchone()[0] or 0.0

        print(f"✅ Pedido da mesa '{numero}' fechado com sucesso! Valor total: R$ {total_pedido_fechado:.2f}")
        return True

    except Exception as e:
        try:
            conexao.rollback()
        except Exception:
            pass
        print(f"🚫 Erro ao fechar a mesa '{numero}': {e}")
        return False
    finally:
        conexao.close()

def calcular_total_pedido():
    conexao = criar_conexao()
    if not conexao:
        return 0.0

    try:
        cursor = conexao.cursor()
        hoje = datetime.now().date()

        cursor.execute("""
            SELECT SUM(ip.quantidade * ip.valor_unitario) AS total_dia
            FROM pedidos p
            JOIN itens_pedido ip ON p.id_pedido = ip.id_pedido
            WHERE DATE(p.data_hora_abertura) = ? AND p.status = 'Fechado'
        """, (hoje,))

        linha_total = cursor.fetchone()
        total_dia = linha_total[0] if linha_total[0] else 0.0

        print(f"💰 Total de vendas de {hoje}: R$ {total_dia:.2f}")
        return total_dia
    except Exception as e:
        print(f"🚫 Erro ao calcular total: {e}")
        return 0.0
    finally:
        conexao.close()

def relatorio_vendas():
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

        print(f"\n📊 ===== Relatório de Vendas - {hoje} =====")
        print(f"Total de pedidos fechados: {total_pedidos}")
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

def relatorio_vendas_detalhado():
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

        print(f"\n📊 ---- Relatório Detalhado de Vendas - {hoje} -----")
        print(f"Total de pedidos fechados: {total_pedidos}")
        print(f"Valor total vendido: R$ {valor_total_vendido:.2f}\n")
        print("Produtos mais vendidos:")
        print(f"{'Produto':<25} {'Qtd Vendida':<12} {'Valor Total':<12}")
        print("-" * 50)

        for produto, quantidade, valor in produtos_vendidos:
            print(f"{produto:<25} {quantidade:<12} R$ {valor:<11.2f}")

        print("-" * 50)

        return {
            "total_pedidos": total_pedidos,
            "valor_total_vendido": valor_total_vendido,
            "produtos_vendidos": produtos_vendidos
        }
    except Exception as e:
        print(f"🚫 Erro ao gerar relatório detalhado: {e}")
        return {}
    finally:
        conexao.close()