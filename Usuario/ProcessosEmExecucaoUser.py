from VariaveisGlobaisEUtilidades import *

def info_processos_do_sistema_view(proList):
    for i in proList:
        print("\nNome: " + i["name"] + " - Pid: " + str(i["pid"]) + "\nNumero de threads: " + str(i["num_threads"]) + "\nUso de CPU: " + str(i["cpu_percent"]) + " %"+ "\nUso de memoria: " + str(i["memory_percent"]) + " %")


##########################################################################################
############### sched function ###########################################################
"""
    *Utilizar o módulo ‘sched’ para chamar as funções criadas no TP4 que retornam as informações sobre diretórios e arquivos.
    *Realizar um escalonamento das chamadas das funções com o módulo ‘sched’ e medir o tempo total utilizado por cada chamada com o módulo ‘time’.
     Você pode escolher com quais funções do seu projeto realizar o escalonamento, deixando indicado no relatório.
    *Dentro do escalonamento realizado na questão anterior, realizar uma comparação dos tempos obtidos com a quantidade total de clocks utilizados pela 
    CPU para a realização dessas mesmas chamadas.
"""
"""def printClockTIme():
    print('\nOs processos demoram',time.clock(),'segundos\n')

def schedFunc():
    s = sched.scheduler(time.time, time.sleep)

    s.enter(1, 1, info_directorio_arquivo,())
    s.enter(1, 2, info_processos_do_sistema,())
    s.enter(1, 3, printClockTIme,())

    s.run()"""

##########################################################################################
