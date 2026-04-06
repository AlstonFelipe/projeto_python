produtos = { "mouse": 98.75,
            "teclado": 125.65,
            "monitor": 134.78,
            "gabinete": 170.00,
            "hd externo": 510.50,
            "headset": 125.45 }

while True:
    produto = input("informe o produto a pesquisar o preço ou fim para sair: ")
    if produto == "fim":
        break
    if produto in produtos:
        print(f"produto {produto} custa {produtos [produto]}.")
    else:
        print (f"produto {produto} não encontrado. ")
print("ACABOU!!!")
