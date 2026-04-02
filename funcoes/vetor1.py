"""
1- Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

"""
numeros = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
print("\nOs números digitados foram:")
for num in numeros:
    print(num)

    