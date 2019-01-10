from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        usuario1 = Usuario('Usuario1')
        usuario2 = Usuario('Usuario2')

        lance_do_usuario1 = Lance(usuario1, 100.0)
        lance_do_usuario2 = Lance(usuario2, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_usuario1)
        leilao.lances.append(lance_do_usuario2)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
