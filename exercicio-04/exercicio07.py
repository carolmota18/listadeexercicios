def to3_frequentes(numeros: list):
    frequencia = {}
    
    for numero in numeros:
        if numero in frequencia:
            frequencia[numero] +=1
        else:
            frequencia[numero] = 1
            
    numeros_ordernados = sorted(frequencia.keys(), key=lambda x:
        (frequencia[x], x),reverse=True
        )
    return numeros_ordernados[:3]

numeros = [1,1,1,1,2,3,3,3,4,4,5,5,5]

print(to3_frequentes(numeros))


