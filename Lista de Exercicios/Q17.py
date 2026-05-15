# programa para calcular o fatorial de um numero

# entradas
print('Programa para calculo de fatorial')
n = int(input('Digite o numero para o calculo:'))
# processamento
fat = 1
for i in range(n,0,-1):# comeca em n termina em 1
    fat = fat * i
# saida
print(f'o fatorial de {n}! = {fat}')