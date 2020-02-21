from VariaveisGlobaisEUtilidades import *

##########(Details) CPU #######################################
def cpu_core_bars(cpuCores):
    blitLvlY=5
    cpuCoresPercent = cpuCores
    surfHorizontalSize = horizontalSize
    surfVerticalSize = spaceing*blitLvlY
    numberOfCores = len(cpuCoresPercent)
    barSpacing = (surfHorizontalSize//numberOfCores)/4
    barThikness = (surfHorizontalSize//numberOfCores)-(barSpacing*2)
    spacinfTotalPerBar = 0

    for i in cpuCoresPercent:
        pygame.draw.rect(SCREEN, BLUE, [barSpacing+(spacinfTotalPerBar*(barSpacing+barThikness)), surfVerticalSize, barThikness, verticalSize])
        pygame.draw.rect(SCREEN, RED, [barSpacing+(spacinfTotalPerBar*(barSpacing+barThikness)), surfVerticalSize,barThikness, (verticalSize*i)//100])
        spacinfTotalPerBar += 1



def cpu_details_user_interface(cpu_details):
    print_text("Physical Cores - "+ str(cpu_details[0]),0.5)
    print_text("Total Threads - "+ str(cpu_details[1]),1)
    print_text("Total Frequency - "+ str(cpu_details[2]) + " Mhz",1.5)
    print_text("Frequency In Use - "+ str(cpu_details[3]) + " Mhz",2)
    print_text("CPU User - "+ str(cpu_details[4]),2.5)
    print_text("CPU Architecture - "+ str(cpu_details[5]['arch']),3)
    print_text("CPU Brand - "+ str(cpu_details[5]['brand']),3.5)
    print_text("CPU Word - "+ str(cpu_details[5]['bits']),4)
    cpu_core_bars(cpu_details[6])

##########################################################################################