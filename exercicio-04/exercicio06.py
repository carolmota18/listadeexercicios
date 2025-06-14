dicionario1 = {'A': 1, 'B':2,'C':7}
dicionario2 = {'A': 3, 'B':5,'C':2}

def combinar_dicts(d1: dict, d2: dict):
    novo_dicionario = {}
    for chave, valor in d1.items():
        novo_dicionario[chave] = valor
    for chave, valor in d2.items():
        if chave in novo_dicionario.keys():
            novo_dicionario[chave] += valor
        else:
            novo_dicionario[chave] = valor
    return novo_dicionario

print(f'Esse é o dionario1:{dicionario1}')
print('-'*100)
print(F'Esse e o novo dicionario:{combinar_dicts(dicionario1,dicionario2)}')
    
