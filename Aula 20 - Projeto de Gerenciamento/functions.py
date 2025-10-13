class Produto:
     def __init__(self, id, nome, valor):
        self.id = id
        self.nome = nome
        self.valor = valor

# nome = input("Digite o nome do produto: ")
# valor = float(input("Digite o valor do produto: ")) 

def cadastrar_produto(id, nome):
    from bd import conexao # Importa a conexão do banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO produtos (id, nome) VALUES (?, ?)", (id, nome)) # Insere o produto e seu valor na tabela
    conexao.commit() # Salva as alterações no banco de dados
    print(f"Produto '{nome}' cadastrado com sucesso!")
    return True