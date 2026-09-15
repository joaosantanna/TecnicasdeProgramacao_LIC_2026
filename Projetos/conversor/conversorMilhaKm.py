import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def converter():
    '''
    converte  valor de milhas para kilometros
    '''
    valor = inputInt.get()
    km_out = valor * 1.61
    out_string.set(f'{km_out:.2f}')


# janela = tk.Tk()
janela = ttk.Window(themename='journal', title='Conversor')
janela.geometry('600x200')

# titulo
label = ttk.Label(janela, text='Milhas para kilometros',
                  font='Calibri 24 bold')
label.pack()

# inputs
frame = tk.Frame(janela)
inputInt = tk.IntVar()  # pega o valor como inteiro toda vez que modificar ele atualiza
entry = ttk.Entry(frame, textvariable=inputInt)
button = ttk.Button(frame, text='Converter', command=converter)
frame.pack(pady=10)
entry.pack(side=tk.LEFT, padx=10)
button.pack(side=tk.LEFT)

# outputs
out_string = tk.StringVar()
out_label = ttk.Label(
    janela,
    text='conversão',
    font='Calibri 24',
    textvariable=out_string)
out_label.pack()


# run
janela.mainloop()
