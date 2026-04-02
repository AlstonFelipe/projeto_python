"""1.Desenvolva
um programa em Python que utilize os comandos aprendidos para identificar e
exibir todos os números pares entre 1 e 100. utulizando, while, for, if e else."""

print("Números pares entre 1 e 100 utilizando for:")    
for num in range(1, 101):
    if num % 2 == 0:
        print(num)


        
print("\nNúmeros pares entre 1 e 100 utilizando while:")    
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1


