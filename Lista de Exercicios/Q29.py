# entrada - um n que vai ser o limite superior

n = int(input('Digite um valor de n:'))

# processamento
print(f'Numeros perfeitos entre 1 e {n}')
for i in range(1,n+1):
    dobro = 2*i 
    soma = 0
    for x in range(1,i+1):
        if i % x == 0:
            soma += x
    
    if soma == dobro:
        print(i) # saida
    
