carros = [
    ["Modelo", "STR Challenger Hellcat"], #linha 0 e coluna 1
    ["Fabricante","Dodge"], #linha 1 e coluna 1
    ["Ano","2023"] #linha 2 e coluna 1
    ]

carros [2][1] = 2024

for l, c in carros:
        print("Linha: " + l + "| Coluna: " + str(c))