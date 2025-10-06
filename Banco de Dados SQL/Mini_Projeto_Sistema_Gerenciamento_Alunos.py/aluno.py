# Classe aluno
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

    def para_tupla(self):
        return (self.nome, self.idade)

