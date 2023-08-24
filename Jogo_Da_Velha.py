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

    def Tabela(self):
        Limpa()
        print("    1    2    3")
        print("1",linha_1)
        print("2",linha_2)
        print("3",linha_3)
        print(f"|{self.sinal}|Escreva sua cordenada. [l,c]")

    def Incrementar(self, cordenada):
        lista = cordenada.split(",")
        cord_l = int(lista[0])
        cord_c = int(lista[1])

        match(cord_l):
            case 1:
                if linha_1[cord_c-1] == " ":
                    linha_1[cord_c-1] = self.sinal
            
            case 2:
                if linha_2[cord_c-1] == " ":
                    linha_2[cord_c-1] = self.sinal

            case 3:
                if linha_3[cord_c-1] == " ":
                    linha_3[cord_c-1] = self.sinal
        
        return self.sinal

    def Ganhador(self):
         print(f"O jogador |{self.sinal}| Ganhou o jogo!!!")
    
bolinha = Jogo_velha("O")
xzinho = Jogo_velha("X")
        
def Verificar_ganhador(elemento):
    if linha_1[0] == elemento and linha_1[1] == elemento and linha_1[2] == elemento:
            return False
        
    if linha_2[0] == elemento and linha_2[1] == elemento and linha_2[2] == elemento:
            return False
        
    if linha_3[0] == elemento and linha_3[1] == elemento and linha_3[2] == elemento:
            return False
        

    if linha_1[0] == elemento and linha_2[0] == elemento and linha_3[0] == elemento:
        return False
    
    if linha_1[1] == elemento and linha_2[1] == elemento and linha_3[1] == elemento:
        return False
    
    if linha_1[2] == elemento  and linha_2[2] == elemento and linha_3[2] == elemento:
        return False
    

    if linha_1[0] == elemento and linha_2[1] == elemento and linha_3[2] == elemento:
            return False
    
    if linha_1[2] == elemento and linha_2[1] == elemento and linha_3[0] == elemento:
            return False
    

def Jogo():
    continuar = True
    i=0

    while continuar:
        i+=1

        if i == 9:  
            print("O jogo deu velha!!!")
            break

        if i%2 != 0:
            jogador = xzinho     
        else: 
            jogador = bolinha

        jogador.Tabela()        
        caminho = str(input())
           
        sinal = jogador.Incrementar(caminho)
        ganhador = Verificar_ganhador(sinal)

        if ganhador == False:
            print(linha_1)
            print(linha_2)
            print(linha_3)
            jogador.Ganhador()
            break
 
Jogo() 
