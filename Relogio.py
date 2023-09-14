#Aqui temos um Relogio

import datetime as dt
import time
import os

def Limpa(): # def para limpar menu{BIBLIOTECA OS}
     if os.name == 'nt': 
        _ = os.system('cls')


def Hora_formatada():
    tempo_agora = dt.datetime.now()
    hora = tempo_agora.strftime('%H:%M:%S')

    return hora


def Dia_Formatado():
    dias_semana = ["Domingo", "Segunda-Feira", "Terça-feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sabado"]
    data = dt.date.today()
    numero_dia_semana = data.weekday()
    dia = dias_semana[numero_dia_semana]

    return dia


def Data_Formatada():
    tempo_agora = dt.datetime.now()
    data = tempo_agora.strftime('%d-%m-%Y')

    return data 

continuar = True
while continuar:
    dia = Dia_Formatado()
    hora = Hora_formatada()
    data = Data_Formatada()

    print(f"--------{dia}--------")
    print(f"------- {data} --------")
    print(f"\n         {hora}")
    time.sleep(1)
    Limpa()



#Output:
# -------- Terça-feira --------
# -------   13-09-2023  -------
#            22:42:57