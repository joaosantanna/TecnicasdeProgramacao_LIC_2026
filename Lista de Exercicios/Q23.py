from random import randint

maior = 0
menor = 1000
#entrada + processamento
for i in range(50):
    n = randint(1,100)
    print(n , end='\t')
    if n > maior:
        maior = n
    if n < menor:
        menor = n

# saida
print()
print(f'Maior numero sorteado = {maior}')
print(f'Menor numero sorteado = {menor}')

