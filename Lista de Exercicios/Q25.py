# precisa melhorar ele gera multiplas listas desnecessariamente
def fib(n):
    lfib = [1,1]
    t1 = 1
    t2 = 1
    for i in range(n - 2):
        t3 = t1 + t2
        lfib.append(t3)
        t1,t2 = t2,t3
    return lfib

n = 10
t = fib(n)[-1]
while t < 1000:
    n += 1
    r = fib(n)
    t = r[-1]

r.pop() # tira o ultimo termo pois passou de 1000
print(r)
soma = 0
print('Pares --->',end=' ')
for n in r:
    if n % 2 == 0:
        print(n,end=',')
        soma += n
print()
print(f'A soma dos pares na serie de fibonacci menores que 1000 = {soma}')


    
    