# entradas

n = int(input('Informe o valor do mes correspondente:'))

# processamento + saida

meses ='janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'
meses = meses.split(' ')

if  n <= 0 or n > 12:
    print(f' Mes invalido')
else:    
    print(f'Mes correspondente ao {n} = {meses[n-1]}')