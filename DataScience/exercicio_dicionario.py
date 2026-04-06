"""crie uma estrutura contendo uma lista com tres dicionarios, onde cada dicionario
representa um livro com titulo, autor e ano. em seguida, imprima as informações
dos livros utilizando loop (for)"""

livros = [
    {"titulo": "Como irritar uma pessoa em dois minutos", "autor": "Alston Felipe", "ano": 1999},
    {"titulo": "12026", "autor": "Felipe. Alston", "ano": 2026},
    {"titulo": "Ansioso pra viajar", "autor": "Alston F. Nonato", "ano": 2026}
]
for livro in livros:
    print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

