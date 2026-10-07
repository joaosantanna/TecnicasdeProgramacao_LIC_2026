
estoque = [
    ["Teclado", 10, 150.0],
    ["Mouse", 0, 85.0],
    ["Monitor", 5, 900.0],
    ["Fone", 0, 120.0]
    ]
disponiveis=[]

for sublista in estoque:
    if sublista[1] > 0 :
        disponiveis.append(sublista)

print('Itens disponiveis na loja')
for item in disponiveis:
    print(item)