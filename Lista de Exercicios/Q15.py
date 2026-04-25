peso = float(input('Informe seu peso :'))
altura = float(input('Informe sua altura:'))

imc = peso/altura**2
print(f'Seu IMC = {imc:.2f}')

if imc < 20:
    print('Abaixo do peso ideal')
elif  imc >= 20 and imc < 25:
    print('Peso ideal')
else:
    print('sobre peso')
    print('''
            Calculo de quantos quilos vc
            precisa perder para ficar com
            o peso saudavel \n''')
    
    peso_ideal = 25 *altura**2
    perda = peso - peso_ideal
    print(f'voce precisa perder {perda:.2f} kg')
    print(f'Seu peso ideal para a sua alura seria {peso_ideal:.2f} kg')
    
    
