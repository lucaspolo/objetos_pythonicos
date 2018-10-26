alunos = [('Renzo', 0), ('Luciano', 10), ('Ada', 9)]

# Ordenará a lista a partir do critério passado por lambda
alunos.sort(key=lambda aluno: aluno[1])

print(alunos)


def por_nome(aluno):
    return aluno[0]


# Retornará uma lista ordenada, baseada em key
print(sorted(alunos, key=por_nome))
