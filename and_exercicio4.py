"""4) Uso de AND

Crie um programa que receba o salário de um funcionário e seu 
tempo de empresa (em anos). O funcionário receberá um bônus 
apenas se tiver salário menor que 3000 e tempo de empresa maior 
ou igual a 2 anos. Caso contrário, não receberá bônus. 
O programa deve exibir uma mensagem informando se o bônus foi concedido ou não.

"""

salario = float(input("Digite o seu salário: "))
tempo_empresa = int(input("Digite o tempo de empresa no formato (anos): "))

if salario < 3000 and tempo_empresa >= 2:
    print("Você tem direito ao bônus salarial!")
else:
    print("Você não tem direito ao bônus.")