# programa que processa uma frase e informa o numero de vogais

frase = input('Digite sua frase:')
quantidade_vogais = 0

for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        quantidade_vogais = quantidade_vogais + 1
        #quantidade_vogais += 1
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        quantidade_vogais += 1
        
print(f'A quantidade de vogais na frase = {quantidade_vogais}')


quantidade_vogais = 0
for letra in frase:
    if letra in 'aeiouAEIOU':
        quantidade_vogais += 1
print(f'A quantidade de vogais na frase = {quantidade_vogais}')

