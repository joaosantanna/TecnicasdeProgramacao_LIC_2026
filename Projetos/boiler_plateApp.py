import PySimpleGUI as sg

sg.theme('Reddit')
# All the stuff inside your window.
layout = [  [sg.Text("Bom dia, qual seu nome?",enable_events=True )],
            [sg.InputText(key='-NOME-')],
            [sg.Text(key='-RESULTADO-')],
            [sg.Button('Ok',bind_return_key=True), sg.Button('sair')] ]

# Create the Window
janela = sg.Window('Ola Mundo', layout = layout, font=('Arial', 12))
while True:
    event, valores = janela.read()

# Event Loop to process "events" and get the "values" of the inputs

while True:
    evento, valores = janela.read()


    if evento == sg.WIN_CLOSED or evento == 'sair':
        break
    if evento == 'Ok':
        nome = valores['-NOME-']
        janela['-RESULTADO-'].update(f'Bom dia {nome}')

janela.close()