import os, time

def info_directorio_arquivo():
    """*Criar uma ou mais funções que retornem ou apresentem informações sobre diretórios e arquivos. Tais informações podem ser qualquer uma que você 
    achar relevante disponível no módulo ‘os’ e ‘psutil’ de Python, como nome, tamanho, localização, data de criação, data de modificação, tipo, etc."""
    listaDir = os.listdir()
    dic = {}
    for i in listaDir:
        dic[i] = []
        dic[i].append(str(os.stat(i).st_size) + ' bytes') # Tamanho
        dic[i].append(time.ctime(os.stat(i).st_atime)) # Tempo de criação
        dic[i].append(time.ctime(os.stat(i).st_mtime)) # Tempo de modificação
        if (os.path.isfile(i)):
            dic[i].append("Arquivo")
        elif (os.path.isdir(i)):
            dic[i].append("Directorio")
        dic[i].append(os.path.abspath(i))
        
    return dic
