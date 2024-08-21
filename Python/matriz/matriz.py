"""
carros = [
    ["Modelo", "STR Challenger Hellcat"], #?linha 0 e coluna 1
    ["Fabricante","Dodge"], #?linha 1 e coluna 1
    ["Ano","2023"] #?linha 2 e coluna 1
    ]

carros [2][1] = 2024

for l, c in carros:
        print("Linha: " + l + "| Coluna: " + str(c))
"""       

#*Matriz múltiplo de 3
matriz = [
    [10, 27, 30],
    [45, 58, 16],
    [78, 83, 99]
]

for linha in matriz:
    for elemento in linha:
        if elemento % 3 == 0:
            print(f"{elemento} (que é múltiplo de 3)", end=' ')
        else:
            print(elemento, end=' ')
    print()

#*Matriz idade
idades = [25, 30, 18, 42, 21, 35, 28]

for i in range(len(idades)):
    print(idades[i])

idades = [25, 30, 18, 42, 21, 35, 28]

for idade in idades:
    print(idade)

#*Matriz cinema cadeira enumerada
acentos = [[76, 99, 90],[65, 88, 50],[80, 71, 96]]

for fila in acentos:
	for cadeira in fila:
		print(cadeira, end=" ")
	print()

#*Matriz cinema acentos e filas enumerados

assentos = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,0), (2,2)]
]

assentos = [
    [15, 12, 35],
    [94, 88, 66],
    [27, 38, 89]
]

for i, fila in enumerate(acentos):
    for j, cadeira in enumerate(fila):
        print(f"Cadeira na posição ({i}, {j}): {cadeira}")

#*Dada a matriz de tamanho 3x3 abaixo, faça um algoritmo em python que ache o valor 85; Se não encontrar, apresente uma mensagem com essa informação

matriz = [
    [15, 12, 35],
    [94, 88, 66],
    [27, 38, 89]
]

matriz = [
    [15, 12, 35],
    [94, 85, 66],
    [27, 38, 89]
]

encontrado = False

for i in range(len(matriz)): 
    for j in range(len(matriz[i])):
        if matriz[i][j] == 85:
            encontrado = True
            print(f"O valor 85 foi encontrado na posição ({i}, {j})")
            break

if not encontrado:
    print("O valor 85 não foi encontrado na matriz.") 



#*Dada a matriz vazia abaixo, solicite ao usuário nomes de pessoas para cada posição, e as preencha com tais nomes, como se fossem assentos de um cinema.
assentos = [[], [], []]
for i in range(3):
    for j in range(3):
        #?nome = input(f"Digite o nome para o assento ({i+1}, {j+1}): ")
        #?assentos[i].append(nome)
        assentos[i].append(input(f"Digite o nome para o assento ({i}, {j}): "))

for fila in assentos:
    print(fila)