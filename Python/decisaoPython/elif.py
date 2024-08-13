a = 10
b = 5
res = 0
op = "-" 

if op=="+":
    res=a+b
    
elif op=="-": #ELIF = verifica se é falso ou verdadeiro e pula pro final da operação, 
                #ignorando as ourtas decisões
    res=a-b
    
elif op=="*":
    res=a*b
    
elif op=="/":
    res=a/b
    
print(str(a) + op + str(b) + "=" + str(res));