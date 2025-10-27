# Funções para manipulação dos dados no banco de dados SQLite para o Sistema de Gerenciamntento do Restaurante
from bd import criar_conexao
from class import *
from datetime import datetime

def cadastrar_produto(id, nome, valor, categoria): #cria função para cadastrar ID, Nome e Valor do produto
    conexao = criar_conexao()
    if not conexao:
        return False
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (id: INTEGER PRIMARY KEY AUTOINCREMENT, nome, valor, categoria) VALUES (?, ?, ?, ?)", (id, nome, valor, categoria)) 
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Produto '{nome}' cadastrado com sucesso!")
    return True
conexao.close()

def buscar_produto(nome): #cria função para buscar produto pelo nome
    conexao = criar_conexao()
    if not conexao:
        return []
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,)) # Busca o produto pelo nome na tabela
    resultado = cursor.fetchone() # Obtém todos os resultados da consulta
    if resultado:
            produto = Produto(resultado[0], resultado[1], resultado[2], resultado[3])
            return produto
    return produto
conexao.close()

def listar_produtos(): #cria função para listar todos os produtos
    conexao = criar_conexao()
    if not conexao:
        return []
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    resultados = cursor.fetchall()
    produtos = []
    for resultado in resultados:
        produto = Produto(resultado[0], resultado[1], resultado[2], resultado[3])
        produtos.append(produto)
        return produtos
conexao.close()

def remover_produto(id_produto): # Remove um produto pelo ID
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
conexao.close()

def realizar_pedido(id_atendente, id_mesa, itens: list): #cria função para realizar pedido com id_atendente, id_mesa e itens do pedido 
    from datetime import datetime
    conexao = criar_conexao()
    if not conexao:
        return [] # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO pedidos (id_atendente, id_mesa, data_pedido, status) VALUES (?, ?, ?, ?)", 
                   (id_atendente, id_mesa, datetime.now(), "Aberto")) # Insere o pedido na tabela
    id_pedido = cursor.lastrowid # Obtém o ID do pedido recém-criado
    for item in itens: # Para cada item no pedido
        cursor.execute("INSERT INTO itens (id_pedido: INTEGER PRIMARY KEY AUTOINCREMENT, id_produto, quantidade) VALUES (?, ?, ?)", 
                       (id_pedido, item.id_produto, item.quantidade)) # Insere o item na tabela
    conection.commit() # Salva as alterações no banco de dados
    print(f"🚀 Pedido realizado com sucesso! ID do Pedido: {id_pedido}")
    return id_pedido

def atualizar_produto(id_produto, novo_nome=None, nova_categoria=None, novo_valor=None): # Atualiza um produto existente
    conexao = criar_conexao()
    if not conexao:
        return False
    try:
        cursor = conexao.cursor()
        # Buscar produto atual
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
        produto_atual = cursor.fetchone()
        if not produto_atual:
            print("🚫 Produto não encontrado!")
            return False
        # Usar valores atuais se novos valores não foram fornecidos
        nome = novo_nome if novo_nome else produto_atual[1]
        categoria = nova_categoria if nova_categoria else produto_atual[2]
        valor = novo_valor if novo_valor else produto_atual[3]
        cursor.execute(
            "UPDATE produtos SET nome = ?, categoria = ?, valor = ? WHERE id = ?",
            (nome, categoria, valor, id_produto)
        )
        conexao.commit()
        print("✅ Produto atualizado com sucesso!")
        return True
    except Exception as erro:
        print(f"🚫 Erro ao atualizar produto: {erro}")
        return False
    finally:
        conexao.close()

def listar_itens_pedido(id_pedido): #cria função para listar itens do pedido pelo id_pedido
    conexao = criar_conexao()
    if not conexao:
        return []
    cursor.execute("""
        SELECT 
            i.id_item,
            p.nome_produto,
            i.quantidade_item,
            p.valor_unitario_produto,
            (i.quantidade_item * p.valor_unitario_produto) AS valor_total_item
        FROM itens_pedido i
        JOIN produtos p ON i.id_produto = p.id_produto
        WHERE i.id_pedido = ?
    """, (id_pedido,))
    # chama o id do item, nome do produto, quantidade do item, valor unitário do produto e calcula o valor total do item (quantidade * valor unitário)
    resultados = cursor.fetchall() # Obtém todos os resultados da consulta
    cursor.close()
    return resultados

 # calcula o subtotal do item do pedido 
