 ##*Lista frutas---------------------------------------

"""
lista = []
for i in range(10):
    lista.append(input("Insira frutas doo seu gosto:"))
    print(lista)
"""
##*-------------------------------------------------

##*Lista de idade-----------------------------------
"""    
listAge = [76, 99, 65, 50, 71, 33] 

for i in listAge:
    print(i*2)
    
    
listAge = [76, 99, 65, 50, 71, 33]
dobro = []

for listAge in listAge:##????????????????????????
    dobro.append(listAge*2)
    print(dobro)  
 
    
listAge = [76, 99, 65, 50, 71, 33]
dobro =   [x*2 for x in listAge]
print(dobro)
"""
##*----------------------------------------------

##*Lista de frutas-------------------------------

"""
frutas = ["maça", "banana", "uva", "kiwi", "manga"]
novalista = []

for fruta in frutas:
    novalista.append(fruta)
    print(novalista)
"""
##*---------------------------------------------

##*Lista números--------------------------------

"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
quadrado = [x**2 for x in list]
print(quadrado)

"""
##*--------------------------------------------

##*Lista nome

"""
list = ["Fábio", "Jefferson", "Ivy", "Ianka", "John", "Maria", "Ygor", "João"]
newList = [x for x in list if x.startswith("a")]
print(newList)

"""

##*Lista números divisiveis por 3------

"""
listNum = [2, 4, 6, 8, 10, 12, 26, 45, 66, 42, 3, 5, 9, 96]
newList = [x for x in listNum  if x%3==0]
print(newList)
"""

##*-----------------------------------

##*Lista alfabeto
import string

"""

def listAlphabet():
    return list(map(chr, range(97, 107)))


print(listAlphabet())

"""
##? map e filter = usados para aplicar função
##todo : interação com map -----> list(map(função, lista de informações))
##!def ------> criar uma função (definir)
##* lambda ---------> parâmetro / calculo direto
"""
precos = [1000, 5500, 5250, 625, 998, 653, 745, 200,]
impostos = list(map(lambda x: x*0.3, precos))

print(impostos)
"""

##*newList = [x for x in list if x.startswith("a")
"""
lista = ["Fábio", "Jefferson", "Ivy", "Ianka", "John", "Maria", "Ygor", "João"]
nomes = list(map(lambda x: x*0.3, lista))

print(nomes)

"""
##*Lista de conversão de F para C

"""
lista = [50, 25, 35, 45, 66, 42, 3, 5, 9, 96]
temperatura = list(map(lambda x: (x-32)/1.8, lista))

print(temperatura)

"""

##*Lista números em dobro

""""

listNum = [2, 4, 6, 8, 10, 12, 14, 16, 18]
lista = list(map(lambda x: (x*2), listNum))

print(lista)

"""
##*Lista Preços Produtos (filter, lambda)

"""
precos = [1000, 5500, 5250, 625, 998, 653, 745, 200]

def aplicar_aumento(preco):
    if preco > 700:
        return True
    else:
        return False;
    
precos_produtos=list(filter(aplicar_aumento, precos))

print(precos_produtos)

"""

##*Lista J
"""
listaNomeJ = ["Fábio", "Jefferson", "Ivy", "Ianka", "John", "Maria", "Ygor", "João"]

j= list(map(lambda nome: nome.startswith('j'), listaNomeJ))

print(j)

"""

##*Lista A
"""
listaNomeA = ["Fábio", "Jefferson", "Ivy", "Ianka", "John", "Maria", "Ygor", "João"]

a= list(map(lambda nome: nome.startswith('a'), listaNomeA))

print(a)
"""

##*Lista das palavras com "rr" e "ss" - Exercício 01
"""
listaPalavras = ["massa", "carro", "correr", "sol", "rir", "corrida", "corrida", "ousado" 
                 ,"ressaca", "carroça", "cor", "muscular", "dor", "asa", "sonar", "assessor", 
                 "rua", "massagista", "sentimento", "passaporte", "assessoria", "obstáculos", 
                 "massagem" , "ressaltar", "azul"]

rrSS=[listaPalavras for x in listaPalavras if "rr" in x or "ss" in x ]


