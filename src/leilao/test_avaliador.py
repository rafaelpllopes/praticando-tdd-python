from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        self.usuario1 = Usuario('Usuario1')
        self.usuario2 = Usuario('Usuario2')
        self.usuario3 = Usuario('Usuario3')
        self.lance_do_usuario1 = Lance(self.usuario1, 100.0)
        self.lance_do_usuario2 = Lance(self.usuario2, 150.0)
        self.lance_do_usuario3 = Lance(self.usuario3, 200.0)
        self.leilao = Leilao('Celular')


    def test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_do_lance(self):
        self.leilao.lances.append(self.lance_do_usuario1)
        self.leilao.lances.append(self.lance_do_usuario2)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def test_quando_adicionados_em_ordem_crescente_deve_retornar_o_menor_e_o_maior_valor_do_lance(self):
        self.leilao.lances.append(self.lance_do_usuario2)
        self.leilao.lances.append(self.lance_do_usuario1)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_tres_lance(self):
        self.leilao.lances.append(self.lance_do_usuario1)
        self.leilao.lances.append(self.lance_do_usuario2)
        self.leilao.lances.append(self.lance_do_usuario3)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.0, avaliador.menor_lance)
        self.assertEqual(200.0, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.lances.append(self.lance_do_usuario1)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.0, avaliador.menor_lance)
        self.assertEqual(100.0, avaliador.maior_lance)
        