# calculadora que recebe dois numeros e me entrega os resultados de:
# soma, subtracao, divisão, multiplicação, expoente e resto.
# existe duas maneiras de printar o resultado na tela o primeiro é: print (f"{nota1}+{nota2}={soma}")
# a segunda maneira é: print(nota1,"+",nota2,"=",soma)
#

nota1 = float(input("digite o primeiro numero:"))
nota2 = float(input("digite o segundo numero:"))

print(f"{nota1}+{nota2}+{(nota1+nota2)}")

# esse exemplo abaixo, se cria a função soma com as variaveis.
soma = nota1+nota2
print (f"{nota1}+{nota2}={soma}")
print(nota1,"+",nota2,"=",soma)

#as variaveis sempre são criadas no inicio do código e nunca no meio.

subtracao = nota1-nota2
print (f"{nota1}-{nota2}={subtracao}")




divisao = nota1/nota2
print (f"{nota1}/{nota2}={divisao}")




multiplicacao = nota1*nota2
print (f"{nota1}*{nota2}={multiplicacao}")

