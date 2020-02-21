import psutil,time

def network_information_server():
    interfaces = psutil.net_if_addrs()
    status = psutil.net_if_stats()
    networkInfoList = []
    networkInfoList.append(interfaces)
    networkInfoList.append(status)
    time.sleep(1)
    io_status = psutil.net_io_counters(pernic=True)
    networkInfoList.append(io_status)
    return networkInfoList
