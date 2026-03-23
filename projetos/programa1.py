# 1. Faça um programa que peça dois números ao usuário e mostre qual o menor número.:
# as duas primeiras variaveis, para que o usuario digite os numeros para fazer comparação.

num1 = float(input("Digite o primeiro número a ser comparado: "))
num2 = float(input("Digite o segundo número a ser comparado: "))

print("Avaliando qual o menor número")


if num1 < num2:
    print("O menor número é:", num1)

elif num1 == num2:
    print("Os números são iguais")

else:
    print("O menor número é:", num2)

    # sempre que colocar numeros decimais, não esqueça de colocar com ponto, 
    # virgula nao funciona. Att. Alston