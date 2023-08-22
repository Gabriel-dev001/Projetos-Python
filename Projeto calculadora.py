result = 0

expre = str(input())

while expre != "fim": 

    for i in range(len(expre)):
        if expre[i] == "+":
            sinal = "+"
            
        if expre[i] == "-":
            sinal = "-"
            
        if expre[i] == "*":
            sinal = "*"
            
        if expre[i] == "/":
            sinal = "/"

    lista = expre.split(sinal)

    if result == 0:
        num1 = float(lista[0])
    else:
        num1 = result

    num2 = float(lista[1])

    if sinal == "+":
        result = num1+num2
        
    if sinal == "-":
        result = num1-num2
        
    if sinal == "*":
        result = num1*num2
        
    if sinal == "/":
        result = num1/num2
        
    expre = str(input(result))

    if expre == "":
        result = 0
        expre = str(input())