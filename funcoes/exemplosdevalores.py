# ==== EXEMPLOS DE COMANDOS PRA SE USAR COM LISTAS ====

lista = [4,5,3,5]
print(lista)
# [4,5,3,5]

lista.append(2)
# [4,5,3,5,2]

lista.insert(2,-3)
# [4,5,-3,3,5]

lista.remove(4)
# [5,3,5]

lista.sort()
# [3,4,5,5]

lista.reverse()
# [5,3,5,3]

print(lista.count(5)) # Count = contagem 
#2

print(lista.pop()) # Pop Mostra qual o ite mais dominante da lista 
#5

print(lista)
# [4,5,3]

lista.sort() # Sort: organiza a minha lista
# [3,4,5,5]

del lista[2]
# [4,5,5]

del lista[2:5]
# [4,5]

lista.clear()
# []
