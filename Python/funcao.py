 #*Média 
'''
def calculo_3(a, b, c):
    return ((a + b + c) / 3)

resultado = calculo_3(10, 16, 8)

print(resultado)
'''
#* Idade
"""
def idade_filtro(idade):
    if idade >= 18:
        resultado = (f"A idade {idade} é maior que 18!")
    else:
        resultado = (f"A idade {idade} é menor que 18!")

    return resultado

print(idade_filtro(25))
"""

#todo - Módulos : organizador de códigos usando módulos e pacotes

#?Exemplo - raiz quadrada de 25:

import math 
print(math.sqrt(25))