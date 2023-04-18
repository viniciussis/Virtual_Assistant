import pygame

MUSICA = "/portadamusica"

def iniciar_musica(musica = MUSICA):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(musica)

    return None

def atuar_tocador(acao, objeto):
    executado = False
    
    if acao == "tocar" and objeto == "música":
        executado = True
        pygame.mixer.music.play()
    elif acao == "parar" and objeto == "música":
        executado = True    
        pygame.mixer.music.stop()
    
    return executado