print(listaPalavras)
"""

#*Lista AR - Exercício 02
"""
listaAR = ["massa", "carro", "correr", "sol", "rir", "corrida", "corrida", "ousado" 
                 ,"ressaca", "carroça", "cor", "muscular", "dor", "asa", "sonar", "assessor", 
                 "rua", "massagista", "sentimento", "passaporte", "assessoria", "obstáculos", 
                 "massagem" , "ressaltar", "azul"]

#?newlist=[x for x in listaAR if x.endswith("ar")]

AR= list(filter(lambda x: x.endswith("ar"), listaAR))
print(AR)
"""


"""
#*Lista C - Exercício 03
listaC = ["massa", "carro", "correr", "sol", "rir", "corrida", "corrida", "ousado" 
                 ,"ressaca", "carroça", "cor", "muscular", "dor", "asa", "sonar", "assessor", 
                 "rua", "massagista", "sentimento", "passaporte", "assessoria", "obstáculos", 
                 "massagem" , "ressaltar", "azul"]

newlistC=[x for x in listaC if x.startswith("c")]

print(newlistC)
"""
#*Lista de multiplos de 3 e 5 - Exercício 04
"""
numeros = [9, 56, 45, 59, 555, 489, 723, 520, 49, 87, 
           74, 71, 51, 46, 125, 265, 433, 547, 589, 33]

#?newList = [x for x in numeros if x%3 or 5 == 0]

 
filtra = list(filter(lambda x: x == x%3 or x%5 ==0,
numeros))
    
print(filtra)
"""

#*Lista de multiplos de 3 e 5 somados - Exercício 05

"""
numeros = [9, 56, 45, 59, 555, 489, 723, 520, 49, 87, 
           74, 71, 51, 46, 125, 265, 433, 547, 589, 33]

listNum = list(map(lambda x: x + 5, filter(lambda x: x % 3 == 0, numeros)))

resultado = [x for x in numeros if x%3 == 0], [x + 5 for x in numeros if x%3 == 0]

print(resultado)
"""
#* Lista funcionáros com matrizes que deu errado

"""
salarioAntigo = 0
percentual1 = 0.12
percentual2 = 0.8
percentual3 = 0.5
salarioAtual = 0
salario = 0

#?funcionarios = input("Digite o salário: "[[None] * 10 for _ in range(2)])

salarioAntigo = input(float("Digite o seu salário: "))

salarioAtual =[]

for salarioAntigo in salarioAtual:
    salarioAtual.append(input(float("Digite o seu salário: ")))


if salarioAntigo <= 1400:
    
    percentual1 = salario + (0.12 * salario)
    
    print(percentual1)
elif salarioAntigo >= 1401 and salarioAntigo <= 5000:
    print(percentual2)
else:
    print(percentual3)
"""
#* Lista funcionáros com matrizes que deu certo
"""
salarioAntigo = []
salarioAtual = []

for i in range(3):
    salarioAntigo.append(float(input("Digite o seu salário {i+1} : ")))
    
salarioAtual = []

for salario in salarioAntigo:
    if salarioAntigo <= 1400:
        salarioAtual.append(salario*1.12)
    elif salario >= 1401 and salario <= 5000:
        salarioAtual.append(salario*1.08)
    else:
        salarioAtual.append(salario*1.05)
        
print(salarioAntigo, salarioAtual)
"""
"""
funcionarios = [[None] * 3 for _ in range(2)]
    
for i in range(3):
    nome = input(f"Digite o nome do funcionário [{i}]: ")
    salario = float(input(f"Digite o salário do funcionário  [{i}]: "))
    funcionarios [0] [i] = nome
    funcionarios [1] [i] = salario
    
    for i in range(3):
        print(f"{funcionarios[0] [i]} - Salário R$ {funcionarios[1] [i]}")
"""       
#* Lista alunos e provas
"""
alunos = []
notas = []


for i in range(5):
    alunos = input(f"Digite o nome do aluno [{i}]: ")
    notas = float(input(f"Digite a nota do aluno  [{i}]: "))
   
    
    for media in notas:
        if media < 6:
            alunos.append(media = (notas + notas + notas + notas) /4 )
        else:
            print(notas, alunos)
