# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

# def falar(self):
#     print("Som genérico")

# class Cachorro(Animal):
#     def falar(self):
#         print("Au au!")

# # Criando instâncias
# animal = Animal("Animal genérico")
# #aqui animal gerérico define a classe Animal com A maiusculo
# cachorro = Cachorro("Rex")

# # Chamando métodos
# #animal.falar() animal nesse caso é a classe animal genérica
# print("-")
# cachorro.falar() #nesse caso é a classe herdada cachorro
# print("-")
# print(animal.nome)  #animal nesse caso é a classe animal genérica = Animal Genérico
# print("-")
# print(cachorro.nome) #Atributo herdado
# -----------------------------------------------------------------------------
# Exercício 1
# class funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.salario = salario

#     def exibir_dados(self):
#         return (f"Nome: {self.nome}, Salário: R$ {self.salario}")

# class gerente(funcionario):
#     def __init__(self, nome, salario, função):
#         super().__init__(nome, salario)
#         self.função = função
    
#     def exibir_dados(self):
#         return (f"Nome: {self.nome}, Salário: R$ {self.salario}, Função: {self.função}")

# class desenvolvedor(funcionario):
#     def __init__(self, nome, salario, linguagem):
#         super().__init__(nome, salario)
#         self.linguagem = linguagem

# def exibir_dados(self):
#         return (f"Nome: {self.nome}, Salário: R$ {self.salario}, Linguagem: {self.linguagem}")

# # Teste das classes
# func = funcionario("Maria", 3000)
# ger = gerente("Ana", 10000, "Supervisionar Operações")
# dev = desenvolvedor("Ronaldo", 10000, "Python")
# print(func.exibir_dados())
# print(ger.exibir_dados())
# print(dev.exibir_dados())
# ----------------------------------------------------------------------------------
# Exercício 2
class veiculo:
    def __init__(self, marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade

    def mover(self):
        return f"Veículo {self.marca} se movendo"

class carro(veiculo):
    def __init__(self, marca, velocidade, movimento, forma):
        super().__init__(marca, velocidade)
        self.movimento = movimento  
        self.forma = forma          

    def mover(self):
        return f"carro {self.movimento} liga o motor"

    def exibir_dados(self):
        return (f"O carro de marca {self.marca}, com velocidade {self.velocidade}, {self.movimento}, e se move {self.forma}")

class bicicleta(veiculo):
    def __init__(self, marca, velocidade, movimento, forma):
        super().__init__(marca, velocidade)
        self.movimento = movimento
        self.forma = forma
    
    def mover(self):
        return f"bicileta {self.movimento} sobe na bike"
    
    def exibir_dados(self):
        return (f"A bicileta de marca {self.marca}, com velocidade {self.velocidade}, {self.movimento}, e se move {self.forma}")

# Teste das classes
car = carro("Toyota", 120, "liga o motor", "acelerando")
print(car.exibir_dados())
print("-")
bike = bicicleta("Caloi", 25, "sobe na bike", "pedalando")
print(bike.exibir_dados())

# Polimorfismo em ação
veiculos = [car, bike]
for i in veiculos:
    print(f"{i.mover()}")