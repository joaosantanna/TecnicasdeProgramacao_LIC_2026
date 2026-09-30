from random import randint
d = {}
for i in range(2,13):
    d[i]= 0
#print(d)
for i in range(1000):
    n1 = randint(1,6)
    n2 = randint(1,6)
    n = n1 + n2
    d[n] += 1
for k,v in d.items():
    print(f'{k} - {v} - {v/10}%')

