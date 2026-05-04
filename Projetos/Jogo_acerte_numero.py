# Jogo que sorteia um numero que eu tenho que acertar
from random import randint

segredo = randint(1,100)
numero_jogadas = 0
print('Jogo do acerte o numero')
while True:
    numero = int(input('Chute um numero:'))
    numero_jogadas += 1
    if numero == segredo:
        print(f' Vc acertou em {numero_jogadas}')
        break
    else:
        print(f'Voce errou , continue tentando')
        print(f'Numero de jogadas = {numero_jogadas}')
        if segredo > numero:
            print(f'numero é maior que {numero}')
        else:
            print(f'numero é menor que {numero}')

print('Bye Bye')
