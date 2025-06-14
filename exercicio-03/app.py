def counter(palavras):
    lista = palavras.split(' ')
    dicionario = {}
    
    for palavra in lista:
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra)
    return dicionario

linguagens = 'Java Java Java Javascript Pyton Ruby Ruby Cobol Java Javascipt Pyton'

print('Quantidade de frequencia')
print('-'*100)
print(counter(linguagens))