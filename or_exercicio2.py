"""
2) Uso de OR

Crie um programa que receba a nota final de um aluno e sua frequência 
(em porcentagem). O aluno será considerado aprovado se tiver 
nota maior ou igual a 7 ou frequência maior ou igual a 75%. Caso contrário, 
deverá ser reprovado. O programa deve exibir uma mensagem informando a 
situação do aluno.
"""

nota = float(input("Digite a nota final: "))
frequencia = float(input("Digite a frequência em (%): "))

if nota >= 7 or frequencia >= 75:
    print("Esse aluno foi aprovado!")
else:
    print("Esse Aluno reprovado.")