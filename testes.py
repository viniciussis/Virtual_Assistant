from assistente_virtual import *
import unittest

CHAMANDO_GEOVANA = "link/caminho"
CHAMANDO_OUTRA_COISA = "link/caminho"
LIGAR_LAMPADA = "link/caminho"
DESLIGAR_LAMPADA = "link/caminho"

class TesteNomeAssistente(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, _, self.nome_do_assistente, _ = iniciar()
    
    def testar_01_reconhecedor_nome(self):
        tem_transcricao, transcricao = processar_teste(CHAMANDO_GEOVANA, self.reconhecedor)

        self.assertTrue(tem_transcricao)
        
        tokens = tokenizar_transcricao(transcricao)
        self.assertEqual(tokens[0], self.nome_do_assistente)

    def testar_02_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = processar_teste(CHAMANDO_OUTRA_COISA, self.reconhecedor)

        self.assertTrue(tem_transcricao)
        
        tokens = tokenizar_transcricao(transcricao)
        self.assertNotEqual(tokens[0], self.nome_do_assistente)
        
class TesteLampada(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()
    
    def testar_01_ligar_lampada(self):
        tem_transcricao, transcricao = processar_teste(LIGAR_LAMPADA, self.reconhecedor)

        self.assertTrue(tem_transcricao)
        
        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        
        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

    def testar_02_desligar_lampada(self):
        tem_transcricao, transcricao = processar_teste(DESLIGAR_LAMPADA, self.reconhecedor)

        self.assertTrue(tem_transcricao)
        
        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        
        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)


""" if __name__ == "__main__":
    iniciado, reconhecedor, _, _, _ = iniciar()
    
    if iniciado:
        tem_transcricao, transcricao = processar_teste(CHAMANDO_GEOVANA, reconhecedor)
        if tem_transcricao:
            print(f"") """
            
if __name__ == "__main__":
    carregador = unittest.TestSuite() 
    testes = unittest.TestSuite()
    
    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteLampada))
    
    executor = unittest.TextTestRunner()
    executor