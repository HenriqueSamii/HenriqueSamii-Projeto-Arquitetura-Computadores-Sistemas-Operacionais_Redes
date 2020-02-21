from VariaveisGlobaisEUtilidades import *

########## server/user (Summary) Funções para a Barra de Espaco  ###############

### Memory
def memory_summary_user_interface(spacing=0, serverReturn = []):
    print_text("MEMORY - "+ str(serverReturn[0]) + "% Free",spacing)
    draw_Bar(spacing+1,sizeOfPercentileLine-serverReturn[1],serverReturn[1])

### CPU
def cpu_summary_user_interface(spacing=0, serverReturn = []):
    print_text("CPU Total - " + str(100-serverReturn) + "% Free",spacing)
    draw_Bar(spacing+1,serverReturn,sizeOfPercentileLine-serverReturn)

### Disc
def disc_summary_user_interface(spacing=0, serverReturn = []):
    print_text("DISC - "+ str(100-serverReturn[0]) + "% Free",spacing)
    draw_Bar(spacing+1,serverReturn[1],sizeOfPercentileLine-serverReturn[1])

### IP
def ip_summary_user_interface(spacing=0, serverReturn = []):
    print_text("IP - "+ str(serverReturn),spacing)

##########################################################################################

def processing_summary(summary_server_return):
    memory_summary_user_interface(0,summary_server_return[0])
    cpu_summary_user_interface(2, summary_server_return[1])
    disc_summary_user_interface(4,summary_server_return[2])
    ip_summary_user_interface(6,summary_server_return[3])