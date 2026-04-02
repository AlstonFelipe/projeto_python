"""
4.Desenvolva
um programa que funcione da seguinte maneira: 
Solicite ao usuário que informe a quantidade total de pessoas em um
grupo.  Para cada pessoa, peça que o
usuário registre o sexo, utilizando a letra 'm' ou 'M' para masculino e ‘f’ ou
‘F’ para feminino.  O programa deve 
contar e, ao final, exibir o total de pessoas do sexo masculino e feminino.
"""


masc = 0
fem = 0

pessoas = int(input("Digite o número total de pessoas: "))

for i in range(pessoas):
    sexo = input(f"Digite o sexo da pessoa {i+1} (m/f): ")
    if sexo == 'm' or sexo == 'M':
        masc += 1
    elif sexo == 'f' or sexo == 'F':
        fem += 1

print(f"\nTotal de pessoas do sexo masculino: {masc}")
print(f"Total de pessoas do sexo feminino: {fem}")

