print('Programa para detectar palindromos')
frase = input('Digite a frase:')

frase = frase.lower()
# coloca a frase toda em minuscula para não dar problema
# na hora de inverter a frase

original = list(frase) # transforma a frase em uma lista com
# todas as letras como elementos dessa lista

numero_espacos = original.count(' ')
# conta o numero de espaços em branco na frase
# os espacos em branco tem que ser retirados antes de
# fazer a inversao da lista para não dar problema na hora
# de comparar

for i in range(numero_espacos): # remove todos os espacos
    original.remove(' ')

copia = original.copy() # copia a lista original
copia.reverse() # inverte a copia da lista 

print(original)
print(copia)

if original == copia : # compara as duas listas
    print(f' a frase {frase} é um palindromo')
else:
    print(f' a frase {frase} NAO é um palindromo')
