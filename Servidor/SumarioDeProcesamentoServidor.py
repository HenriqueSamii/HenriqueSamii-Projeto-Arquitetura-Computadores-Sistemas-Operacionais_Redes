import psutil,socket

########## server/user (Summary) Funções para a Barra de Espaco  ###############
horizontalSize = 800
margin = horizontalSize/10/2
sizeOfPercentileLine = horizontalSize-margin-margin

### Memory
def memory_summary_server_return():
    memoryList = []

    memoryTotal = psutil.virtual_memory().total
    memoryAvailable = psutil.virtual_memory().available
    percentileAvailable = (memoryAvailable*sizeOfPercentileLine)//memoryTotal

    memoryList.append(((memoryAvailable*100)//memoryTotal))
    memoryList.append(percentileAvailable)
    
    return memoryList

### CPU
def cpu_summary_server_return():
    percentileInUse = psutil.cpu_percent()
    return percentileInUse

### Disc
def disc_summary_server_return():
    discList = []
    discPrecentUsed = psutil.disk_usage('/').percent
    discPrecentUsedRound = int(round(discPrecentUsed))
    
    discList.append(discPrecentUsedRound)
    discList.append((discPrecentUsedRound*sizeOfPercentileLine)//100)
    return discList

### IP
def ip_summary_server_return():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

###Retornar SUmario Completo

def processing_summary():
    listaDePreocessa = [memory_summary_server_return(),cpu_summary_server_return(),disc_summary_server_return(),ip_summary_server_return()]
    return listaDePreocessa