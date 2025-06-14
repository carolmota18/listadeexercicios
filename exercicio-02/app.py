def ordernar_tuplas(lista_tuplas):
    lista_odernada = sorted(lista_tuplas,key=lambda tupla:tupla[1])
    return lista_odernada

lista = [('Samuel',3), ('Karynne',20),('Carol',22),('Suelem',21),('Romulo',15)]

print(f'AS tuplas ordernadadas por idade:{ordernar_tuplas(lista)}')