def calcular_subtotal(self, valor_unitario: float) -> float: # o -> float indica o tipo de retorno da função
    return self.quantidade * valor_unitario    # Retorna o subtotal do item do pedido

# define a função de representação em string da classe Produto
# O método __str__ é um método especial (também chamado de "dunder method") em Python que define como um objeto será representado quando convertido para string.
def __str__(self): # sugestão IA
    return f"Produto(id={self.id}, nome='{self.nome}', valor=R${self.valor:.2f})"

def cadastrar_atendente(nome): #cria função para cadastrar atendente pelo id e nome
    conexao = criar_conexao()
    if not conexao:
        return False
    try:
        conexao = criar_conexao()
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
            atendente = Atendente(resultado[0], resultado[1], bool(resultado[2]))
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
        cursor.execute(
            "INSERT INTO mesas (numero, capacidade) VALUES (?, ?)",
            (numero, capacidade)
        )
        conexao.commit()
        print(f"✅ Mesa {numero} cadastrada com sucesso!")
        return True
    except Exception as erro:
        print(f"🚫 Erro ao cadastrar mesa: {erro}")
        return False
    finally:
        conexao.close()

# def abrir_mesa(numero, capacidade): #cria função para abrir mesa pelo número e capacidade
#     cursor = conection.cursor() # Cria um cursor para executar comandos SQL
#     cursor.execute("INSERT INTO mesas (numero, capacidade, ocupada) VALUES (?, ?, ?)", (numero, capacidade, False)) # Insere a mesa na tabela indicando numero, capacidade e ocupação
#     # define False como padrão para saber se a mesa está ocupada no restaurante
#     conection.commit() # Salva as alterações no banco de dados
#     if True:
#         print(f"Mesa '{numero}' com capacidade para {capacidade} pessoas aberta com sucesso!")
#     else: 
#         print(f"🚫 Erro ao abrir a mesa '{numero}'.")
#     # Retorna True após abrir a mesa com sucesso
#     return True

def listar_mesas(): #cria função para listar todas as mesas
    conexao = criar_conexao()
    if not conexao:
        return []
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM mesas")
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
    """
    Realiza um novo pedido
    lista_itens deve ser uma lista de dicionários: [{'nome_produto': 'Pizza', 'quantidade': 2}, ...]
    """
    conexao = criar_conexao()
    if not conexao:
        return False
    
    try:
        cursor = conexao.cursor()
        
        # Criar o pedido
        cursor.execute(
            "INSERT INTO pedidos (numero_mesa, id_atendente) VALUES (?, ?)",
            (numero_mesa, id_atendente)
        )
        id_pedido = cursor.lastrowid
        
        valor_total = 0.0
        
        # Adicionar itens ao pedido
        for item_data in lista_itens:
            nome_produto = item_data['nome_produto']
            quantidade = item_data['quantidade']
            
            # Buscar produto
            cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome_produto,))
            produto = cursor.fetchone()
            
            if not produto:
                print(f"🚫 Produto '{nome_produto}' não encontrado!")
                continue
            
            valor_unitario = produto[3]  # valor do produto
            subtotal = quantidade * valor_unitario
            valor_total += subtotal
            
            # Inserir item do pedido
            cursor.execute(
                "INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, valor_unitario) VALUES (?, ?, ?, ?)",
                (id_pedido, produto[0], quantidade, valor_unitario)
            )
        
        # Atualizar valor total do pedido
        cursor.execute(
            "UPDATE pedidos SET valor_total = ? WHERE id = ?",
            (valor_total, id_pedido)
        )
        
        # Marcar mesa como ocupada
        cursor.execute(
            "UPDATE mesas SET ocupada = 1, id_pedido_atual = ? WHERE numero = ?",
            (id_pedido, numero_mesa)
        )
        
        conexao.commit()
        print(f"✅ Pedido {id_pedido} realizado com sucesso! Total: R\$ {valor_total:.2f}")
        return id_pedido
        
    except Exception as erro:
        print(f"🚫 Erro ao realizar pedido: {erro}")
        return False
    finally:
        conexao.close()

