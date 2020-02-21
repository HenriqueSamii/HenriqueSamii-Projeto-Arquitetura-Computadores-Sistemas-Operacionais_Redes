# HenriqueSamii-Projeto-Arquitetura-Computadores-Sistemas-Operacionais_Redes

Um aplicativo simples de apresentação textual do monitoramento e análise de computadores em rede. Ele deverá ser implementado em Python usando módulos como psutil (para capturar dados do sistema computacional) e sockets (para criar cliente e servidor) e será desenvolvido de forma incremental durante o curso. A apresentação gráfica no lado cliente é opcional e pode ser parcial (parte gráfica e parte texto).

Você deve fazer com que seu programa cliente apresente todas as informações presentes nos TPs 4, 5, 6 e 7. Tais informações devem ser obtidas da máquina onde o processo servidor está executando. Portanto, o processo servidor deve obtê-las e enviar ao processo cliente.

Lembre-se que as informações requisitadas são:

   
    1. Capturas das informações dos diretórios, como nome, tamanho, localização, data de criação, data de modificação, tipo, etc.
    
    2. Capturas das informações dos processos do sistema, como PID, nome do executável, consumo de processamento, consumo de memória.
    
    3. Escalonamento das chamadas das funções com o módulo ‘sched’ e medição do tempo total utilizado por cada chamada com o módulo ‘time’.
    
    4. Informações sobre as máquinas pertencentes à sub-rede do IP específico.
    
    5. Informações sobre as portas dos diferentes IPs obtidos nessa sub-rede.
    
    6. Ao menos 3 informações de interfaces de redes (exemplos: interfaces disponíveis, IP, gateway, máscara de subrede, etc.).

    7. A criação do cliente e servidor.
