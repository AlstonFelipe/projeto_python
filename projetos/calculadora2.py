# Entrada de dados
nota1 = float(input("Digite o primeiro número: "))
nota2 = float(input("Digite o segundo número: "))

# Operações
soma = nota1 + nota2
subtracao = nota1 - nota2
divisao = nota1 / nota2
multiplicacao = nota1 * nota2
expoente = nota1 ** nota2
resto = nota1 % nota2

opcao = int(input("===Digite o numero da opção desejada===\n" \
"1. Adicao\n" \
"2. Subtracao\n" \
"3. Divisao\n" \
"4. Multiplicacao\n" \
"5. Restante da divisão\n" \
"6. Expoente\n"
"------>"))

if (opcao == 1):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}+{nota2}={(nota1+nota2)}")
elif(opcao == 2):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}-{nota2}={(nota1-nota2)}")
elif(opcao == 3):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}/{nota2}={(nota1/nota2)}")
elif(opcao == 4):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}*{nota2}={(nota1*nota2)}")
elif(opcao == 5):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}%{nota2}={(nota1%nota2)}")
elif(opcao == 6):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}**{nota2}={(nota1**nota2)}")
else:
    print("Voce digitou um valor inválido !!!")

    

# Saída de dados
"""print(f"\nResultados:")
print(f"Soma: {nota1} + {nota2} = {soma}")
print(f"Subtração: {nota1} - {nota2} = {subtracao}")
print(f"Divisão: {nota1} / {nota2} = {divisao}")
print(f"Multiplicação: {nota1} * {nota2} = {multiplicacao}")
print(f"Expoente: {nota1} ** {nota2} = {expoente}")
print(f"Resto da divisão: {nota1} % {nota2} = {resto}")

"""