def listar_itens_pedido(id_pedido):
    """Lista todos os itens de um pedido"""
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
                id_produto=0,  # Não precisamos do ID aqui
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

def fechar_mesa(numero): # Fecha o pedido associado à mesa 'numero' e libera a mesa. 
# Fluxo:
# - busca mesa e pedido associado
# - calcula total do pedido (soma quantidade * valor)
# - atualiza status do pedido para 'fechado' (se ainda não estiver)
# - libera a mesa (ocupada = False, id_pedido_atual = NULL)
# - commit ou rollback em caso de erro
# Retorna True quando concluído com sucesso, False caso ocorra algum problema.
    conexao = criar_conexao()
    if not conexao:
        return []
    try:
        # 1) Busca informações da mesa e do pedido associado
        cursor.execute("""
            SELECT mesa.id, mesa.id_pedido_atual, pedido.status
            FROM mesas AS mesa
            LEFT JOIN pedidos AS pedido ON mesa.id_pedido_atual = pedido.id
            WHERE mesa.numero = ?;
        """, (numero,))
        resultado = cursor.fetchone()
        if not resultado:
            print(f"🚫 Mesa '{numero}' não encontrada.")
            return False
        id_mesa, id_pedido, status_pedido = resultado
        print(f"🔎 Fechando mesa ID {id_mesa}, pedido {id_pedido} (status: {status_pedido})")
        if id_pedido is None:
            print(f"🚫 A mesa '{numero}' não possui pedido associado para fechar.")
            return False

# Calcula o total do pedido 
        cursor.execute("""
            SELECT SUM(i.quantidade * p.valor) AS total_pedido
            FROM itens AS i
            JOIN produtos AS p ON i.id_produto = p.id
            WHERE i.id_pedido = ?;
        """, (id_pedido,))
        linha_total = cursor.fetchone() # Retorna uma tupla com os resultados da consulta SQL pq retorna apenas uma coluna e uma linha (a soma total
        total_pedido = linha_total[0] or None # Se for None, atribui 0.0 como valor padrão, se não atribui o primeiro valor retorecnontrado nado pela consulta SQL
        print(f"💰 Total do pedido ID {id_pedido}: R${total_pedido:.2f}")

# Se o pedido ainda não estiver marcado como fechado, atualiza status
        if status_pedido is None or status_pedido.lower() != "fechado": # se o status do pedido for diferente de fechado
            # atualiza o status do pedido para 'Fechado'
            cursor.execute("""
                UPDATE pedidos
                SET status = ?
                WHERE id = ?;
            """, ("Fechado", id_pedido))
            
# Libera a mesa e desassocia o pedido anterior feito
        cursor.execute("""
            UPDATE mesas
            SET ocupada = ?, id_pedido_atual = ?
            WHERE numero = ?;
        """, (False, None, numero)) # Libera a mesa definindo ocupada como False e id_pedido_atual como None

        conexao.commit()
        print(f"✅ Pedido da mesa '{numero}' fechado com sucesso! Valor total: R${total_pedido:.2f}")
        return True

    except Exception as e: # em caso de erro (exception), desfaz as alterações feitas na transação
        try:
            conexao.rollback() # rollback desfaz todas as alterações feitas na transação atual
        except Exception: # em caso de erro ao fazer rollback, apenas ignore o erro
            pass # ignorar
        print(f"🚫 Erro ao fechar a mesa '{numero}': {e}") 
        return False

