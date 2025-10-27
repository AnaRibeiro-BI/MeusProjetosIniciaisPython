# classes.py
from datetime import datetime

class Produto:
    def __init__(self, id=None, nome="", valor=0.0):
        self.id = id
        self.nome = nome
        self.valor = valor

    def __str__(self): # Retorna uma string formatada com as informações do objeto, facilitando a leitura do que foi inputado
        return f"ID: {self.id} | {self.nome} | R$ {self.valor:.2f}"

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
# O =0 no parâmetro do método __init__ é uma forma de dizer “Se ninguém informar um valor, use este por padrão.”
# evita erros e permite criar objetos mesmo sem passar todos os argumentos.
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = ocupada
        self.id_pedido_atual: None

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
    def __init__(self, id=None, id_atendente=0, numero_mesa=0, status="Aberto"):
        self.id = id
        self.id_atendente = id_atendente
        self.numero_mesa = numero_mesa
        self.itens = []
        self.data_pedido = datetime.now()
        self.valor_total = 0.0
        self.status = status

    def adicionar_item(self, item):
        self.itens.append(item)
        self.calcular_total()

    def calcular_total(self):
        self.valor_total = 0.0
        for item in self.itens:
            self.valor_total += item.calcular_subtotal()

    def __str__(self):
        return f"Pedido {self.id} | Mesa {self.numero_mesa} | Status: {self.status} | Total: R$ {self.valor_total:.2f}"

class ItemPedidoHerdado:
    def __init__(self, id=None, quantidade=0, valor_unitario=0.0):
        self.id = id
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario