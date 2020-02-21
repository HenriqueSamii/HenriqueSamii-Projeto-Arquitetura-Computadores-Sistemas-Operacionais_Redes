import socket, sched, time, os, pickle, ProcesamentoDeDiscoUser, VariaveisGlobaisEUtilidades,SumarioDeProcesamentoUser, ProcesamentoDeMemoriaUser, ProcesamentoDeCPUUser, ProcesamentoDeIpUser, InfoDiretoriosEArquivosUser, ProcessosEmExecucaoUser, SubredesEPortsUserServidor, NetworkInfoUser
from VariaveisGlobaisEUtilidades import *

localCarrosel = 0
numeroDeItens = 7

clear = lambda: os.system('cls')

ended = False
clockTick = 60
segundosDeRefesh = 40
refreshRatePygame = 20
refreshRateConsole = segundosDeRefesh*clockTick

refresh = 0

move_ticker_processos_directorio = 0

def print_func(texto):
    print(texto)
def sched_func(lista):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, print_func,argument=("Informações de Diretorios e Arquivos irmãos da pasta do servidor:",))
    s.enter(2, 1, InfoDiretoriosEArquivosUser.info_directorio_arquivo_view,argument=(lista[0],))

    s.enter(3, 1, print_func,argument=("\n\n########################\nProcessos em Execução:",))
    s.enter(4, 1, ProcessosEmExecucaoUser.info_processos_do_sistema_view,argument=(lista[1],))
    s.run()

while not ended:
    clockPygame.tick(clockTick)
    pygame.display.update()

    refresh += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if localCarrosel == numeroDeItens:
                    localCarrosel = 0
                else:
                    localCarrosel += 1
            elif event.key == pygame.K_LEFT:
                if localCarrosel == 0:
                    localCarrosel = numeroDeItens
                else:
                    localCarrosel -= 1
            refresh = 0
        if event.type == pygame.QUIT:
            ended = True

    
    if localCarrosel >= 0 and localCarrosel < 5:
        if refresh == refreshRatePygame:
            refresh = 0
    elif localCarrosel >=  5:
        if refresh == refreshRateConsole:
            refresh = 0

    try:
        if refresh == 0:
            clear()
            lista = []
            input_dir = str(localCarrosel)
            socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            port = 9999

            socket_cliente.connect((host, port))

            socket_cliente.send(input_dir.encode('ascii'))

            data = b""
            while True:
                packet = socket_cliente.recv(1024)
                if not packet: break
                data += packet
            lista = pickle.loads(data)

            SCREEN.fill(pygame.Color("black"))
            if input_dir == "0":
                SumarioDeProcesamentoUser.processing_summary(lista)
            elif input_dir == "1":
                ProcesamentoDeMemoriaUser.memory_details_user_interface(lista)
            elif input_dir == "2":
                ProcesamentoDeCPUUser.cpu_details_user_interface(lista)
            elif input_dir == "3":
                ProcesamentoDeDiscoUser.disc_details_user_interface(lista)
            elif input_dir == "4":
                ProcesamentoDeIpUser.ip_details_user_interface(lista)
            elif input_dir == "5":
                print_text("Duas funções neste ecrã",0.5)
                print_text(" - Informações de Diretorios e Arquivos irmãos da pasta do servidor",1.5)
                print_text(" - Processos em Execução",2)
                #InfoDiretoriosEArquivosUser.info_directorio_arquivo_view(lista[0])
                #ProcessosEmExecucaoUser.info_processos_do_sistema_view(lista[1])
                sched_func(lista)
            elif input_dir == "6":
                print_text("Subredes e Ports",0.5)
                SubredesEPortsUserServidor.print_masks_and_ports(lista)
            elif input_dir == "7":
                print_text("Informações da Rede",0.5)
                NetworkInfoUser.network_information_user_view(lista)
                
        
        
            socket_cliente.close()
    except:
        pass
pygame.quit()