def calcular_total_pedido() -> float:
    # Calcula o valor total de todos os pedidos realizados no dia atual
    from datetime import datetime # Importa datetime para manipulação de datas 
    conexao = criar_conexao()
    if not conexao:
        return []
    hoje = datetime.now().date()  # define a variável hoje com a data atual , descondiderando a hora
    cursor.execute("""
        SELECT SUM(i.quantidade * p.valor) AS total_dia
        FROM pedidos ped
        JOIN itens i ON ped.id = i.id_pedido
        JOIN produtos p ON i.id_produto = p.id
        WHERE DATE(ped.data_pedido) = ?;
    """, (hoje,))
    linha_total = cursor.fetchone()
    total_dia = linha_total[0] or None  # Se não houver pedidos no dia, retorna None
    print(f"💰 Total de vendas de {hoje}: R${total_dia:.2f}") 
    return total_dia

def relatorio_vendas():
    # Gera um relatório simples de vendas do dia atual, incluindo total de pedidos e valor total vendido
    conexao = criar_conexao()
    if not conexao:
        return []
    from datetime import datetime # Importa datetime para manipulação de datas 
    hoje = datetime.now().date()
    # Total de pedidos e valor total vendido
    cursor.execute("""
        SELECT COUNT(*) AS total_pedidos,
               SUM(i.quantidade * p.valor) AS valor_total_vendido
        FROM pedidos ped
        JOIN itens i ON ped.id = i.id_pedido
        JOIN produtos p ON i.id_produto = p.id
        WHERE DATE(ped.data_pedido) = ?;
    """, (hoje,))
    total_pedidos, valor_total_vendido = cursor.fetchone() or (0, 0.0) # Se não houver pedidos, retorna 0 e 0.0

    # Exibição do relatório
    print(f"\n -----📊 Relatório de Vendas - {hoje} -----")
    print(f"Total de pedidos: {total_pedidos}")
    print(f"Valor total vendido: R${valor_total_vendido:.2f}")
    print("-" * 30)
    return {
        "total_pedidos": total_pedidos,
        "valor_total_vendido": valor_total_vendido
    }

def relatorio_vendas_detalhado():
# Gera um relatório de vendas do dia atual, incluindo:
# - Total de pedidos
# - Total vendido
# - Produtos mais vendidos (quantidade e valor)
    conexao = criar_conexao()
    if not conexao:
        return []
    from datetime import datetime # Importa datetime para manipulação de datas 
    hoje = datetime.now().date()
 # Total de pedidos e valor total vendido
    cursor.execute("""
        SELECT COUNT(*) AS total_pedidos,
               SUM(i.quantidade * p.valor) AS valor_total_vendido
        FROM pedidos ped
        JOIN itens i ON ped.id = i.id_pedido
        JOIN produtos p ON i.id_produto = p.id
        WHERE DATE(ped.data_pedido) = ? AND ped.status = 'Fechado';
    """, (hoje,))
    total_pedidos, valor_total_vendido = cursor.fetchone() or (0, 0.0)

# Produtos mais vendidos
    cursor.execute("""
        SELECT 
            p.nome AS produto,
            SUM(i.quantidade) AS quantidade_vendida,
            SUM(i.quantidade * p.valor) AS valor_total
        FROM pedidos ped
        JOIN itens i ON ped.id = i.id_pedido
        JOIN produtos p ON i.id_produto = p.id
        WHERE DATE(ped.data_pedido) = ? AND ped.status = 'Fechado'
        GROUP BY p.id
        ORDER BY quantidade_vendida DESC;
    """, (hoje,))
    produtos_vendidos = cursor.fetchall()

# Exibição do relatório
    print(f"\n -----📊 Relatório de Vendas - {hoje} -----")
    print(f"Total de pedidos fechados: {total_pedidos}")
    print(f"Valor total vendido: R${valor_total_vendido:.2f}\n")
    print("Produtos mais vendidos:")
    print(f"{'Produto':<25} {'Qtd Vendida':<12} {'Valor Total':<12}")
    print("-" * 50)
    for produto, quantidade, valor in produtos_vendidos:
        print(f"{produto:<25} {quantidade:<12} R${valor:<12.2f}")
    print("-" * 50)
    return {
        "total_pedidos": total_pedidos,
        "valor_total_vendido": valor_total_vendido,
        "produtos_vendidos": produtos_vendidos
    }
