import pygame,math, time#, socket, subprocess, cpuinfo, os, sched, platform, nmap, psutil

##################### Variaieis Globais #################################################

horizontalSize = 800
verticalSize = 600

margin = horizontalSize/10/2
leterLeftSpaceing = horizontalSize/10/4

sizeOfPercentileLine = horizontalSize-margin-margin
percentilePineThickness = int(verticalSize/10/2+10)

areaSeparation = verticalSize/10/2

pygame.init()
DISPLAY = pygame.display
SCREEN = DISPLAY.set_mode([horizontalSize,verticalSize])
DISPLAY.set_caption("Arquitetura de Computadores, Sistemas Operacionais e Redes")
clockPygame = pygame.time.Clock()

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (251, 225, 118)

fontSize = int(verticalSize/10/2)
font = pygame.font.SysFont(None, fontSize)

spaceing = areaSeparation+percentilePineThickness
#########################################################################################

################### Funções de Utilidade ################################################
def print_text(textToShow,numerOfSpacing):
    render = font.render(textToShow,0,YELLOW)
    SCREEN.blit(render, (leterLeftSpaceing,spaceing*numerOfSpacing+percentilePineThickness))

def draw_Bar(numerOfSpacing,redSize,blueSize):
    pygame.draw.rect(SCREEN, RED, [margin, spaceing*numerOfSpacing,redSize, percentilePineThickness])
    pygame.draw.rect(SCREEN, BLUE, [(margin+redSize), spaceing*numerOfSpacing, blueSize, percentilePineThickness])

def bytes_to_kbyte(pers):
    return math.ceil(pers/1000)
##########################################################################################
