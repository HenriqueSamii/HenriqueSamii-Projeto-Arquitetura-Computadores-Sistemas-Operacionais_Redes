import psutil,cpuinfo

##########(Details) CPU #######################################
def cpu_details_server_return():
    cpuServerInfoReturn = []
    cpuServerInfoReturn.append(psutil.cpu_count(logical=False))
    cpuServerInfoReturn.append(psutil.cpu_count())
    cpuServerInfoReturn.append(psutil.cpu_freq().max)
    cpuServerInfoReturn.append(psutil.cpu_freq().current)
    cpuServerInfoReturn.append(psutil.cpu_times().user)
    cpuServerInfoReturn.append(cpuinfo.get_cpu_info())
    cpuServerInfoReturn.append(psutil.cpu_percent(percpu=True))
    return cpuServerInfoReturn