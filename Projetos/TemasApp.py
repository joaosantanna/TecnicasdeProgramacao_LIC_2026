import PySimpleGUI as sg

sg.theme('DarkTanBlue')
desenho = [
    [sg.Push(),sg.Text("Preview de Temas", font=('Arial 14')),sg.Push()],
    [
        sg.Push(), sg.Button("Temas"),sg.Button("Relogio"),
        sg.Button("Sair"), sg.Push()
    ]
]

janela = sg.Window("Visualizador de Temas", layout=desenho,
                   size=(450,100), font=('Arial 12'))

while True:

    evento, valores = janela.read()
    if evento in ("Sair", sg.WIN_CLOSED):
        break
    elif evento == "Temas":
        sg.theme_previewer(
            columns=8,
            scrollable=True,
            scroll_area_size=(None, None),
            search_string=None,
            location=(None, None),
        )
    elif evento == 'Relogio':
        sg.theme_previewer_swatches()

janela.close()
