def eh_primo(n):
    if n == 1 :
        return False
    for i in range(n-1,1,-1):
        if n % i == 0:
            return False
    return True

soma = 0
print('Numeros primos entre 100 e 200')
for i in range(100,201):
    if eh_primo(i):
        print(i)
        soma += i

print(f'A soma dos primos entre 100 e 200 = {soma}')