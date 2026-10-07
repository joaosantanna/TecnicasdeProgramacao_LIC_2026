leituras = [
    [22, 25, 19, 21],
    [30, 32, 31, 29],
    [15, 18, 14, 17]
    ]
    
medias = []

for sublista in leituras:
    medias.append(sum(sublista)/len(sublista))
for p,v in enumerate(medias):
    print(f'{p + 1} -{v:.2f}')
posicao = medias.index(max(medias))
print(f' A cidade que tem a maior media = {posicao + 1}')

'''
# versao classica alternativa ...
for l in range(3):
    soma = 0
    for c in range(4):
        soma += leituras[l][c]
    medias.append(soma/4)
'''        