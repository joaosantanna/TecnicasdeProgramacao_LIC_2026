# programa para achar somar os multiplos de 7 entre 100 e 200


# entrada nao tem

# processamento
soma = 0
for i in range(100,201):
    if i % 7 == 0:
        soma = soma + i
        print(f' Multiplo de 7 - {i}')
        
print(f'Soma dos multiplos de 7 entre 100 e 200 = {soma}')        