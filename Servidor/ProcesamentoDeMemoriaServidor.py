import psutil, SumarioDeProcesamentoServidor

##########(Details) Memory #######################################
def memory_details_server_return():
    memoryServerInfoReturn = []
    memoryServerInfoReturn.append(SumarioDeProcesamentoServidor.memory_summary_server_return())
    memoryServerInfoReturn.append(psutil.virtual_memory().total)
    memoryServerInfoReturn.append(psutil.virtual_memory().available)
    memoryServerInfoReturn.append(psutil.swap_memory().used)
    memoryServerInfoReturn.append(psutil.swap_memory().sin)
    memoryServerInfoReturn.append(psutil.swap_memory().sout)
    
    return memoryServerInfoReturn