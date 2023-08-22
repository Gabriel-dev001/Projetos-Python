continuar = True

def Erro():
     print("Essa data não existe")


while continuar:
    print("Escreva uma data nesse formato [dia-mes-ano]")
    data_string = str(input())
    data_separada = data_string.split("-")
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])

    if mes>12 or mes<1:
        continuar = False
        Erro()
    
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia>30 or dia<1:
            continuar = False
            Erro()

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia>31 or dia<1:
            continuar = False
            Erro()

    if mes == 2 :
        if ano%4 == 0 and dia>29:
            continuar = False
            Erro()
            
    if mes == 2:
        if ano%4 != 0 and dia>28:
            continuar = False
            Erro()