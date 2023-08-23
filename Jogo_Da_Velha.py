import os


linha_1 = [" "]*3
linha_2 = [" "]*3
linha_3 = [" "]*3

def Limpa(): # def para limpar menu{BIBLIOTECA OS}
     if os.name == 'nt': 
        _ = os.system('cls')

class Jogo_velha():
    def __init__(self, sinal):
        self.sinal = sinal

    def Incrementar(self, cordenada):
        lista = cordenada.split(",")
        cord_l = int(lista[0])
        cord_c = int(lista[1])

        match(cord_l):
            case 1:
                linha_1[cord_c-1] = self.sinal
            
            case 2:
                linha_2[cord_c-1] = self.sinal

            case 3: 
                linha_3[cord_c-1] = self.sinal

             
bolinha = Jogo_velha("O")
xzinho = Jogo_velha("X")
        
            
def Verificar_ganhador():
    if linha_1[0] == " " or linha_1[1] == " " or linha_1[2] == " ":
            return False
        
    if linha_2[0] == " " or linha_2[1] == " " or linha_2[2] == " ":
            return False
        
    if linha_3[0] == " " or linha_3[1] == " " or linha_3[2] == " ":
            return False
        

    if linha_1[0] == " " or linha_2[0] == " " or linha_3[0] == " ":
        return False
    
    if linha_1[1] == " " or linha_2[1] == " " or linha_3[1] == " ":
        return False
    
    if linha_1[2] == " " or linha_2[2] == " " or linha_3[2] == " ":
        return False
    

    if linha_1[0] == " " or linha_2[1] == " " or linha_3[2] == " ":
            return False
    
    if linha_1[2] == " " or linha_2[1] == " " or linha_3[0] == " ":
            return False
    
    
    return True

def Jogo():
    for i in range(9):
        Limpa()
        print("    1    2    3")
        print("1",linha_1)
        print("2",linha_2)
        print("3",linha_3)
        caminho = str(input("Escreva sua cordenada. [l,c]\n"))

        if i%2 == 0:
            xzinho.Incrementar(caminho)
            ganhador = Verificar_ganhador()
        
        else: 
            bolinha.Incrementar(caminho)
            ganhador = Verificar_ganhador()

        if ganhador == True:
            print("O jogo foi ganho!!!")
            break

    print("O jogo deu velha!!!")

Jogo()






        