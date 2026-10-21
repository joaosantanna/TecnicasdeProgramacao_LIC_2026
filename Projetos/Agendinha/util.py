def novo_contato(nome, telefone, agenda):
    contato = {'nome':nome , 'telefone':telefone}
    agenda.append(contato)


def atualizar_listagem(agenda):
    lista_nomes =[]
    for contato in agenda:
        nome = contato['nome']
        lista_nomes.append(nome)
    return lista_nomes

def apagar_contato(nome,agenda):
    for posicao, contato in enumerate(agenda):
        if contato['nome'] == nome:
            agenda.pop(posicao)
            return 0
    return -1 # erro contato nao achado para apagar

def buscar_contato(nome,agenda):
    for contato in agenda:
        if contato['nome'] == nome:
            return contato
    return -2 # erro contato não encontrado na busca
    
def atualizar_contato(nome_antigo, novo_nome, novo_tel,agenda):
    for contato in agenda:
        if contato['nome'] == nome_antigo:
            contato['nome'] = novo_nome
            contato['telefone'] = novo_tel
            return 0
    return -3 # contato nao atualizado
    
    
    
    
    