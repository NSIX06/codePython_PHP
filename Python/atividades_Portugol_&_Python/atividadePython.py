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