#* 01 - Atividade par ou ímpar:
"""
numero = int(input("Digite um número:")) 
if numero % 2 == 0:
    print("O número", numero, "é par")
else:
    print("O número", numero, "é ímpar")
"""
#* 02 -Atividade idade:
"""
idade = int(input("Digite a sua idade:"))

if idade <= 12:
    print("\nVocê é uma criança!")
elif  idade <=17:
    print("\nVocê é um adolecente!")
else:
    print("\nVocê é um adulto!")
"""

#* 03 - Atividade número

"""
nota1 = float(input("Digite a sua primeira nota:"))

nota2 = float(input("Digite a sua segunda nota:"))

nota3 = float(input("Digite a sua terceira nota:"))


media_final = (nota1 + nota2 + nota3) / 3

if media_final >=6:
    print("Você foi aprovado com a média: ", media_final)
else:
    print("Você foi reprovado com a média: ", media_final)
"""

#* 04 - Atividade maior e menor:

"""
num1 = 0
num2 = 0

num1 = int(input("Digite o primeiro número:"))

num2 = int(input("Digite o segundo número:"))

if num1 > num2:
    print("O número" , num1,  "é maior")
elif num2 > num1:
    print("O número" , num2, "é maior")
else:
    print("Os números são iguais")
"""

#* 05 - Atividade notas:

"""
nota = float(input("Digite a sua nota de 0 à 10: "))

if 9 <= nota <= 10:
    print("Excelente")
elif 7 <= nota < 9:
    print("Bom")
elif 5 <= nota < 7:
    print("Regular")
elif 0 <= nota < 5:
    print("Insuficiente")
else:
    print("Escreva um número válido!")
"""

#* 06 - Atividade multiplos de 3 e 5:

"""
numero = float(input("Digite um número e veja se ele é um múltiplo de 3 ou 5: "))

if numero % 3 == 0:
    print("O número", numero, "é múltiplo de 3")
else:
    print("O número", numero, "é múltiplo de 5")
    
"""

#* 07 - Atividade desconto:
"""
valor = 0
percentual = 0
valor_final = 0

valor = float(input("Digite o valor da compra: "))

valor_final = valor - (0.10 * valor)

if valor > 100:
    print("\nVálido para desconto!")
    print("\nO valor da compra com deconto é: ", valor_final)
elif valor == 100:
    print("\nInválido para desconto!")
else:
    print("\nFim do programa")
"""
#* 08 - Atividade temperatura:
"""
temperatura = int(input("Digite uma temperatura em celcius: "))

if temperatura < 15:
    print("Frio")
elif temperatura >= 15 and temperatura <=25:
    print("Agradável")
else:
    print("Quente")
"""

#* 09 - Atividade ano bissexto:

"""
ano = int(input("Informe o ano (com quatro dígitos): "))

if ((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)):
    print("O ano informado é bissexto.")
else:
    print("O ano informado não é bissexto.")
    
"""

#* 10 - Atividade salário:

"""
salario = 0
percentual = 0.15
salario_final = 0

salario = float(input("Digite o seu salário: "))

salario_final = salario + (1.15 * salario)

if salario < 1500:
    print("\nVálido para aumento!")
    print("\nO salário final é de: ", salario_final)
elif salario >= 1500:
    print("\nInvávildo para aumento!")
else:
    print("\nFim do programa")
"""

#* 11 - Atividade voto:

"""
idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você está hapto para votar!")
else:
    print("Você não está hapto para votar!")
"""

#* 12 - Atividade IMC:
"""

peso = 0
altura = 0
imc = 0

peso = float(input("Informe o seu peso(em kg): "))

altura = float(input("Informe a sua altura: "))

imc = peso / (altura* altura)

print("Seu IMC é:", imc)

if imc < 16:
    print("\nSua classificação é Magreza grave")
elif imc < 17:
    print("\nSua classificação é Magreza moderada")
elif imc < 18.5:
    print("\nSua classificação é Magreza leve")
elif imc < 25:
    print("\nSua classificação é Saúdavel")
elif imc < 30:
    print("\nSua classificação é Sobrepeso")
elif imc < 35:
    print("\nObesidade Grau I")
elif imc < 40:
    print("\nObesidade Grau II")
else:
    print("\nObesidade Grau III (mórbida)")
"""


#* 13 - Atividade dias da semana:
"""
dia = int(input("Digite um número de 1 à 7: "))

dias_da_semana = {
    1: "Domingo",
    2: "Segunda-Feira",
    3: "Terça-Feira",
    4: "Quarta-Feira",
    5: "Quinta-Feira",
    6: "Sexta-Feira",
    7: "Sábado"
}

print(dias_da_semana.get(dia, "Número inválido! Digite um número de 1 à 7."))
"""

#* 14 - Atividade de notas:
"""
nota = int(input("Digite uma nota de 0 à 10: "))

notas = {
    "Excelente" :(9,10),
    "Bom":(7,8),
    "Regular":(5,6),
    "Insufiente": (0,4)

}

if nota == 10:
    notas = "Excelente"
elif nota >= 7:
    notas = "Bom"
elif nota >= 5:
    notas = "Regular"
else:
    notas = "Insufuciente"

print(f"Nota: {notas}")
"""

#* 15 - Atividade planetas:
"""

planeta = int(input("Digite um número de 1 à 8: "))

planetas = {
    1: "Mercúrio",
    2: "Vênus",
    3: "Terra",
    4: "Marte",
    5: "Júpiter",
    6: "Saturno",
    7: "Urano",
    8: "Netuno"
}

print(planetas.get(planeta, "Número inválido! Digite um número de 1 à 7."))
"""

#* 16 - Atividade meses:

"""
mes = int(input("Digite um número de 1 à 12: "))

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

print(meses.get(mes, "Número inválido! Digite um número de 1 à 12."))
"""