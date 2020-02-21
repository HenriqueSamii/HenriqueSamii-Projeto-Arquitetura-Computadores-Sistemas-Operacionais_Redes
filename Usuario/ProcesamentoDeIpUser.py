from VariaveisGlobaisEUtilidades import *
import SumarioDeProcesamentoUser

##########(Details) IP #######################################
def ip_details_user_interface(serverReturn = []):

    spacingIpText = 0.5

    SumarioDeProcesamentoUser.ip_summary_user_interface(0,serverReturn[0])
    for target_list in serverReturn[1]:
        print_text("   - " + str(target_list),spacingIpText)
        spacingIpText+=0.5

##########################################################################################
