import PySimpleGUI as sg

sg.theme('Material 2')
# All the stuff inside your window.
layout = [  [sg.Text("Qual o seu nome?",enable_events=True )],
            [sg.InputText()],
            [sg.Button('Ok',bind_return_key=True), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Exemplo do Ola mundo', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    #if event == 'ok' or event ==

    print('Hello', values[0], '!')
    print(event)

window.close()