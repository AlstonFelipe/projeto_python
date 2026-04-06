"""
copiando um dicionario para outro
adicionando conteudo de um dicionario em outro dicionario
para retornar quantos conjuntos chave/valor existem no dicionario usamos a função len()"""

dic = {"nome":"fulano", "sobrenome": "de tal"}
local = {"UF": "SP", "cidade": "São Carlos"}
dic2 = dic.copy()
dic.update(local)
print(len(dic))
print(f"dic: {dic}")
print(f"dic2: {dic2}")

