# -*- coding: latin1 -*-
import os

def converteCparaF(graus=0):
    F = 9/5 * graus + 32
    clear()
    print ("Fahrenheit: %dF°") % F

def converteFparaC(graus=0):
    C = float(graus-32)/1.8
    clear()
    print ("Celsius:%dC°") % C

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def xavier(OP):
    if(OP==1):
        x = int(raw_input("Entre com a tenperatura: "))
        converteFparaC(x)
        tela()
    elif(OP==2):
        x = int(raw_input("Entre com a temperatura: "))
        converteCparaF(x)
        tela()

def tela():
    try:
        print("==========================================")
        print("=========Conversão de Temperatura=========")
        print("         1-Fahrenheit para Celsius ")
        print("         2-Celsius para Fahrenheit ") 
        print("         3-Sair")
        OP = int(raw_input("Escola a Opção: "))
    except ValueError:
        print("Escolha um numero entre 1 a 3")
        clear()
    except:
        print("Erro desconhecido")
    if(OP==3):
        clear()
        print("Obrigado por usar o programa")
    else:
        xavier(OP)
clear()
tela()
