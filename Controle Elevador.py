#PRIMEIRO EXERCICIO EM CLASSES
import os

def Limpa(): # DEF PARA LIMPAR O CONSOLE NA P/ ESCONDER A VARIAVEL{BIBLIOTECA OS}
     if os.name == 'nt': 
        _ = os.system('cls')

def Print_ERRO():
    print("Erro inesperado !!!")
    voltar = input("Aperte Enter para voltar: ")

class Elevador():
    def __init__(self, andar_atual, total_andares, quantidade_pessoa, capacidade_elevador):
        self.andar_atual = andar_atual
        self.total_andares = total_andares+1
        self.quantidade_pessoa = quantidade_pessoa
        self.capacidade_elevador = capacidade_elevador

    def Adicionar_pessoa(self, pessoa_entrando):
        if pessoa_entrando<0 or pessoa_entrando>self.capacidade_elevador or pessoa_entrando+self.quantidade_pessoa>self.capacidade_elevador:
                Print_ERRO()
        else: 
                self.quantidade_pessoa += pessoa_entrando
        
    def Retirar_pessoa(self, pessoa_saindo):
        if pessoa_saindo>self.quantidade_pessoa or pessoa_saindo<0 or pessoa_saindo>self.capacidade_elevador:
            Print_ERRO()
        else:
            self.quantidade_pessoa -= pessoa_saindo
        
    def Subir(self, andar_acima):
        if andar_acima<=self.andar_atual or andar_acima>self.total_andares:
            Print_ERRO()
        else:
            self.andar_atual = andar_acima

    def Descer(self, andar_abaixo):
        if andar_abaixo>=self.andar_atual or andar_abaixo>self.total_andares:
            Print_ERRO()
        else:
            self.andar_atual = andar_abaixo

    def Inspecionar(self):
        if self.andar_atual == 0:
            print(f"Existem {self.quantidade_pessoa} pessoas no elevador")
            print(f"O elevador esta no Terreo")
        else:    
            print(f"Existem {self.quantidade_pessoa} pessoas no elevador")
            print(f"O elevador esta no {self.andar_atual} andar")


elevador_principal = Elevador(0, 10, 0, 5)
elevador_segundario = Elevador(0, 10, 0, 5)     #Elevadores para ser operaveis
elevador_servico = Elevador(0, 10, 0, 10)

def Escolha_elevador():
    print("Escolha qual elevador voce quer operar:\n")
    escolha = int(input("1-Elevador Principal\n2-Elevador Segundario\n3-Elevador de Servico\n"))
    Limpa()

    match(escolha):
        case 1:
            elevador_operavel = elevador_principal

        case 2:
            elevador_operavel = elevador_segundario
        
        case 3:
            elevador_operavel = elevador_servico

        case _:
            Escolha_elevador()

    return elevador_operavel
    


def Rodar_elevador():
    Limpa()
    
    print(f"\tVoce esta operando o elevador {elevador_operavel}")
    escolha = int(input("1-Trocar de Elevador\n2-Mexer no fluxo de pessoas\n3-Mexer no fluxo do elevador\n4-Status Elevador\n"))
       
    match(escolha):
        case 1:
            print("")
        case 2:
            Fluxo_pessoa()

        case 3:
            Fluxo_elevador()

        case 4:
            Status_elevador()

        case _:
            Rodar_elevador()

    Limpa()

def Fluxo_pessoa():
    escolha = int(input("1-Adicionar pessoas\n2-Remover pessoas\n"))
    Limpa()

    match(escolha):
        case 1:
            entrada = int(input("Quantas pessoas dejesa adcionar: "))
            elevador_operavel.Adicionar_pessoa(entrada) 

        case 2:
            entrada = int(input("Quantas pessoas retirar adcionar: "))
            elevador_operavel.Retirar_pessoa(entrada)

        case _:
            Limpa()
            Fluxo_pessoa()

    Rodar_elevador()


def Fluxo_elevador():
    escolha = int(input("1-Subir\n2-Descer\n"))
    Limpa()

    match(escolha):
        case 1:
            entrada = int(input("Escreva o andar desejado: "))
            elevador_operavel.Subir(entrada)

        case 2:
            entrada = int(input("Escreva o andar desejado: "))
            elevador_operavel.Descer(entrada)

        case _:
            Limpa()
            Fluxo_elevador()
 
    Rodar_elevador()


def Status_elevador():
    elevador_operavel.Inspecionar()
    voltar = input("\nAperte Enter para voltar: ")
    Limpa()
    Rodar_elevador()


continuar = True

while continuar:
    elevador_operavel = Escolha_elevador()
    Rodar_elevador()