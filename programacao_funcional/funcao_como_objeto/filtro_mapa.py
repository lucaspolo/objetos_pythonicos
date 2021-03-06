alunos = [('Renzo', 0), ('Luciano', 10), ('Ada', 9)]

print([(nome, nota) for nome, nota in alunos if nota > 5])


# Pode-se fazer o mesmo usando filter
def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5


print(list(filter(possui_nota_maior_que_5, alunos)))


# Agora vamos apenas extrair apenas o nome
def extrair_nome(aluno):
    nome, _ = aluno
    return nome


print(list(map(extrair_nome, filter(possui_nota_maior_que_5, alunos))))
