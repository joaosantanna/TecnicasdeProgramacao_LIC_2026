nome = input('Digite o nome do aluno:')
idade = input('Informe a idade do aluno:')
notas =[]
for i in range(4):
    n = float(input(f'Nota {i+1}:'))
    notas.append(n)
    
ficha_aluno = {'nome':nome, 'idade':idade, 'notas':notas}
media = sum(ficha_aluno['notas'])/4
print('Tabela de dados do aluno')
print(f"{ficha_aluno['nome']} - {ficha_aluno['idade']}")
for i in range(4):
    print(f"{ficha_aluno['notas'][i]}")
print(f'Media do alunos = {media}')