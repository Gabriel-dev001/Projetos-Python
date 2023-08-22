import os

ARMAZENAMENTO_CONTA = []

def Limpa(): #DEF PARA LIMPAR O CONSOLE NA P/ ESCONDER A VARIAVEL{BIBLIOTECA OS}
     if os.name == 'nt': 
        _ = os.system('cls')

def Erro(opcao_erro):

    match(opcao_erro):
        case 1:
            print("Saque indisponivel|Saldo insuficiente ...\n\n")

        case 2:
            print("Seu saldo nao pode ser negativo ...\n\n")

        case 3:
            print("Deposito indisponivel ...\n\n")

        case 4:
            print("Emprestimo negado|Valor solicitado maior que 30% do seu saldo ...")

    Volar_menu()

def Volar_menu():
    input("Aperte Entar para voltar para o menu: ")
    Limpa()

class Conta_bancaria():
    def __init__(self, nome_titular, dinheiro_conta):
        self.nome_titular = nome_titular
        self.dinheiro_conta = dinheiro_conta

    def Depositar(self):
        deposito = float(input("Deposito: "))
        
        if deposito<0:
            Erro(3)
        else:
            self.dinheiro_conta+=deposito

    def Sacar(self):
        saque = float(input("Saque: "))

        if saque>self.dinheiro_conta:
            Erro(1)
        else:
            self.dinheiro_conta-=saque

    def Emprestimo(self):
        PORCENTAGEM_DO_EMPRESTIMO = 0.30

        porcentagem_disponivel = self.dinheiro_conta*PORCENTAGEM_DO_EMPRESTIMO
        emprestimo = float(input("Emprestimo: "))

        if emprestimo>porcentagem_disponivel:
            Erro(4)
        else:
            self.dinheiro_conta+=emprestimo

    def Extrato(self):
        print(f"Esse é seu saldo da conta do {self.nome_titular}:\n\t{self.dinheiro_conta}")

    def Mostrar_nome_titular(self):
        print(self.nome_titular)

conta1 = Conta_bancaria("Rosa", 1000)
conta2 = Conta_bancaria("Isabella ♥", 2000)

def Escolha_conta():
    print("QUAL CONTA DESEJA OPERAR:")
    conta1.Mostrar_nome_titular() 
    conta2.Mostrar_nome_titular()
    escolha = int(input())

    match(escolha):
        case 1:
            conta_operavel = conta1

        case 2:
            conta_operavel = conta2

        case __:
            Escolha_conta()

    Limpa()
    return conta_operavel

def Operar_conta():
    conta_operavel.Mostrar_nome_titular()
    # print(f"Ola, {conta_operavel.Mostrar_nome_titular()}:")
    escolha = int(input("1-Depositar\n2-Sacar\n3-emprestimo\n4-Extrato\n"))

    match(escolha):
        case 1:
            conta_operavel.Depositar()

        case 2:
            conta_operavel.Sacar()

        case 3:
            conta_operavel.Emprestimo()

        case 4:
            conta_operavel.Extrato()
            Volar_menu()
            print("\n")

        case __:
            Operar_conta()

    Limpa()

continuar = True

while continuar:
    conta_operavel = Escolha_conta()
    Operar_conta()