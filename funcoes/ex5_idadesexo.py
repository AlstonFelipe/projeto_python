"""
5.Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima: 

idade média das mulheres 
idade média dos homens
idade média do grupo""" 


total_idade_masc = 0
total_idade_fem = 0
masc = 0
fem = 0
for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} (m/f): ")
    
    if sexo == 'm' or sexo == 'M':
        total_idade_masc += idade
        masc += 1
    elif sexo == 'f' or sexo == 'F':
        total_idade_fem += idade
        fem += 1

if masc > 0:
    media_masc = total_idade_masc / masc
else:
    media_masc = 0

if fem > 0:
    media_fem = total_idade_fem / fem
else:
    media_fem = 0

media_grupo = (total_idade_masc + total_idade_fem) / (masc + fem)

print(f"\n Idade média das mulheres: {media_fem:.2f}")
print(f" Idade média dos homens: {media_masc:.2f}")
print(f" Idade média do grupo: {media_grupo:.2f}")

