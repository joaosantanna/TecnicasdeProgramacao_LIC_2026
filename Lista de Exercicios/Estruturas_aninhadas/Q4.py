dados_mistos = [
    [1, 2],
    [3],
    [4, 5, 6],
    [7, 8]
    ]
lista_achatada = list()
for sublista in dados_mistos:
    for numero in sublista:
        lista_achatada.append(numero)

print(lista_achatada)
