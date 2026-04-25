# esse programa equivale a 5 questao do lista
# isso é um comentario de 1 linha

'''
comentario de multiplas linhas
Escreva um programa que calcule área de um quadrado,
área de um trapézio e a área de um triângulo e informe
qual tem maior área.

'''
lado_quadrado = float(input('Informe o lado do quadrado:'))
area_quadrado = lado_quadrado**2

base_triangulo = float(input('Informe a base do triangulo:'))
altura_triangulo = float(input('Informe a altura do triangulo:'))
area_triangulo = (base_triangulo*altura_triangulo)/2

base_maior = float(input('Informe a base maior do trapezio:'))
base_menor = float(input('Informe a base menor do trapezio:'))
altura_trapezio = float(input('Informe a altura do trapezio:'))
area_trapezio = ( base_maior + base_menor) * altura_trapezio/2

print(f' Area do quadrado = {area_quadrado}')
print(f' Area do triangulo = {area_triangulo}')
print(f' Area do trapezio = {area_trapezio}')


if area_quadrado > area_trapezio and area_quadrado > area_triangulo:
    print('Area do quadrado é a maior')
elif area_triangulo > area_quadrado and area_triangulo > area_trapezio:
    print('Area do triangulo é a maior')
else:
    print('Area do trapezio é a maior')
    
# forma alternativa
maior = max(area_quadrado,area_trapezio,area_triangulo)
if maior == area_quadrado:
    print('Area do quadrado é a maior')
elif maior == area_triangulo:
    print('Area do triangulo é a maior')
else:
    print('Area do trapezio é a maior')
    
# forma alternativa 2

if area_quadrado > area_triangulo > area_trapezio:
    print('Area do quadrado é a maior')
elif area_triangulo > area_quadrado > area_trapezio:
    print('Area do triangulo é a maior')
else:
    print('Area do trapezio é a maior')
    
    
    
    