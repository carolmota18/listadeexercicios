def contar_palavras (palavras):
    lista = palavras.split(' ')
    dicionario = {}
    
    for palavra in lista:
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra)
    return dicionario

frutas = 'Uva  Uva Maça Maça Maça Pera Pera Banana '

print('Quantidade de frequencia')
print('-'*100)
print(contar_palavras(frutas))