import speech_recognition as sr
from nltk import word_tokenize, corpus
from scraper import *
import json

IDIOMA_CORPUS = "portuguese"
CAMINHO_CONFIG = "config.json"
IDIOMA_FALA = "pt-BR"

ATUADORES = [
    {
        "nome": "área",
        "parametro_de_atuacao": None,
        "atuar": atuar_area
    },
    {
        "nome": "flora",
        "parametro_de_atuacao": None,
        "atuar": atuar_flora
    },
    {
        "nome": "fauna",
        "parametro_de_atuacao": None,
        "atuar": atuar_fauna
    },
    {
        "nome": "afluentes",
        "parametro_de_atuacao": None,
        "atuar": atuar_afluentes
    },
    {
        "nome": "clima",
        "parametro_de_atuacao": None,
        "atuar": atuar_clima
    },
    {
        "nome": "população",
        "parametro_de_atuacao": None,
        "atuar": atuar_população
    }
]

def iniciar():
    iniciado = False
    
    reconhecedor = sr.Recognizer()
    
    try:
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))
        with open(CAMINHO_CONFIG, "r") as arquivo_de_configuracao:
            configuracao = json.load(arquivo_de_configuracao)

            nome_do_assistente = configuracao["nome"]
            acoes = configuracao["acoes"]
            
            arquivo_de_configuracao.close()
            
        iniciado = True

        print("Olá! Sou GEOvana, sua assistente virtual!")

    except:
        #erros do assistente
        ...
        
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["iniciar"]()
        atuador["parametro_de_atuacao"] = parametro_de_atuacao
                        
    return iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes
    
def escutar_fala(reconhecedor):
    tem_fala = False
    
    with sr.Microphone() as fonte_de_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_de_audio)
        print("Fale algo...")
        try:
            fala = reconhecedor.listen(fonte_de_audio, timeout = 6)
            tem_fala = True
        except:
            #erros de captura de fala
            ...

    return tem_fala, fala

def processar_teste(audio, reconhecedor):
    tem_transcricao = False
    
    with sr.AudioFile(audio) as fonte_de_audio:
        fala = reconhecedor.listen(fonte_de_audio)
        try:
            fala = reconhecedor.recognize_google(fonte_de_audio, language = IDIOMA_FALA)
            tem_transcricao = True
        except:
            #erros em audios gravados
            ...
    
    return tem_transcricao, fala.lower

def transcrever_fala(fala, reconhecedor):
    tem_transcricao = False
    
    try:
        transcricao = reconhecedor.recognize_google(fala, language = IDIOMA_FALA)
        tem_transcricao = True
    except:
        #erros de transcricao
        ...
    
    return tem_transcricao, transcricao.lower

def tokenizar_transcricao(transcricao):
    return word_tokenize(transcricao)
    
def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []
    
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)
    
    return tokens_filtrados
    
def validar_comando(tokens, nome_do_assistente, acoes):
    valido, acao, objeto = False, None, None
    
    if len(tokens) >= 3:
        if nome_do_assistente == tokens[0]:
            acao = tokens[1]
            objeto = tokens[2]
            
        for acao_cadastrada in acoes:
            if acao == acao_cadastrada["nome"]:
                if objeto in acao_cadastrada["objetos"]:
                    valido = True

                    break

    return valido, acao, objeto

def executar_comando(acao, objeto):
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["parametro_de_atuacao"]
        atuou = atuador["atuar"](acao, objeto, parametro_de_atuacao)
        
        if atuou:
            break
    
if __name__ == "__main__":
    iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
    
    if iniciado:
        while True:
            tem_fala, fala = escutar_fala(reconhecedor)
            if tem_fala:
                tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
                if tem_transcricao:
                    tokenizar_transcricao(transcricao) #adicionar "tokens = tokenizar_transcricao(transcricao)" em caso de erro
                    tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
                    
                    valido, acao, objeto = validar_comando(tokens, nome_do_assistente, acoes)
                    if valido:
                        executar_comando(acao, objeto)
                    else:
                        print(f"comando inválido, tente novamente!")