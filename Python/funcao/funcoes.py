#*Criação de Funções - 01
'''
def mostrar_mensagens():
    print("Aula de ADS")
    
mostrar_mensagens() 
'''

#*Função Somar - 02
'''
def soma_dois(numero1, numero2):
    print(numero1 + numero2)
    
    
soma_dois(8,9)
'''
#?outro meio usando o return
'''
def soma_dois(numero1, numero2):
    return numero1 + numero2 #? retorna uma função e encerra a mesma, o que está abaixo dele não roda
    
    
print(soma_dois(8,9))
'''
#*Função - 03
'''
def exibir_dados(nome, sobrenome, cpf, idade):
    print(f"O {nome} {sobrenome} tem {idade} anos e seu cpf é {cpf}")
    
exibir_dados("José", "Santana", "123456789", 25)#! tem que ter todos os parametros para o código para rodar 
'''

#*Função Somar sem parametros - 04
'''
def somar_sequencia():
    soma = 0
    for i in range(1, 11):
        soma += i
    print(soma)
    
somar_sequencia()
'''

#*Função conversão clima - 05
'''
Uso - 01

def celsius_p/_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin
'''
'''
Uso - 02

def celsius_para_kelvin(celsius):
    return  celsius + 273.15

temperaturas = [15, 29, 31, 27, 23, 15, 15]

temperaturas_kelvin = list(map(celsius_para_kelvin, temperaturas))
print(temperaturas_kelvin)
'''
'''
temperaturas = [15, 29, 31, 27, 23, 15, 15]

temperaturas_kelvin = []
    for temperatura in temperaturas:
        temperaturas_kelvin.append(celsius_para_kelvin(temperatura))
        
print(temperaturas_kelvin)
'''

#*Função - 06
'''
numeros = [1, 2, 3, 4, 5, 6]

numeros_ao_quadrado = [1 ** 2, 2 ** 2, 3 ** 2, 4 ** 5, 6 ** 2,]

print(numeros_ao_quadrados)
'''
'''
numeros_ao_quadrado = []

for i in numeros:
    numeros_ao_quadrado.append(i**2)
    
print(numeros_ao_quadrados)
'''
'''
numeros = [1, 2, 3, 4, 5, 6]

numeros_ao_quadrado = [x**2 for i in numeros]

print(numeros_ao_quadrado)
'''

#*Função - 07
'''
def juntar_nomes(nome, sobrenome):
    return nome + " " + sobrenome

print(juntar_nomes("Luiz", "Felipe"))
'''

def juntar_nomes(nome, sobrenome):
     return nome + " " + sobrenome

nomes = []
sobrenomes = []
nomes_completos = []

for x in range(5):
    nome = input("Digite o seu nome:")
    sobrenome = input("Digite o seu sobrenome:")
    nomes_completos.append(juntar_nomes(nome, sobrenome))

print(nomes_completos)