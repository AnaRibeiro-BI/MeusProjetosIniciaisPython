# Definição das classes dos objetos do sistema de gerenciamento do restaurante conforme o modelo ERD(desenho)

from datetime import datetime # Importa datetime para manipulação de datas e horas no pedido

class Produto:
     def __init__(self, id=None, nome="", categoria="", valor=0.0):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.categoria = categoria 

def __str__(self):
    return f"ID {self.id} | {self.nome} | {self.categoria} | R$ {self.valor:.2f}"

class Atendente:
    def __init__(self, id=None, nome="", ativo=True):
        self.id = id
        self.nome = nome
        self.ativo = ativo

def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"ID: {self.id} | {self.nome} | Status: {status}"

class Mesa:
    def __init__(self, numero=0, capacidade=0, ocupada=False):
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = ocupada # false indica que a mesa está desocupada
        self.id_pedido_atual: None # ID do pedido atual associado à mesa, None se não houver pedido

def __str__(self):
        status = "Ocupada" if self.ocupada else "Livre"
        return f"Mesa {self.numero} | Capacidade: {self.capacidade} | Status: {status}"

class ItemPedido:
    def __init__(self, id_produto=0, nome_produto="", quantidade=0, valor_unitario=0.0):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

def calcular_subtotal(self):
        return self.quantidade * self.valor_unitario

def __str__(self):
        subtotal = self.calcular_subtotal()
        return f"{self.nome_produto} | Qtd: {self.quantidade} | Valor Unit: R$ {self.valor_unitario:.2f} | Subtotal: R$ {subtotal:.2f}"
        
 
class Pedido: 
    def __init__(self, id=None, id_atendente=0, numero_mesa=0):
        self.id = id
        self.id_atendente = id_atendente
        self.numero_mesa = numero_mesa
        self.itens = []  # Lista para armazenar os itens do pedido
        self.data_pedido = datetime.now()
        self.valor_total = 0.0

def adicionar_item(self, item):
    self.itens.append(item)
    self.calcular_total()
    
def calcular_total(self):
    self.valor_total = 0.0
    for item in self.itens:
        self.valor_total += item.calcular_subtotal()
    
def __str__(self):
    return f"Pedido {self.id} | Mesa {self.numero_mesa} | Status: {self.status} | Total: R$ {self.valor_total:.2f}"

class ItemPedidoHerdado(Produto): # Herda de Produto id, nome, valor e categoria
     def __init__(self, id=None, produto="", quantidade=0, valor_unitario=0.0):
        super().__init__(produto.id, produto.nome, produto.valor, produto.categoria) # Chama o construtor da classe Produto
        # abaixo define os atributos específicos da classe Pedido
        self.id = id 
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario.valor # aqui o .valor se refere ao atributo valor da classe Produto

