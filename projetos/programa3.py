"""

3. Faça um programa que verifique o estado civil de uma pessoa. Se a letra digitada 
é "C" (casado), "S" (solteiro), "D" (divorciado), "V" (viúvo), ou "O" (outros). 
Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil. Exemplo:
Usuário digita: C
Seu programa deve responder:
C - Casado

"""

# criei uma variavel com o estado civil e suas siglas.

estado = input("Digite seu estado civil (C - Casado, S - Solteiro, D - Divorciado, V - Viuvo, O - OUTROS): Observe que tem que ser com letra maíuscula ")

# coloquei as condições com if o principal, e o elif com as outras condições.
if estado == "C":
    print("C - Casado")

elif estado == "S":
    print("S - Solteiro")

elif estado == "D":
    print("D - Divorciado")

elif estado == "V":
    print("V - Viúvo")

elif estado == "O":
    print("O - Outros")

else:
    print("Para de Palhaçada e digite uma letra que exista nas opçoes desejadas, EM MAIUSCULA")