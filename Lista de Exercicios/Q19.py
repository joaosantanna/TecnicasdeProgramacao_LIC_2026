# programa para achar os divisores de um numero inteiro

# entrada
print('Programa para achar os divisores de um numero ')
n = int(input('Digite um valor de n:'))

# processamento
contador = 0
for i in range(1,n+1):
    if n % i == 0:
        print(f'divisor de {n} = {i}')
        contador = contador + 1

# saida
print(f'o numero {n} tem {contador} divisores')