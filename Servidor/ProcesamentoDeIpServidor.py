import psutil, SumarioDeProcesamentoServidor

##########(Details) IP #######################################
def ip_details_server_return():
    ipReturnList = []
    
    ipReturnList.append(SumarioDeProcesamentoServidor.ip_summary_server_return())
    ipReturnList.append(psutil.net_if_addrs())

    return ipReturnList