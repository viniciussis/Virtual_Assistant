import serial
from time import sleep

PORTA_LAMPADA = "/portadalampada"

LIGAR = b'L'
DESLIGAR = b'D'

def iniciar_lampada(porta = PORTA_LAMPADA):
    porta_lampada = serial.Serial(port = porta, baudrate = 9600, bytesize = 8, timeou = 2,stopbits=serial)
    
    return porta_lampada

def atuar_lampada(acao, objeto, porta_lampada):
    executado = False
    
    if acao == "ligar" and objeto == "lampada":
        executado = True
        porta_lampada.write(LIGAR)
    elif acao == "desligar" and objeto == "lâmpada":
        executado = True
        porta_lampada.write(DESLIGAR)
    
    return