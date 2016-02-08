# -*- coding: latin1 -*-'
import zipfile
import os
import glob
import string


def zipagem(arquivo):
    try:
        os.system('clear')
        print ("Arquivo a ser zipado %s") % arquivo
        zip = zipfile.ZipFile('%s.zip' % arquivo, 'w',zipfile.ZIP_DEFLATED)
        zip.write('%s.py'% arquivo)
    except ValueError:
        print("Arquivo não encontrado")
    except:
        print("Erro desconhecido")   
    tela()

def listagem():
    for arq in sorted(glob.glob('*.py')):
        print arq
    x = raw_input("Digite o nome do arquivo que vai ser zipado: ")
    zipagem(x)
    
def tela():
    try:
        print """
            *********************************************************
            ******************PROGRAMA DE ZIPAGEM*******************

                            *******OPÇÕES*******

                            -1 LISTA ARQUIVOS
                            -2 COMPRIMIR ARQUIVO
                            -3 SAIR
            """
        OP = int(input("Escolha uma das opções: "))
    except ValueError:
            print("Escolha um numero entre 1 a 3")
    except:
            print("Erro desconhecido")

    if(OP==1):
        os.system('clear')
        listagem()
    elif(OP==2):
        arquivo = raw_input("Digite o nome do arquivo: ")
        zipagem(arquivo)
    elif(OP==3):
        print ("Obrigado por usar o programa")
        exit()
            
tela()
