# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, 
# o salário e o cargo do funcionário. Implemente métodos para calcular o salário 
# líquido, considerando descontos de impostos e benefícios.
# -------------------------------------------
#classe base
class Funcionário:  #as classes devem ter letra inicial maiuscula por convenção
    def __init__(self, nome, cargo, salario_bruto):
        self.nome = nome
        self.cargo = cargo 
        self.salario_bruto = salario_bruto
    
    def calculadora_salario_liquido(self):
        # Calcula o salário líquido considerando:
        # - INSS (previdência): tabela
        # - IR (imposto de renda): tabela
        # - Benefícios: R$ 300 fixos somados ao salário (vale alimentação, vale transporte)
        beneficios = 300
        salario = self.salario_bruto
        # Cálculo do INSS conforme faixas simplificadas
        if salario <= 1518:
            inss = salario * 0.075
        elif salario >= 4190:
            inss = salario * 0.14
        else:
            inss = salario * 0.12
        # Cálculo simplificado do IR
        if salario <= 2112:
            ir = 0
        elif salario <= 2826:
            ir = salario * 0.075
        elif salario <= 3751:
            ir = salario * 0.15
        else:
            ir = salario * 0.225

        descontos = inss + ir
        salario_liquido = salario - descontos + beneficios

        return salario_liquido
    
def exibir_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Cargo: {self.cargo}")
    print(f"Salário Bruto: R$ {self.salario_bruto:.2f}")
    print(f"Salário Líquido: R$ {self.calculadora_salario_liquido():.2f}")
        
# Subclasse: Funcionária Ana
class funcionaria_Ana(Funcionário):
    def __init__(self, nome, cargo, salario_bruto):
        super().__init__(nome, cargo, salario_bruto)
    
    def atribuicao(self):
        print("Orientar e Acompanhar o trabalho dos Gerentes")
    
    def exibir_dados(self):
        return f"A Funcionária {self.nome}, possui o cargo de {self.cargo}, tem Salário Bruto R${self.salario_bruto:.2f} e Salário Líquido R${self.calculadora_salario_liquido():.2f}"

# Subclasse: Funcionária Karina
class funcionaria_Karina(Funcionário):
    def __init__(self, nome, cargo, salario_bruto):
        super().__init__(nome, cargo, salario_bruto)
    
    def atribuicao(self):
        print("Gerenciar as atividades executivas da unidade")

    def exibir_dados(self):
        return f"A Funcionária {self.nome}, possui o cargo de {self.cargo}, tem Salário Bruto R${self.salario_bruto:.2f} e Salário Líquido R${self.calculadora_salario_liquido():.2f}"

#  Criando uma instância
Ana = funcionaria_Ana("Ana", "Coordenadora Técnica", 12000)
Karina = funcionaria_Karina("Karina", "Gerente", 15000)
#chamando métodos
print(Ana.exibir_dados())
print("-------------")
print(Karina.exibir_dados())

# === MÉTODOS ESPECÍFICOS DAS SUBCLASSES ===
print('\n=== MÉTODOS ESPECÍFICOS DAS SUBCLASSES ===\n')
print('Ana' + '\n' + '-' * 50)
Ana.atribuicao()
print('\n' + 'Ana' + '\n' + '-' * 50)
Karina.atribuicao()

# Polimorfismo (lista de funcionários)
lista_funcionarios = [Funcionário("Ana", "Coordenadora Técnica", 12000),Funcionário("Karina", "Gerente", 15000)]
print("\n--- Lista de Funcionários ---")
for func in lista_funcionarios:
    print(f"{func.nome}: {func.cargo} - Salário Líquido R${func.calculadora_salario_liquido():.2f}")