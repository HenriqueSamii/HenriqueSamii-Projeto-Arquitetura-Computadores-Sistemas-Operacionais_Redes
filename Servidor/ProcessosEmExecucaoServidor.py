import psutil,os,time

def info_processos_do_sistema():
    """*Criar uma ou mais funções que retornem ou apresentem informações sobre processos do sistema. As informações podem ser: PID, nome do executável,
     consumo de processamento, consumo de memória, entre outras disponíveis no módulo ‘psutil’ de Python."""
    proList = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name','memory_percent','cpu_percent','num_threads'])
        except psutil.NoSuchProcess:
            pass
        else:
            proList.append(pinfo)
    
    return proList