import sqlite3
def conection():
    #Criação da conexão com o banco
    conexao = sqlite3.connect("alunos.db")

    #Criação do cursor
    cursor = conexao.cursor()

    # Criar o banco

    try:
        cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT, idade INTEGER)''')
        conexao.commit()
    except sqlite3.Error as erro:
        print(f"Erro no banco: {erro}")
    return conexao

# def inserir_aluno(aluno):
#     cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", aluno.para_tupla())
#     conexao.commit()

# def listar_alunos():
#     cursor.execute("SELECT * FROM alunos")
#     return cursor.fetchall()

# def alterar_aluno(id, aluno):
#     cursor.execute(f"UPDATE alunos SET nome = ?, idade = ? WHERE id = {id}", aluno.para_tupla())
#     conexao.commit()

# def deletar_aluno(id):
#     cursor.execute(f"DELETE FROM alunos WHERE id = {id}")
#     conexao.commit()

# def buscar_aluno(nome):
#     if nome == "":
#         print("Nome não foi inserido")
    
#     cursor.execute(f"SELECT * FROM alunos WHERE nome LIKE '%{nome}%'")
#     return cursor.fetchall()