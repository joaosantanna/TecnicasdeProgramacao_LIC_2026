from pathlib import Path
import pickle

contatos=[]


if Path("agenda.bin").is_file():
  # carregar o arquivo para a memoria
    try:
        with open('agenda.bin','rb') as file:
            contatos = pickle.load(file)
                    
    except Exception as e:
        print(e)
            
    else:
        print('Arquivo carregado com sucesso')
  

while True:
    
    print('''

                Agendinha versao texto - CRUD
                0-sair
                1-novo contato
                2-listar contatos
                3-apagar contato
                4-editar contato
                
    ''')
    op = int(input('Digite a sua opção:'))
    
    match op:
        
        case 0:
            # rodar rotina para salvar os dados antes de sair do programa
            try:
                with open('agenda.bin','wb') as file:
                    pickle.dump(contatos, file)
                    
            except Exception as e:
                print(e)
            
            else:
                print('Arquivo Salvo com sucesso')
                print('Bye bye')
            break # sai do programa
        
        case 1:
            print('Novo contato')
            nome = input('Nome:')
            tel = input('Telefone:')
            contato = {'nome':nome , 'telefone':tel}
            contatos.append(contato)
        case 2:
            print('Listando contatos')
            for p,c in enumerate(contatos):
                print(f"{p} - {c['nome']} :{c['telefone']}  ")
        
        case 3:
            print('Apagar Contato - listando ...')
            for p,c in enumerate(contatos):
                print(f"{p} - {c['nome']} :{c['telefone']}  ")
            
            posicao = int(input('Informe a posicao a ser deletada:'))
            try:
                contatos.pop(posicao)
            except IndexError:
                print('Erro - posição não existe na agenda')
        
        case 4:
            print('Editar Contato - listando ...')
            for p,c in enumerate(contatos):
                print(f"{p} - {c['nome']} :{c['telefone']}  ")
            
            posicao = int(input('Informe a posicao a ser editada:'))
            contato = contatos.pop(posicao)
            print(f"Nome:{contato['nome']} - tecle enter para manter ou digite novo valor")
            nome = input(':')
            if nome != '':
                contato['nome'] = nome
            
            print(f"Telefone:{contato['telefone']} - tecle enter para manter ou digite novo valor")
            tel = input(':')
            if tel != '':
                contato['telefone'] = tel
                
            contatos.insert(posicao,contato)# insere o contato na mesma posicao em que ele estava
            print('Contato editado com sucesso')
                
                               
        case _:
            print('Opção invalida')