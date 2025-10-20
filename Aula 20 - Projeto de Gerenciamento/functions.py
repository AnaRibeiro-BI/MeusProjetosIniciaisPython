# Definição das classes dos objetos do sistema de gerenciamento do restaurante conforme o modelo ERD(desenho)

from datetime import datetime # Importa datetime para manipulação de datas e horas no pedido
from typing import List, Optional # Importa List e Optional para tipagem de listas e valores opcionais (sugestão IA)

class Produto:
     def __init__(self, id, nome: str, valor: float):
        self.id = id
        self.nome = nome
        self.valor = valor

class Item: 
    def __init__(self, id_item: int, id_produto: int, quantidade: int, id_pedido: int):
        self.id_item = id_item
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.id_pedido = id_pedido
   
class Pedido: 
    def __init__(self, id: int, id_atendente: int, id_mesa: int):
        self.id = id
        self.id_atendente = id_atendente
        self.id_mesa = id_mesa
        self.itens = []  # Lista para armazenar os itens do pedido
        self.data_pedido = datetime.now()
        self.itens: List[Item] = []
        self.status = "Aberto", "Fechado", "Cancelado" # Aberto, Fechado, Cancelado

class Pedido(Produto): # Herda de Produto id, nome e valor
     def __init__(self, id: int, produto, quantidade, valor_unitario):
        super().__init__(produto.id, produto.nome, produto.valor) # Chama o construtor da classe Produto
        # abaixo define os atributos específicos da classe Pedido
        self.id = id 
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario.valor # aqui o .valor se refere ao atributo valor da classe Produto

class Atendente:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome
        self.ativo = True

class Mesa:
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = False # false indica que a mesa está desocupada
        self.id_pedido_atual: Optional[int] = None # ID do pedido atual associado à mesa, None se não houver pedido

# Funções para manipulação dos dados no banco de dados SQLite para o Sistema de Gerenciamntento do Restaurante

def cadastrar_produto(id, nome, valor): #cria função para cadastrar ID, Nome e Valor do produto
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        # Insere o produto, nome e valor na tabela
    cursor.execute("INSERT INTO produtos (id, nome, valor) VALUES (?, ?, ?)", (id, nome, valor)) 
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Produto '{nome}' cadastrado com sucesso!")
    return True

def buscar_produto(nome): #cria função para buscar produto pelo nome
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,)) # Busca o produto pelo nome na tabela
    resultado = cursor.fetchall() # Obtém todos os resultados da consulta
    return resultado # Retorna os resultados encontrados

def listar_produtos(): #cria função para listar todos os produtos
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("SELECT * FROM produtos") # Seleciona todos os produtos da tabela
    resultados = cursor.fetchall() # Obtém todos os resultados da consulta
    return resultados # Retorna a lista de produtos encontrados

def remover_produto(id): #cria função para remover produto pelo ID
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,)) # Remove o produto pelo ID na tabela
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Produto com ID '{id}' removido com sucesso!")
    return True

def realizar_pedido(id_atendente, id_mesa, itens: list): #cria função para realizar pedido com id_atendente, id_mesa e itens do pedido 
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO pedidos (id_atendente, id_mesa, data_pedido, status) VALUES (?, ?, ?, ?)", 
                   (id_atendente, id_mesa, datetime.now(), "Aberto")) # Insere o pedido na tabela
    id_pedido = cursor.lastrowid # Obtém o ID do pedido recém-criado
    for item in itens: # Para cada item no pedido
        cursor.execute("INSERT INTO itens (id_pedido, id_produto, quantidade) VALUES (?, ?, ?)", 
                       (id_pedido, item.id_produto, item.quantidade)) # Insere o item na tabela
    conexao.commit() # Salva as alterações no banco de dados
    print(f"🚀 Pedido realizado com sucesso! ID do Pedido: {id_pedido}")
    return id_pedido

def atualizar_produto(nome, novo_nome, novo_valor): #cria função para atualizar produto pelo nome
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("UPDATE produtos SET nome = ?, valor = ? WHERE nome = ?", (novo_nome, novo_valor, nome)) # Atualiza o produto pelo nome na tabela
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Produto '{nome}' atualizado com sucesso para '{novo_nome}' com valor '{novo_valor}'!")
    return True

