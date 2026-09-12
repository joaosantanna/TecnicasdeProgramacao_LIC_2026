import PySimpleGUI as sg
from random import randint
from pathlib import Path

diretorio_base = Path.cwd()
subpasta = "imagem"
nome_arquivo = "acerteNumero.png"
caminho_completo = diretorio_base / subpasta / nome_arquivo
sg.theme('Reddit')
segredo = randint(1,100)
numero_jogadas = 0

# All the stuff inside your window.
layout = [
            [sg.Push(), sg.Image(filename=caminho_completo), sg.Push()],
            [sg.Text("Jogo do acerte o numero?",enable_events=True )],
            [sg.InputText(key='-NUMERO-')],
            [sg.Text( key='-RESULTADO-')],
            [sg.Text(f'Numero de jogadas: {numero_jogadas}',key='-NUMERO_JOGADAS-')],
            [sg.Button('Ok',bind_return_key=True), sg.Button('sair')] ]

# Create the Window
janela = sg.Window('Jogo do acerte o numero', layout=layout , font=('Arial',14))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = janela.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'sair':
        break
    if event == 'Ok':
        numero = int(values['-NUMERO-'])
        numero_jogadas += 1
        if numero == segredo:
            janela['-RESULTADO-'].update(f' Vc acertou !!!!')
            janela['-NUMERO_JOGADAS-'].update(f'Numero de jogadas: {numero_jogadas}')

        else:
            if segredo > numero:
                janela['-RESULTADO-'].update(f'Voce errou,numero é maior que {numero}')
            else:
                janela['-RESULTADO-'].update(f'Voce errou,numero é menor que {numero}')

            #atualiza o numero de jogadas em caso de erro
            janela['-NUMERO_JOGADAS-'].update(f'Numero de jogadas: {numero_jogadas}')

janela.close()