import PySimpleGUI as sg


# sg.theme('LightGrey')
sg.theme('LightBlue')
#sg.theme('Reddit')
# sg.theme('Material1')
# Define the layout
layout = [
    [sg.Push(), sg.Text('Milhas para Kilometros', font='Calibre, 24'), sg.Push()],
    [sg.Push(), sg.Input( key='milhas', size=(10, 4), font='Calibre, 12'),
     sg.Button('Converter', font='Calibre, 12'), sg.Push()],
    [sg.Push(), sg.Text(key='output', font='Calibre, 18'), sg.Push()]
]

# Create the window

window = sg.Window('Milhas para Kilometros', layout, size=(400, 150))

# Event loop

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Converter':
        try:
            milhas = float(values['milhas'])
            kilometros = milhas * 1.61
            window['output'].update(f'{kilometros:.2f} Km')
            window['milhas'].update('')
        except ValueError:
            pass

window.close()
