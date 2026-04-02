"""
3- Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

"""
notas = []
soma = 0
contador = 0

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
    soma += nota
    contador += 1

media = soma / contador

print("\nAs notas digitadas foram:")
for nota in notas:
    print(nota)

print(f"\nA média das notas é: {media:.2f}")



