linha_1 = [" "]*3
linha_2 = [" "]*3
linha_3 = [" "]*3

class Jogo_velha():
    def __init__(self, sinal, expre):
        self.sinal = sinal

    def Incrementar(self, cordenada):
        lista = cordenada.split(",")
        cord_l = lista[0]
        cord_c = lista[1]