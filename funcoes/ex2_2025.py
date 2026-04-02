"""
2.Faça um programa que peça para n
pessoas a sua idade, ao final o programa deverá mostrar a quantidade de pessoas
por geração (Em 2025): 
Geração Beta (a partir de 2025): 0 a 1 ano.
Geração Alfa (2011-2024): 2 a 14 anos.
Geração Z (1997-2010): 15 a 29 anos.
Millennials ou Geração Y (1981-1996): 30 a 45 anos.
Geração X (1965-1980): 46 a 61 anos.
Baby Boomers (1946-1964): 62 a 80 anos.
Silent Generation (1925-1945): 81 a 101 anos.

"""
n = int(input("Digite o número de pessoas: "))
geracao_beta = 0
geracao_alfa = 0    
geracao_z = 0
geracao_y = 0
geracao_x = 0
baby_boomers = 0
silent_generation = 0
for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    
    if 0 <= idade <= 1:
        geracao_beta += 1
    elif 2 <= idade <= 14:
        geracao_alfa += 1
    elif 15 <= idade <= 29:
        geracao_z += 1
    elif 30 <= idade <= 45:
        geracao_y += 1
    elif 46 <= idade <= 61:
        geracao_x += 1
    elif 62 <= idade <= 80:
        baby_boomers += 1
    elif 81 <= idade <= 101:
        silent_generation += 1
print("\nQuantidade de pessoas por geração:")
print(f"Geração Beta (0 a 1 ano): {geracao_beta}")
print(f"Geração Alfa (2 a 14 anos): {geracao_alfa}")
print(f"Geração Z (15 a 29 anos): {geracao_z}")
print(f"Millennials ou Geração Y (30 a 45 anos): {geracao_y}")
print(f"Geração X (46 a 61 anos): {geracao_x}")
print(f"Baby Boomers (62 a 80 anos): {baby_boomers}")
print(f"Silent Generation (81 a 101 anos): {silent_generation}")

