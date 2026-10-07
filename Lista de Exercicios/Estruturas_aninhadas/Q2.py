def verificar_diagonal_principal(tab):
    jogador = tab[0][0]
    for l in range(3):
        if tab[l][l] != jogador:
            return False
    return jogador
            
        

tabuleiro = [
    ["X", ".", "O"],
    ["O", "X", "."],
    [".", ".", "X"]
    ]

resultado = verificar_diagonal_principal(tabuleiro)
if resultado != False:
    print(f' Ganhador = {resultado}')
else:
    print('Não teve ganhador na diagonal principal')



