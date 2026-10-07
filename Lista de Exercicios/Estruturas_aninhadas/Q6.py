inventario = {
    "armas": ["espada", "arco"],
    "pocoes": {"cura": 5, "mana": 2},
    "ouro": 150
    }

lista_armas = inventario['armas']
lista_armas.append('adaga')
inventario['pocoes']['cura'] -= 1
print(inventario['armas'])
print(inventario['pocoes'])
print(inventario['ouro'])