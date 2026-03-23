"""

Crie um programa em Python que peça ao usuário três notas, 
calcule a média dessas notas e mostre o resultado na tela. 
Em seguida, o programa deve informar a situação do aluno com base na média: 
se for maior ou igual a 7, o aluno está aprovado; se for maior ou igual a 5 e menor que 7,
 está em recuperação; e se for menor que 5, está reprovado. Para resolver o exercício, 
 utilize as estruturas condicionais if, elif e else."""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

#coloqueio o .2f porque quero apenas duas casas decimais se a média for acima de duas casas decimais.

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")