import random

def play():
    user = input("'r' para pedra, 'p' para papel, 't' para tesoura" )
    computador = random.choice(['r', 'p', 't'])
    
    if user == computador:
        return 'Empate'
    

