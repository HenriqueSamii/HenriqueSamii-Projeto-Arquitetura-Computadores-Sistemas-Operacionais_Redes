import psutil,platform,subprocess,os,socket,nmap
##########################################################################################
""""
Este TP6 corresponde à continuação do TP5. Agora, você irá introduzir no seu programa informações sobre subrede de um IP especificado e sobre as portas desse IP.
A partir de então, você terá mais liberdade para criar a forma de visualização das informações da maneira que desejar e de acordo com seu orientador. 
Certifique-se apenas que está realizando o básico do que este TP requisita.

A seguir, os requisitos básicos:

    Criar uma ou mais funções que retornem ou apresentem informações sobre as máquinas pertencentes à sub-rede do IP específico.
    Usar a função em seu programa para mostrar o resultado. O resultado pode ser em texto formatado impresso na tela ou gráfico, usando o módulo ‘pygame’.
    Criar uma ou mais funções que retornem ou apresentem informações sobre as portas dos diferentes IPs obtidos nessa sub rede.
    Usar a função em seu programa para mostrar o resultado. O resultado pode ser em texto formatado impresso na tela ou gráfico, usando o ‘pygame’.
"""
def retorna_codigo_ping(hostname):
    plataforma = platform.system()
    args = []

    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]
    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]
        
    ret_cod = subprocess.call(args,stdout=open(os.devnull, 'w'),stderr=open(os.devnull, 'w'))
    return ret_cod

def verifica_hosts(base_ip):
    host_validos = []
    return_codes = dict()

    for i in range(1, 100):#255
        return_codes[base_ip + '{0}'.format(i)] =   retorna_codigo_ping(base_ip + '{0}'.format(i))
        if return_codes[base_ip + '{0}'.format(i)] == 0:
            host_validos.append(base_ip + '{0}'.format(i))
    
    return host_validos


def info_portas_do_ip(listaDeHosts):
    nm = nmap.PortScanner()
    for i in listaDeHosts:
        try:
            nm.scan(i)
            print(""+ i + "\nNome - "+ nm[i].hostname())
        except:
            pass
"""def info_portas_do_ip(listaDeHosts):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for ip in listaDeHosts:
        print(ip)
        for porta in range(1,1025):
            try:
                result = s.connect_ex((ip, porta))
                if result == True:
                    print ("Porta "+ porta + ": Aberta")
                else:
                    print ("Porta "+ porta + ": Fechada")
            except:
                print("Error")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for ip in listaDeHosts:
            print(ip)
            for porta in range(1,1025):
                result = s.connect_ex((ip, porta))
                if result == True:
                    print ("Porta "+ porta + ": Aberta")
                else:
                    print ("Porta "+ porta + ": Fechada")
                #s.close()
    except:
        pass"""
        

def print_masks_and_ports(ipProucura):
    #ip_string = input("Entre com o ip alvo: ")
    ip_string = ipProucura
    ip_lista = ip_string.split('.')
    base_ip = ".".join(ip_lista[0:3]) + '.'
    print("O teste será feito na sub rede: ", base_ip)
    listaDeHosts = verifica_hosts(base_ip)
    print("Subredes:")
    print(listaDeHosts)
    #info_portas_do_ip(listaDeHosts)

##########################################################################################

if __name__ == "__main__":
    print_masks_and_ports() 