import PySimpleGUI as sg
from pathlib import Path

diretorio_base = Path.cwd()
subpasta = "imagem"
nome_arquivo = "temperatura.png"
caminho_completo = diretorio_base / subpasta / nome_arquivo

#sg.theme('Reddit')

# All the stuff inside your window.
layout = [
            [sg.Push(), sg.Image(filename=caminho_completo), sg.Push()],
            [sg.Text("Conversor de Temperatura",enable_events=True )],
            [sg.Text('Celcius:'),sg.InputText(key='-TEMPERATURA-')],
            [sg.Text('Fahrenheit :', key='-TEMP_FHREHEIT-')],
            [sg.Text('Kelvin :', key='-TEMP_KELVIN-')],
            [sg.Button('Converter',bind_return_key=True), sg.Button('sair',size=(8,1))] ]

# Create the Window
janela = sg.Window('Conversor de temperatura', layout = layout, font=('Arial', 12))
while True:
    evento, valores = janela.read()

    if evento in (sg.WIN_CLOSED, 'sair'):
        break
    if evento == 'Converter':
        temp = float(valores['-TEMPERATURA-'])
        f = (temp * 1.8) + 32
        k = temp + 273
        janela['-TEMP_FHREHEIT-'].update(f'Fahrenheit : {f:.2f}')
        janela['-TEMP_KELVIN-'].update(f'Kelvin : {k:.2f}')
janela.close()