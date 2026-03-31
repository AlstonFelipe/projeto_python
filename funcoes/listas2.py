letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
var = input("Digite uma letra: ")
if var.lower () in letras:
    print(f"A letra '{var.lower()}' digitada está na lista")
else:
    print(f"A letra '{var.lower()}' digitada não está na lista")
    