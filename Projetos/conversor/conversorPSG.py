import PySimpleGUI as sg


sg.theme('Reddit')

# Define the layout
layout = [
    [sg.Push(), sg.Text('Conversor', font='Calibre, 24'), sg.Push()],
    [sg.Text('Milhas para Kilometros'), sg.Input( key='-MILHAS-', size=(5,1)), sg.Text(key='-MILHA_KM-')],
    [sg.Text('Decimal para Binario'), sg.Input( key='-DECIMAL-', size=(5,1)), sg.Text(key='-DECIMAL_BINARIO-')],
    [sg.Push(),sg.Button('Converter', font='Calibre, 12'), sg.Push()]
]

# Create the window

janela = sg.Window('Conversor de medidas', layout, size=(400, 150))

# Event loop

while True:
    event, values = janela.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Converter':
        if values['-MILHAS-'] != '':
            milhas = float(values['-MILHAS-'])
            kilometros = milhas * 1.61
            janela['-MILHA_KM-'].update(f'{kilometros:.2f} Km')
        
        if values['-DECIMAL-'] != '':
            decimal = int(values['-DECIMAL-'])
            binario = bin(decimal)
            binario = str(binario)
            binario = binario[2:]
            janela['-DECIMAL_BINARIO-'].update(f'{binario}')
            
        

janela.close()
