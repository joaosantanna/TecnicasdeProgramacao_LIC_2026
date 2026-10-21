import PySimpleGUI as sg
from util import *
from faker import Faker


agenda =[]
            
    
fake = Faker('pt_Br')


lista_nomes= atualizar_listagem(agenda)
sg.theme('Reddit')
# All the stuff inside your window.
desenho = [
            [sg.Push(),sg.Text('Agendinha', font=('Helvetica',20)),sg.Push() ],
            [sg.Text('Nome:',size=(10,1)),sg.InputText(key='-NOME-')],
            [sg.Text('Telefone:',size=(10,1)),sg.InputText(key='-TELEFONE-')],
            [sg.Push(),sg.Listbox(lista_nomes,key='-LISTA-',
                        size=(30,10),enable_events=True), sg.Push()],
            [sg.Push(),sg.Button('Novo',size=(10,1)),sg.Button('Apagar',size=(10,1)),
             sg.Button('Atualizar', size=(10,1)), sg.Push(),
             sg.Button('Novo Automatico')]
        ]

# Create the Window
janela = sg.Window('Ola Mundo', layout = desenho, font=('Arial', 12))
while True:
    evento, valores = janela.read()


    if evento == sg.WIN_CLOSED :
        break
    
    if evento == 'Novo':
        nome = valores['-NOME-']
        tel = valores['-TELEFONE-']
        novo_contato(nome,tel,agenda)
        janela['-NOME-'].update('')
        janela['-TELEFONE-'].update('')
        #sg.Popup('Contato adicionado com sucesso')
        lista_nomes = atualizar_listagem(agenda)
        janela['-LISTA-'].update(lista_nomes)
    
    if evento == 'Apagar':
        nome = valores['-LISTA-'][0]
        resultado = apagar_contato(nome,agenda)
        lista_nomes = atualizar_listagem(agenda)
        janela['-LISTA-'].update(lista_nomes)
    
    if evento == '-LISTA-':
        nome = valores['-LISTA-'][0]
        contato = buscar_contato(nome,agenda)
        janela['-NOME-'].update(contato['nome'])
        janela['-TELEFONE-'].update(contato['telefone'])
        
    if evento == 'Atualizar':
        nome = valores['-LISTA-'][0]
        novo_nome = valores['-NOME-']
        novo_tel = valores['-TELEFONE-']
        atualizar_contato(nome,novo_nome,novo_tel,agenda)
        lista_nomes = atualizar_listagem(agenda)
        janela['-LISTA-'].update(lista_nomes)
    if evento == 'Novo Automatico':
        nome = fake.name()
        tel = fake.phone_number()
        novo_contato(nome,tel,agenda)
        janela['-NOME-'].update('')
        janela['-TELEFONE-'].update('')
        #sg.Popup('Contato adicionado com sucesso')
        lista_nomes = atualizar_listagem(agenda)
        janela['-LISTA-'].update(lista_nomes)
        
        
        
janela.close()
