import sqlite3
#importando bilbioteca sqlite3
banco = sqlite3.connect('primeiro_banco_de_dados.db')
#criando o primeiro banco de dados
cursor = banco.cursor()    #cursor é um comando específico de banco de dados o qual executa os comandos SQL
#se não definir o cursor, não é possível executar comandos SQL
cursor.execute("CREATE TABLE pessoas (nome TEXT, idade INTEGER, email TEXT)")
cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES ('Maria', 40, 'maria_123@gmail.com')")
banco.commit()
cursor.execute('SELECT * FROM pessoas')
print(cursor.fetchall())  #fetchall() retorna todas as linhas da tabela