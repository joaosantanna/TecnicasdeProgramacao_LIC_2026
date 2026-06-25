print( 'Tabela de conversao de temperturas')
print('C - F')
for c in range(0,101,10):
    print(f'{c} - {c*1.8 + 32}')
    # contas podem ser realizadas dentro de um print
    # desde que se esteja usando F-Strings
    # a conta de conversao de celcius é realizada dentro
    # do print.