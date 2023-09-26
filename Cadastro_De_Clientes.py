#Aqui temos um cadastro simples de Clintes

import os
import datetime as dt

NOME = []
DATA_NASCIMENTO = []
CPF = []
SEXO = []

#Função responsavel por limpar o console
def Limpa():
     if os.name == 'nt': 
        _ = os.system('cls')


#Responsavel por abrir a função Menu
def Voltar_Menu():
    voltar = input("Prescione para volatar pro menu: ")
    Limpa()
    Menu()


#Menu para direcionar para as opções do programa
def Menu():
    print("1 - Cadastrar novo Cliente")
    print("2 - Listas de Clientes")

    escolha = str(input())
    Limpa()
   
    match(escolha):
        case "1":
            Cadastrar_Clientes()

        case "2":
           Lista_Clientes()

        case __:
            Menu()


#1.0 Essa é a função principal do cadastro, nela vamos chamar as complementares
def Cadastrar_Clientes():
    cliente = []

    print("Vamos cadastrar um novo Cliente !!!")

    nome_cliente = Cadastro_nome()
    Limpa()
    print(f"Nome: {nome_cliente}")

    idade_cliente = Cadastro_Idade()
    Limpa()
    print(f"Nome: {nome_cliente}")
    print(f"idade: {idade_cliente} Anos")

    cpf_cliente = Cadastro_Cpf()
    Limpa()
    print(f"Nome: {nome_cliente}")
    print(f"idade: {idade_cliente} Anos")
    print(f"CPf: {cpf_cliente}")

    sexo_cliente = Cadastro_Sexo()
    Limpa()
    print(f"Nome: {nome_cliente}")
    print(f"idade: {idade_cliente} Anos")
    print(f"CPf: {cpf_cliente}")
    print(f"Genero: {sexo_cliente}")

    print("Cliente Adcionado com Sucesso !!!")
    voltar = input()      

    Voltar_Menu()


#1.1 Responsavel por receber o nome e salvar no vetor.
def Cadastro_nome():
    nome = str(input("Nome completo: "))
    NOME.append(nome)

    return nome


#1.2 responsavel por receber a data de nascimento, e calcular a idade.
def Cadastro_Idade():
    data_nascimento = str(input("Data de Nascimento: "))

    data_nascimento_formatada = Formatar_Data(data_nascimento)

    tempo_agora = dt.datetime.now()
    data_atual = tempo_agora.strftime('%d-%m-%Y')
    data_atual_formatada = Formatar_Data(data_atual)

    idade_dias = data_atual_formatada - data_nascimento_formatada
    idade = idade_dias.days/365
    
    DATA_NASCIMENTO.append(int(idade))
    
    return int(idade)


#1.2.1 Recebe uma Str no formato(dia-mês-ano), e Retorna um tipo composto operavel.
def Formatar_Data(data_pura):
    data_pura_separada = data_pura.split("-")
    dia_nascimento = int(data_pura_separada[0])
    mes_nascimento = int(data_pura_separada[1])
    ano_nascimento = int(data_pura_separada[2])

    data_formatadata = dt.date(ano_nascimento, mes_nascimento, dia_nascimento)

    return data_formatadata


#1.3 Responsavel por receber, validar a quantidade de caracters e salvar no vetor.
def Cadastro_Cpf():
    cpf = str(input("CPF Cliente: "))

    while len(cpf) != 11:
        cpf = str(input("CPF Invalido|CPF Cliente: "))

    CPF.append(cpf)

    return cpf


#1.4 Responsavel por receber, e salvar o sexo do cliente no vetor.
def Cadastro_Sexo():
    genero = str(input("Sexo Cliente[M|F]: "))

    while genero != "m" and genero != "M" and genero != "f" and genero != "F":
        genero = str(input("Sexo invalido|Sexo Cliente[M|F]: "))

    if genero == "m" or genero == "M":
        sexo = "Homem"
    else:
        sexo = "Mulher"

    SEXO.append(sexo)

    return sexo


#2.0 Essa é a função principal da Lista dos clientes, nela vamos chamar as complementares
def Lista_Clientes():
    print("Esses sao todos seus clientes !!!")

    for i in range(len(NOME)):
        print(f"{i+1} - {NOME[i]}")

    escolha = str(input())

    if escolha == "":
        Voltar_Menu()

    if int(escolha)<1 or int(escolha)>len(NOME):
        print("Erro!!!")
    else:
        Ver_Cliente(int(escolha)-1)

    Voltar_Menu()
        

#2.1 Sera responsavel por printar os dados especificos dos clientes.
def Ver_Cliente(cliente):
    Limpa()

    print(f"{NOME[int(cliente)-1]}")
    print(f"\tCPF:{CPF[int(cliente)-1]}")
    print(f"\tIdade:{DATA_NASCIMENTO[int(cliente)-1]}")
    print(f"\tGenero:{SEXO[int(cliente)-1]}")


Menu()