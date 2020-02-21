from VariaveisGlobaisEUtilidades import *
import SumarioDeProcesamentoUser

##########(Details) Memory #######################################
def memory_details_user_interface(memory_details):
    SumarioDeProcesamentoUser.memory_summary_user_interface(0,memory_details[0])
    print_text("Total Memory - "+ str(memory_details[1])+ " Bytes",1.5)
    print_text("Available Memory - "+ str(memory_details[2])+ " Bytes",2)
    print_text("Memory Used - "+ str(memory_details[3])+ " Bytes",2.5)
    print_text("Bytes swapped in from disk - "+ str(memory_details[4]),3)
    print_text("Bytes swapped out from disk - "+ str(memory_details[5]),3.5)
##########################################################################################
