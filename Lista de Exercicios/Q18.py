# programa para calculo da tabuada de um numero

#entrada
while True:
    print('Programa tabuada')
    n = int(input('Digite um valor de n:'))
    if n >= 1 and n <= 10:
        break
    else:
        print('Erro - so aceito numero entre 1 e 10')
        
# processamento + saida
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')

# saida