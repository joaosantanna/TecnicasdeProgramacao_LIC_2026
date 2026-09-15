import PySimpleGUI as sg


# sg.theme('LightGrey')
# sg.theme('LightBlue')
sg.theme('Reddit')
# sg.theme('Material1')
# sg.theme('DarkGrey2')
# Define the layout
layout = [
    [sg.Push(), sg.Text('Decimal para Binario', font='Calibre, 24'), sg.Push()],
    [sg.Push(), sg.Input('0', key='decimal', size=(10, 1), font='Calibre, 12'),
     sg.Button('Converter', font='Calibre, 12'), sg.Push()],
    [sg.Push(), sg.Text(key='output', font='Calibre, 18'), sg.Push()]
]

# Create the window

window = sg.Window('Decimal para Binario', layout,
                   size=(400, 150))

# Event loop

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Converter':
        try:
            decimal = int(values['decimal'])
            binario = bin(decimal)
            binario = str(binario)
            binario = binario[2:]
            window['output'].update(f'{binario}')
            window['decimal'].update('')
        except ValueError:
            pass

window.close()
