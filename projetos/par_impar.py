numero = float(input("Digite um número para ser verificado: "))
resto = numero % 2

if (numero <= 0):
    print("Você digitou um valor inválido!!!")
elif (resto != 0):
    print(f"{numero} é um número impar!")
else:
    print(f"{numero} é um número par!")