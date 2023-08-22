QUANTIDA_CARACTERS = 5
palavra_nova = ""
palavra = str(input("Escreva sua palavra: "))
quantidade_palavra = 1

def Inverter_palavra(texto):
    return texto[::-1]

for i in range(len(palavra)):   #For para descobrir quantas palavras existem na frase
    if palavra[i] == " ":
        quantidade_palavra+=1

if quantidade_palavra == 1:
    if len(palavra) >= QUANTIDA_CARACTERS:
        print(Inverter_palavra(palavra))

    else:
        print(palavra)

else:
    palavra_separas = palavra.split (" ")

    for i in range(len(palavra_separas)):
        if len(palavra_separas[i]) >= QUANTIDA_CARACTERS:
            palavra_invertida = Inverter_palavra(palavra_separas[i])
            palavra_nova = palavra_nova + " " +  palavra_invertida

        else:
            palavra_nova = palavra_nova + " " + palavra_separas[i]
    
    print(palavra_nova)
