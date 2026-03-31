"""
2 - faça um programa que leia um vetor de 10 numeros reais e mostre-os na ordem inversa
"""


lista = []

for i in range(10):
    numero = int(input("Digite um numero real: "))
    lista.append(numero)

lista.reverse()

print("Lista na ordem inversa:")
print(lista)