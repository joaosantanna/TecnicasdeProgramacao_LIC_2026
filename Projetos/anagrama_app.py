import PySimpleGUI as sg
from util_anagrama import processar_anagrama

sg.theme('Reddit')
desenho =[
        [sg.Push(),sg.Text('Detector de Anagramas',font=('Forte',26)),
         sg.Push()],
        [sg.Text('Palavra 1:'), sg.InputText(key='-P1-')],
        [sg.Text('Palavra 2:'), sg.InputText(key='-P2-')],
        [sg.Text('>>>', key='-MENSAGEM-')],
        [sg.Button('Processar'),sg.Button('Limpar',size=(9,1)),
         sg.Button('Sair',size=(9,1))]
    ]

janela = sg.Window('Anagrama App', layout=desenho,
                   font=('Helvetica',16))

while True:
    evento,valores = janela.read()
    if evento in ('Sair',sg.WIN_CLOSED):
        break
    
    if evento == 'Processar':
        p1 = valores['-P1-']
        p2 = valores['-P2-']
        eh_anagrama = processar_anagrama(p1,p2)
        if eh_anagrama:
            janela['-MENSAGEM-'].Update(f'>>> {p1} e {p2} são anagramas')
        else:
            janela['-MENSAGEM-'].Update(f'>>> {p1} e {p2} não são anagramas')
        
    
    if evento == 'Limpar':
        janela['-P1-'].Update('')
        janela['-P2-'].Update('')

janela.close()
    
    