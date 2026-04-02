"""
3.Numa eleição existem três
candidatos: Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""


Rhenam = 0
Lucas = 0
Daniel = 0

eleitores = int(input("Digite o numero de eleitores: "))

while eleitores > 0:
    voto = input("Digite o numero do Candidato: \n 1. Rhenam \n 2. Lucas Luz \n 3. Daniel: ")
    if voto == "1" or voto == "Rhenam":
        Rhenam += 1
    elif voto == "2" or voto == "Lucas":
        Lucas += 1
    elif voto == "3" or voto == "Daniel":
        Daniel += 1
    else:
        print("Por isso o Brasil nao vai pra frente, nem sabe votar. Tente novamente.")
        
    eleitores -= 1  
print("\n Resultado da eleição:")
print(f"O candidato Rhenam recebeu: {Rhenam} votos")
print(f"O candidado Lucas Luz recebeu: {Lucas} votos")
print(f"O candidato Daniel Recebeu: {Daniel} votos")



