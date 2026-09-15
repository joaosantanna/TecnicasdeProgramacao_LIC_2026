'''
aplicativo para calcular a idade do usuario
biblioteca externa utilizada : PySimpleGUI versao 6
data: 15/09/2026
autor: João Santanna
'''
import PySimpleGUI as sg
import sys
from calcula_idade import calculo_idade
from pathlib import Path

sg.theme('Reddit')

# comandos necessarios para o carregamento da imagem no app
diretorio_base = Path.cwd()
subpasta = "imagem"
nome_arquivo = "img_idade.png"
caminho_completo = diretorio_base / subpasta / nome_arquivo

layout = [
            [sg.Push(),sg.Image(filename=caminho_completo), sg.Push()],
            [sg.Text('Programa para calcular idade ')],
            [sg.Text('Ano Nascimento:'), sg.InputText(key='-ANO-')],
            [sg.Text('Resultado:', key='-RESULTADO-', size=(30, 1))],
            [sg.Button('Calcular', size=(10, 1),bind_return_key=True), sg.Button('sair', size=(10, 1))]]

# Create the Window
window = sg.Window('Calculadora de Idade', layout=layout, font=('Helvetica', 14))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    evento, values = window.read()
    if evento in ( sg.WIN_CLOSED, 'sair'):  # if user closes window or clicks cancel
        break
    if evento == 'Calcular':
        ano = int(values['-ANO-'])
        valor = calculo_idade(ano)
        window['-RESULTADO-'].Update(f'Resultado: sua idade é de {valor} anos')

window.close()
sys.exit(0)
