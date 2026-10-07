alunos = {
    "Ana": {"Mat": 8.5, "Prog": 9.0},
    "Bruno": {"Mat": 6.0, "Prog": 7.5},
    "Carla": {"Mat": 9.5, "Prog": 10.0}
    }

nome = input('Informe o nome do aluno:')
notas = alunos.get(nome)
if notas != None:
    media = sum(notas.values())/len(notas.values())
    print(f'Media aluno {nome} = {media}')
else:
    print('aluno não encontrado')