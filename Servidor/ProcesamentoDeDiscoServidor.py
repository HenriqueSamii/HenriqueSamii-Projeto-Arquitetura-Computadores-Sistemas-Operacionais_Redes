import psutil,SumarioDeProcesamentoServidor

##########(Details) Disc #######################################
def disc_details_server_return():
    discServerInfoReturn = []
    discServerInfoReturn.append(SumarioDeProcesamentoServidor.disc_summary_server_return())
    discServerInfoReturn.append(psutil.disk_io_counters().read_count)
    discServerInfoReturn.append(psutil.disk_io_counters().write_count)
    discServerInfoReturn.append(psutil.disk_io_counters().read_bytes)
    discServerInfoReturn.append(psutil.disk_io_counters().write_bytes)
    discServerInfoReturn.append(psutil.disk_io_counters().read_time//1000)
    discServerInfoReturn.append(psutil.disk_io_counters().write_time//1000)
    
    return discServerInfoReturn