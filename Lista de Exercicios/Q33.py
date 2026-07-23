
print('''  Numeros divisiveis por 7 e que não são
multiplos de 5 no intervalo de 2000 a 3200 \n''')
for i in range(2000,3201):
    if i % 7 == 0 and not(i % 5 == 0):
        print(i, end='\t') 
        