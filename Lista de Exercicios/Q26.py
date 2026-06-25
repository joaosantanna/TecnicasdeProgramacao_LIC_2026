print('Programa para determinar se um numero é primo')
n = int(input('Informe o numero a ser testado:'))
if n == 1 or n == 0:
    eh_primo = False
else:
    eh_primo = True

for i in range(2, n ):
    if n % i == 0:
        eh_primo = False
        break

if eh_primo == True:
    print(f' Numero {n} é um numero primo')
else:
    print(f'Numero {n} não é um numero primo') 