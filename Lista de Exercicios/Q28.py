# entradas - um numero n maior de zero

n = int(input('Digite o valor de n:'))

soma = 0

for i in range(1,n+1):
    termo = i/(i+1)
    soma += termo

print(f'A serie com n valendo {n} , a soma = {soma:.2f}')
    
    