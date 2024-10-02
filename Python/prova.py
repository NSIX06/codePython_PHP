'''
numeros = [ 1, 2, 3, 4, 5]

quadrados = [(numero ** 2) for numero in numeros]


print(quadrados)
'''

'''
temperaturas = [25, 30, 28, 32, 29]

temperaturas_fahrenheit = [(temperatura * 9/5) + 32 for temperatura in temperaturas]

print(temperaturas_fahrenheit)
'''

precos = [100, 50, 25, 120, 25, 30, 28, 32, 29]

desconto = [x for x in precos if x * (0.25 - x )]

print(desconto)

'''

salarios = [2000, 2500, 3000, 5500, 11500, 3250, 9275, 6982]

aumento = list(filter(lambda x: x for x in salrios if x * (x + 10/100), salarios))

aumento = [x for x in salarios if x * (x + 10/100)]

print(aumento)
'''
'''
nomes = ["Ana", "Bruno", "Carlos", "Alice", "Emanuel", "Augusto", "Rafel", "Alberto"]

lista_A = list(filter(lambda nome: nome for nome in nomes if x.startswith("A"), nomes))
print(lista_A) 
'''
'''
lista_A = [x for x in nomes if x.startswith("A")]
print(lista_A)

'''
'''
'''
'''
precos = [12, 8, 15, 9, 18, 16, 52, 23, 7, 6]

desconto = [x for in x]

desconto = list(filter(lambda preco: preco for precos in precos if preco <= 10 , precos))
print(desconto)
'''
'''
def conversao_monetarios():
    valor = input(float("Insira um valor para a conversão:"))
    valor * 5.45
    return conversao_monetarios
'''


    
    


