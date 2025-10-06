
# Funções de banco
def inserir_aluno(conexao, aluno):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", aluno.para_tupla())
    conexao.commit()
    return True


def listar_alunos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    return cursor.fetchall()


def buscar_aluno(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos WHERE nome LIKE ?", ('%' + nome + '%',))
    return cursor.fetchall()

# Exemplo de função para deletar aluno
def deletar_aluno (conexao, nome):
    cursor = conexao.cursor()
    # Verificar se o aluno existe
    cursor.execute ("SELECT * FROM alunos WHERE nome = ?",(nome,))
    aluno = cursor.fetchone ()
    if aluno:
        cursor.execute("DELETE FROM alunos WHERE nome = ?",(nome,))
        conexao.commit()
        return True
    else :
        return False

# Exemplo de função para deletar aluno
def alterar_aluno (conexao, nome):
    cursor = conexao.cursor()
    # Verificar se o aluno existe
    cursor.execute ("SELECT * FROM alunos WHERE nome = ?",(nome,))
    aluno = cursor.fetchone ()
    if aluno:
        novo_nome = input("Digite o nome novo:")
        nova_idade = input("Digite a idade nova:")
        cursor.execute("UPDATE alunos SET nome = ?, idade = ? WHERE nome = ?",  (novo_nome, nova_idade, nome))
        # cursor.execute("""
        #                 UPDATE alunos
        #                 SET nome = ?, idade = ?
        #                 WHERE nome = ?
        #             """, (novo_nome, nova_idade, nome))
        conexao.commit()
        return True
    else :
        return False
