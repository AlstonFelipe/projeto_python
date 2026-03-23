# 2. Faça um programa que receba um número inteiro e diga se ele é par ou ímpar.

num1 = int(input("Digite um numero e saberemos se ele é par ou impar"))

# para verificar se o numero é par ou impar ele tem que ser divisivel por dois ou igual a zero.
"""
num1 é o número que você digitou
% ele pega o resto da divisão
num1 % 2 divide o número por 2 e pega o resto
== 0 verifica se o resto é igual a 0

"""
if num1 % 2 == 0:
    print("O número digitado é par")

elif num1 % 2 == 1:
    print("O número digitado é ímpar")

else:
    print("Informação digitada é inválida")