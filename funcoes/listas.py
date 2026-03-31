bancos = ["Banco do Brasil", "caixa", "santander"]
print(bancos)
# resultado: ['Banco do Brasil', 'caixa', 'santander']
bancos[1] = "itau"
print(bancos)
# resultado: "banco do brasil", "itau", "santander"
bancos[-1] = "c6"
print(bancos)
# resultado: "banco do brasil", "itau', "c6"

#incrementar o valor de uma lista

print(bancos)
# resultado: "banco do brasil", "itau', "c6")
bancos = bancos + ["bradesco","nubank"]
print(bancos)
# resultado: "banco do brasil", "itau', "c6", "bradesco", "nubank"
bancos += ["Safra"]
print(bancos)
# resultado: "banco do brasil", "itau', "c6", "bradesco", "nubank", "Safra"

