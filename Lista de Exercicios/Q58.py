print('Detector de anagrama')
p1 = input('Informe a primeira palavra:')
p2 = input('Informe a segunda palavra:')
p1 =p1.lower()
p2 = p2.lower() 
print('... analisando ...')
l1 = list(p1)
l2 = list(p2)
s1 = set(l1)
s2 = set(l2)
eh_anagrama = True
if s1 != s2:
    eh_anagrama = False
elif s1 == s2:
    for letra in s1:
        if l1.count(letra) != l2.count(letra):
            eh_anagrama = False
            break
if eh_anagrama:
    print(f'{p1} e {p2} são anagramas')
else:
    print(f'{p1} e {p2} não são anagramas')

