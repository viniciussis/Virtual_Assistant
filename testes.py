import unittest
from assistente_virtual import *

CHAMANDO_GEOVANA = "sounds\Chamando-Geovana.wav"
CHAMANDO_OUTRO_NOME = "sounds\Chamando-Outro-Nome.wav"
COMANDO_AREA = "sounds\Comando-Area.wav"
COMANDO_FLORA = "sounds\Comando-Flora.wav"
COMANDO_FAUNA = "sounds\Comando-Fauna.wav"
COMANDO_AFLUENTES = "sounds\Comando-Afluentes.wav"
COMANDO_CLIMA = "sounds\Comando-Clima.wav"
COMANDO_POPULACAO = "sounds\Comando-Populacao.wav"
CHAMANDO_OUTRO_COMANDO = "sounds\Chamando-Outro-Comando.wav"

class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        iniciar()

    def teste_reconhecer_nome(self):

        _, reconhecedor, palavras_de_parada, _, _ = iniciar()
        tem_fala, fala = processar_testes(CHAMANDO_GEOVANA, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        nome_assistente = tokens[0].lower()
        print(f"nome do assistente: {nome_assistente}")
        self.assertIn("geovana", nome_assistente)

    def teste_nao_reconhecer_outro_nome(self):

        _, reconhecedor, palavras_de_parada, _, _ = iniciar()
        tem_fala, fala = processar_testes(CHAMANDO_OUTRO_NOME, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        nome_assistente = tokens[0].lower()
        print(f"nome do assistente: {nome_assistente}")
        self.assertNotIn("geovana", nome_assistente)

class TesteAcao(unittest.TestCase):
    ...
    def setUp(self):
        iniciar()
    
    def teste_area(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(COMANDO_AREA, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

    def teste_flora(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(COMANDO_FLORA, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

    def teste_fauna(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(COMANDO_FAUNA, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

    def teste_afluentes(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(COMANDO_AFLUENTES, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

    def teste_clima(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(COMANDO_CLIMA, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

    def teste_populacao(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(COMANDO_POPULACAO, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertTrue(valido)

    def teste_outro_comando(self):
        iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()
        self.assertTrue(iniciado)
        tem_fala, fala = processar_testes(CHAMANDO_OUTRO_COMANDO, reconhecedor)
        self.assertTrue(tem_fala)
        tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
        print(f"comando reconhecido: {transcricao}")
        self.assertTrue(tem_transcricao)
        tokens = tokenizar_transcricao(transcricao)
        tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)
        valido, _, _ = validar_comando(tokens, nome_do_assistente, acoes)
        self.assertFalse(valido)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteAcao))
    executor = unittest.TextTestRunner()
    executor.run(testes)
