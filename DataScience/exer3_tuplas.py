""" crie uma tupla numeros = (5, 10, 15, 20) e converta-a em um alista.
adicione o numero 25 a lista resultante depois volte a lista para a dupla
e print ela"""

numeros = (5, 10, 15, 20)
lista_numeros = list(numeros)   
lista_numeros.append(25)
numeros = tuple(lista_numeros)
print(numeros)

