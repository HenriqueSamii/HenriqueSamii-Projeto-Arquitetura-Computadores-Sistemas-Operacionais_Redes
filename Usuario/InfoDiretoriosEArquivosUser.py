from VariaveisGlobaisEUtilidades import *

def info_directorio_arquivo_view(holder):
    for i in holder:
        print("\n" + holder[i][3] + " " + i)
        print("Tamanho: " + holder[i][0] + "\nTempo de criação: "+ holder[i][1] +"\nTempo de ultima modificação: "+ holder[i][2]+"\nLocal: "+ holder[i][4])
