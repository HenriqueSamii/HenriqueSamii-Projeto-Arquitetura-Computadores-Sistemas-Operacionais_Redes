import socket, os, pickle, ProcesamentoDeDiscoServidor, SumarioDeProcesamentoServidor, ProcesamentoDeMemoriaServidor, ProcesamentoDeCPUServidor, ProcesamentoDeIpServidor, InfoDiretoriosEArquivosServidor, ProcessosEmExecucaoServidor, NetworkInfoServidor
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

socket_servidor.bind((host, port))
socket_servidor.listen()
print("escutando na porta", port)
lista_resposta = []
while True:
    (cliente, cliente_addr) = socket_servidor.accept()
    print("conectado ao", str(cliente_addr))
    mensagem = cliente.recv(1024)
    pathS = mensagem.decode('ascii')

    try:
        #lista_resposta = []
        if pathS == "0":
            lista_resposta = SumarioDeProcesamentoServidor.processing_summary()
        elif pathS == "1":
            lista_resposta = ProcesamentoDeMemoriaServidor.memory_details_server_return()
        elif pathS == "2":
            lista_resposta = ProcesamentoDeCPUServidor.cpu_details_server_return()
        elif pathS == "3":
            lista_resposta = ProcesamentoDeDiscoServidor.disc_details_server_return()
        elif pathS == "4":
            lista_resposta = ProcesamentoDeIpServidor.ip_details_server_return()
        elif pathS == "5":
            lista_resposta = []
            lista_resposta.append(InfoDiretoriosEArquivosServidor.info_directorio_arquivo())
            lista_resposta.append(ProcessosEmExecucaoServidor.info_processos_do_sistema())
        elif pathS == "6":
            lista_resposta = socket.gethostbyname(socket.gethostname())
        elif pathS == "7":
            lista_resposta = NetworkInfoServidor.network_information_server()

        #retornar a cliente lista_resposta
        bytes_resp = pickle.dumps(lista_resposta)
        cliente.send(bytes_resp)
    except Exception as erro:
        print(str(erro))
    
    cliente.close()