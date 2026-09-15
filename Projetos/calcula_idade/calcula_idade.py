from datetime import date


def calculo_idade(ano):
    hoje = date.today()
    anos = hoje.year - ano
    return anos
