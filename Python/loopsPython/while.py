
import os

carros=[]
carro=input("Insira um nome de uma carro!: ")
while carro != "-1": #While = é usado para controle de variáveis, sendo elas verdadeiras continua a execução e sendo falsa  
                        #ele para o loop.
    carros.append(carro)
    carro=input("Insira um nome de um carro!: ")
    
    os.system('cls')
    for x in carros:
        print(x)
        
print("Fim do loop")