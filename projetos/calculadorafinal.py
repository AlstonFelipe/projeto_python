# Calculadora que recebe dois numeros e me entrega os resultados de
# soma, subtração, divisão, multiplicação, expoente e resto
nota1 = 0
nota2 = 0
opcao = int(input("Digite o numero da opção desejada\n 1. Adição\n" \
"2. Subtração\n" \
"3. Divisão\n" \
"4. Multiplicação\n" \
"5. Restante da divisão\n" \
"6. Expoente\n"
"------>"))

if (opcao == 1):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}+{nota2}={(nota1+nota2)}")
elif (opcao == 2):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}-{nota2}={(nota1-nota2)}")
elif (opcao == 3):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}/{nota2}={(nota1/nota2)}")
elif (opcao == 4):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}x{nota2}={(nota1*nota2)}")
elif (opcao == 5):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}%{nota2}={(nota1%nota2)}")
elif (opcao == 6):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}**{nota2}={(nota1**nota2)}")
else:
    print("Voce Digitou uma opção invalida")


# esta dando erro ao compilar


