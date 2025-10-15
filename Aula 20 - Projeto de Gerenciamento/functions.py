class Produto:
     def __init__(self, id, nome, valor):
        self.id = id
        self.nome = nome
        self.valor = valor

class Item: 
    def __init__(self, id_item, id_produto, quantidade, id_pedido):
        self.id_item = id_item
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.id_pedido = id_pedido

class Pedido(Produto): # Herda de Produto id, nome e valor
     def __init__(self, id, produto, quantidade, valor_unitario):
        super().__init__(produto.id, produto.nome, produto.valor) # Chama o construtor da classe Produto
        # abaixo define os atributos específicos da classe Pedido
        self.id = id 
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario.valor # aqui o .valor se refere ao atributo valor da classe Produto

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

def atualizar_produto(nome, novo_nome, novo_valor): #cria função para atualizar produto pelo nome
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("UPDATE produtos SET nome = ?, valor = ? WHERE nome = ?", (novo_nome, novo_valor, nome)) # Atualiza o produto pelo nome na tabela
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Produto '{nome}' atualizado com sucesso para '{novo_nome}' com valor '{novo_valor}'!")
    return True

def listar_itens_pedido(id_pedido): #cria função para listar todos os itens de um pedido
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("""
        SELECT i.ID_Item, i.ID_Produto, i.Quantidade_item, p.Valor_unitario_produto,
               (i.Quantidade_item * p.Valor_unitario_produto) AS Valor_total_item
        FROM Item i
        JOIN Produtos p ON i.ID_Produto = p.ID_produtos
        WHERE i.ID_Pedido = ?
    """, (id_pedido,)) # Seleciona todos os itens do pedido com o valor total calculado
    resultados = cursor.fetchall() # Obtém todos os resultados da consulta
    return resultados # Retorna a lista de itens do pedido encontrados
