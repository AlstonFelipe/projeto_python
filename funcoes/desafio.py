"""
Desafio - Desconto no posto de gasolina

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% no preço total;
acima de 20 litros, desconto de 5% no preço total.

Gasolina:
até 20 litros, desconto de 4% no preço total;
acima de 20 litros, desconto de 6% no preço total.

Escreva um algoritmo que leia o número de litros vendidos e o 
tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e 
imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 5,50 e 
o preço do litro do álcool é R$ 3,89
utilizando if, e o else são obrigatórios.
"""
preco_gasolina = 5.50
preco_alcool = 3.89

print(f"o valor do alcool é: {preco_alcool} e o valor da gasolina é: {preco_gasolina}")
litros = float(input("Digite a quantidade de litros vendidos: "))

tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

if tipo_combustivel == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

    valor_total = litros * preco_alcool * (1 - desconto)
    print(f"O valor a ser pago pelo cliente é: R$ {valor_total:.2f}")

elif tipo_combustivel == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

    valor_total = litros * preco_gasolina * (1 - desconto)
    print(f"O valor a ser pago pelo cliente é: R$ {valor_total:.2f}")

else:
    print("Tipo de combustível inválido.")

