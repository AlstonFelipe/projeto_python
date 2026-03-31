"""
3 - faça um programa que leia 4 notas, 
mostre as notas e a media na tela
"""
lista = []
soma = 0

for var in range(4):
    numero = int(input("Digite as notas: "))
    lista.append(numero)
    soma += numero

media = soma / 4

print(f"As notas são {lista} e a média é: {media}")