def calcular_medias(notas: dict):
    lista_medias = []
     
    for chave, valor in notas.items():
        media = (valor[0] + valor[1] + valor[2]) / len(valor)
        lista_medias.append((chave,media))
    return lista_medias
notas = {'Samuel': [10,10,10], 'Karynne':[10,10,10], 'Suelem':[2,2,8]}

print(calcular_medias(notas))