"""
3) Uso de AND

Crie um programa que peça o nome de usuário e a senha.
 O sistema deve permitir o acesso apenas se o usuário for "admin" 
 e a senha for "1234". Caso contrário, 
deve exibir uma mensagem de acesso negado."""

usuario = "admin"
senha = "1234"
entrada_usuario = input("Digite seu usuario")
entrada_senha = input("Digite sua senha:")

if (entrada_usuario == usuario and entrada_senha == senha):
    print ("Digite seu Usuário : ")
else:
    print ("Tente Novamente")
    