def listar_itens_pedido(id_pedido): #cria função para listar todos os itens de um pedido o id_pedido é o identificador único do pedido
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    # i é abreviação para item e p para produto
    # A consulta SQL abaixo seleciona os itens do pedido junto com o valor unitário do produto e calcula o valor total do item (quantidade * valor unitário)
    cursor.execute("""
        SELECT i.ID_Item, i.ID_Produto, i.Quantidade_item, p.Valor_unitario_produto,
               (i.Quantidade_item * p.Valor_unitario_produto) AS Valor_total_item
        FROM Item i 
        JOIN Produtos p ON i.ID_Produto = p.ID_produtos
        WHERE i.ID_Pedido = ?
    """, (id_pedido,)) # Seleciona todos os itens do pedido com o valor total calculado
    resultados = cursor.fetchall() # Obtém todos os resultados da consulta
    return resultados # Retorna a lista de itens do pedido encontrados

 # calcula o subtotal do item do pedido 
def calcular_subtotal(self, valor_unitario: float) -> float: # o -> float indica o tipo de retorno da função
    return self.quantidade * valor_unitario    # Retorna o subtotal do item do pedido

# define a função de representação em string da classe Produto
# O método __str__ é um método especial (também chamado de "dunder method") em Python que define como um objeto será representado quando convertido para string.
def __str__(self): # sugestão IA
    return f"Produto(id={self.id}, nome='{self.nome}', valor=R${self.valor:.2f})"

def cadastrar_atendente(id, nome): #cria função para cadastrar atendente pelo id e nome
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO atendentes (id, nome, ativo) VALUES (?, ?, ?)", (id, nome, True)) # Insere o atendente na tabela]
    # define True como padrão para saber se o atendente está ativo no restaurante
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Atendente '{nome}' cadastrado com sucesso!")
    return True

def listar_atendentes(): #cria função para listar todos os atendentes
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("SELECT * FROM atendentes") # Seleciona todos os atendentes da tabela
    resultados = cursor.fetchall() # Obtém todos os resultados da consulta
    return resultados # Retorna a lista de atendentes encontrados

def abrir_mesa(numero, capacidade): #cria função para abrir mesa pelo número e capacidade
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO mesas (numero, capacidade, ocupada) VALUES (?, ?, ?)", (numero, capacidade, False)) # Insere a mesa na tabela indicando numero, capacidade e ocupação
    # define False como padrão para saber se a mesa está ocupada no restaurante
    conexao.commit() # Salva as alterações no banco de dados
    if True:
        print(f"Mesa '{numero}' com capacidade para {capacidade} pessoas aberta com sucesso!")
    else: 
        print(f"🚫 Erro ao abrir a mesa '{numero}'.")
    # Retorna True após abrir a mesa com sucesso
    return True

def listar_mesas(): #cria função para listar todas as mesas
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("SELECT * FROM mesas") # Seleciona todas as mesas da tabela
    resultados = cursor.fetchall() # Obtém todos os resultados da consulta
    return resultados # Retorna a lista de mesas encontrados

def fechar_mesa(numero): # Fecha o pedido associado à mesa 'numero' e libera a mesa. 
# Fluxo:
# - busca mesa e pedido associado
# - calcula total do pedido (soma quantidade * valor)
# - atualiza status do pedido para 'fechado' (se ainda não estiver)
# - libera a mesa (ocupada = False, id_pedido_atual = NULL)
# - commit ou rollback em caso de erro
# Retorna True quando concluído com sucesso, False caso ocorra algum problema.
    from bd import conexao
    cursor = conexao.cursor()
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
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor()
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

def gerar_relatorio_vendas():
   from datetime import datetime

def relatorio_vendas_detalhado():
# Gera um relatório de vendas do dia atual, incluindo:
# - Total de pedidos
# - Total vendido
# - Produtos mais vendidos (quantidade e valor)
    from bd import conexao
    cursor = conexao.cursor()
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
