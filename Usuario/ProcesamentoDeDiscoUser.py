from VariaveisGlobaisEUtilidades import *
import SumarioDeProcesamentoUser
##########(Details) Disc #######################################
def disc_details_user_interface(disc_details):
    SumarioDeProcesamentoUser.disc_summary_user_interface(0,disc_details[0])
    print_text("Number of reads - " + str(disc_details[1]),1.5)
    print_text("Number of writes - "+ str(disc_details[2]),2)
    print_text("Number of bytes read - "+ str(disc_details[3]),2.5)
    print_text("Number of bytes written - "+ str(disc_details[4]),3)
    print_text("Read Time - "+ str(disc_details[5]) + " Seconds",3.5)
    print_text("Write Time - "+ str(disc_details[6]) + " Seconds",4)

##########################################################################################
