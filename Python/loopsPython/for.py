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

for listAge in listAge:
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