"""            
"""            
nota1 = float(input("Digite a sua primeira nota:"))

nota2 = float(input("Digite a sua segunda nota:"))

nota3 = float(input("Digite a sua terceira nota:"))
"""

#*Funções com o def

"""
#?Sem a função

nomes = []
sobrenomes = []
nomes_completos = []

for x in range(2):
    nome = input("Digite o seu nome:")
    sobrenome = input("Digite o seu sobrenome:")
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    
    for i in range(len(nomes)):
        nome_completo = nomes[i] + " " + sobrenomes[i]
    nomes_completos.append(nome_completo)

print(nomes_completos)
"""
'''
#?Usando a função

def nomes_juntos(nome, sobrenome):
    return f"{nome} {sobrenome}"

nomes = []
sobrenomes = []
nomes_completos = []

for x in range(2):
    nome = input("Digite o seu nome:")
    sobrenome = input("Digite o seu sobrenome:")
    nomes_completos.append(nomes_juntos(nome, sobrenome))

print(nomes_completos)
'''
'''
#?Usando o for 
precos = [1500, 1100, 1000, 3000]

#!aliquota1 = IR = 0.2
#!aliquota2 = ISS = 0.15
#!aliquota3 = CSLL = 0.05

for preco in precos:
    imposto_ir = 0.2 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.5 * preco
    
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    print(imposto_total)
'''
'''
#?Usando o for com if & else
precos = [1500, 1100, 1000, 3000]

#!aliquota1 = IR = 0.2
#!aliquota2 = ISS = 0.15
#!aliquota3 = CSLL = 0.05

for preco in precos:
    if preco > 2000:
        imposto_ir = 0.3 * preco
    else:
        imposto_ir = 0.2 * preco
        imposto_iss = 0.15 * preco
        imposto_csll = 0.5 * preco
    
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    print(imposto_total)
'''
'''
#?Outro meio de se fazer usando o def
precos = [1500, 1100, 1000, 3000]

#!aliquota1 = IR = 0.2
#!aliquota2 = ISS = 0.15
#!aliquota3 = CSLL = 0.05

def calcular_imposto_total(preco):
    if preco > 2000:
        imposto_ir = 0.3 * preco
    else:
        imposto_ir = 0.2 * preco
        imposto_iss = 0.15 * preco
        imposto_csll = 0.5 * preco
        imposto_total = imposto_ir + imposto_iss + imposto_csll
        return imposto_total
    
for preco in precos:
    impostos = calcular_imposto_total(preco)
    print(impostos)
        
mais_precos = [2500, 2100, 1400, 1000]
for preco in mais_precos:
            print(calcular_imposto_total(preco))
'''
'''
#?Segundo meio de se fazer usando o def
def calcular_imposto_total(preco):
    if preco > 2000:
        imposto_ir = 0.3 * preco
        imposto_iss = 0
        imposto_csll = 0
    else:
        imposto_ir = 0.2 * preco
        imposto_iss = 0.15 * preco
        imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

precos = [1500, 1100, 1000, 3000]
for preco in precos:
    impostos = calcular_imposto_total(preco)
    print(f"Preço: R${preco:.2f} - Imposto Total: R${impostos:.2f}")

mais_precos = [2500, 2100, 1400, 1000]
for preco in mais_precos:
    impostos = calcular_imposto_total(preco)
    print(f"Preço: R${preco:.2f} - Imposto Total: R${impostos:.2f}")
'''
'''
def calcular_media(notas):
    soma = sum(notas)
    return soma / len(notas)

notas1 = [7.5, 8.0, 9.0, 6.5]
notas2 = [5.5, 6.0, 8.0, 7.0]

print(calcular_media(notas1))
print(calcular_media(notas2))
'''

#?Lista de números pares

def filtro_numeros(numeros):
    return [numero for numero in numeros if numero % 2 ==0]

numeros1 = [10, 15, 20, 25, 30]
numeros2 = [7, 18, 21, 24, 29]

print(filtro_numeros(numeros1))
print(filtro_numeros(numeros2))