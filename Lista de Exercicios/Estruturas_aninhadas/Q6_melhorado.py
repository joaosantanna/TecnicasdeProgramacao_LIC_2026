inventario = {
    "armas": ["espada", "arco"],
    "pocoes": {"cura": 5, "mana": 2},
    "ouro": 150
    }

while True:
    print('''
                   Mini RPG
            0 - sair
            1 - adicionar arma ao inventario
            2 - atualizar pocoes ou mana
            3 - Informar total de ouro
            4 - Mostrar inventario
    ''')
    op = int(input('>>'))
    
    if op == 0:
        break
    elif op == 1:
        lista_armamento = inventario['armas']
        nova_arma = input('Informe a nova arma:')
        lista_armamento.append(nova_arma)
        print(inventario['armas'])
    elif op == 2:
        p = inventario['pocoes']
        opcao = input('atualizar mana ou cura:')
        valor = int(input('valor:'))
        p[opcao] += valor
        print(inventario['pocoes'])
    
    elif op == 3:
        print(f'Quantidade de ouro {inventario["ouro"]}')
    
    elif op == 4:
        print(f'''
                    Inventario
                    
                    Armas - {inventario["armas"]}
                    Poções - {inventario["pocoes"]}
                    ouro - {inventario["ouro"]}
            ''')
        
        
    else:
        print('Comando não cadastrado')
    