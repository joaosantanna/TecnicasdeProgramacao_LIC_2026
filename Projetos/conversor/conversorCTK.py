import customtkinter as ctk


# funcoes

def converter():
    '''
    Funcao que converte uma entrada de milhas( float)
    para Kilometros 
    '''
    valor = float(entry.get())
    km_out = valor * 1.61
    km_out = f'{km_out:.2f}'
    output.configure(text=km_out)


janela = ctk.CTk()

janela.geometry('400x150')

label = ctk.CTkLabel(janela, text='Decimal para Binario',
                     font=('Calibri', 24))
label.pack()

# inputs

entry = ctk.CTkEntry(janela)
entry.pack()

output = ctk.CTkLabel(janela, font=('Calibri', 24),
                      text='Milhas para Km')
output.pack()

botao = ctk.CTkButton(janela, text='converter', command=converter)
botao.pack()

janela.mainloop()
