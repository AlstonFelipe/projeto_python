"""
2- Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
inversa.

"""
numeros = []
for i in range(10):
    num = float(input(f"Digite o número {i+1}: "))
    numeros.append(num) 
print("\nOs números digitados na ordem inversa são:")
for num in reversed(numeros):
    print(num)


    