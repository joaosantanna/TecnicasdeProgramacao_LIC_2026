from math import pi
print(pi)

xi = 3 # variavel que contem o valor aproximado de pi
print(f'1 - 3 - erro ={pi - 3}')

d = 2
for i in range(1,15):
    
    if i % 2 != 0:
        # itercao impar
        t = 4/(d*(d+1)*(d+2)) # calcula o termo
        d += 2 # incrementa o divisor para o proximo termo
        xi += t # adiciona o termo ao valor do pi aproximado xi
        print(f'{i+1} - {xi} - erro ={pi - xi}')
    else:
        #itercao par
        t = -4/(d*(d+1)*(d+2))
        d += 2
        xi += t
        print(f'{i+1} - {xi} - erro ={pi - xi}')