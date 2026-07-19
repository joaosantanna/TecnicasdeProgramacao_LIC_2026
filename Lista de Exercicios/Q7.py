# entradas p,l,c

profundidade = float(input('Informe a profundidade da piscina(m):'))
comprimento = float(input('Informe o comprimento da piscina(m):'))
largura = float(input('Informe a largura da piscina(m):'))

# processamento

volume = profundidade* comprimento * largura

tempo = volume/20

# saida
print(f'O volume da piscina = {volume} metros cubicos')
print(f'Tempo para encher a piscina = {tempo} minutos')

