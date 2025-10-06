import sqlite3

# CONEXÃO COM O BANCO DE DADOS

conexao = sqlite3.connect("banco_teste.db")
cursor = conexao.cursor()

# CRIAÇÃO DA TABELA CLIENTES
cursor.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT, telefone TEXT, cidade TEXT)")

# INSERÇÃO DE DADOS FICTÍCIOS
cursor.execute("DELETE FROM clientes;")

clientes = [
    ("Ana Silva", "ana@email.com", "(62)99999-1111", "Goiânia"),
    ("Carlos Oliveira", "carlos@email.com", "(21)88888-2222", "Rio de Janeiro"),
    ("Mariana Costa", "mariana@email.com", "(31)97777-3333", "Belo Horizonte"),
    ("Pedro Santos", "pedro@email.com", "(41)96666-4444", "Aparecida de Goiânia"),
    ("Fernanda Lima", "fernanda@email.com", "(64)95555-5555", "Rio Verde"),
    ("Paulo Abreu", "pauloabreu@email.com", "(62)98555-2333", "Goiânia"),
    ("João Carlos", "joaocarlos@email.com", "(62)96666-4444", "Goiânia")
]

cursor.executemany("INSERT INTO clientes (nome, email, telefone, cidade) VALUES (?, ?, ?, ?)", clientes)
# Inserir múltiplos registros

conexao.commit() # Salvar (commit) as mudanças
print(" Banco de dados 'banco_teste.db' criado com sucesso com a tabela 'clientes'!")

# CONSULTAR E MOSTRAR RESULTADOS
cursor.execute("SELECT * FROM clientes;")
resultados = cursor.fetchall()

print("\n Lista de clientes cadastrados:\n")

# Cabeçalho formatado
print(f"{'Nº':<3} {'ID':<3} {'Nome':<18} {'Email':<25} {'Telefone':<17} {'Cidade'}")
print("-" * 80)

# Mostrar dados com índice
for i, (id_cliente, nome, email, telefone, cidade) in enumerate(resultados, start=1): # Iniciar a contagem a partir de 1
    print(f"{i:<3} {id_cliente:<3} {nome:<18} {email:<25} {telefone:<17} {cidade}") # Formatação da tabela para alinhamento

# ENCERRAR CONEXÃO
conexao.close() # Fechar a conexão com o banco de dados