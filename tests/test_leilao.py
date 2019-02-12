from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador
from src.leilao.exececoes import LanceInvalido


class Test_Leilao(TestCase):

    def setUp(self):
        self.usuario1 = Usuario('Usuario1')
        self.usuario2 = Usuario('Usuario2')
        self.usuario3 = Usuario('Usuario3')
        self.lance_do_usuario1 = Lance(self.usuario1, 100.0)
        self.lance_do_usuario2 = Lance(self.usuario2, 150.0)
        self.lance_do_usuario3 = Lance(self.usuario3, 200.0)
        self.leilao = Leilao('Celular')


    def test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_do_lance(self):
        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(self.lance_do_usuario2)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_nao_deve_permitir_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_usuario2)
            self.leilao.propoe(self.lance_do_usuario1)
            self.assertEqual(100.0, self.leilao.menor_lance)
            self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_tres_lance(self):
        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(self.lance_do_usuario2)
        self.leilao.propoe(self.lance_do_usuario3)
        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(200.0, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_usuario1)
        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_usuario1)
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def text_deve_permitir_propor_um_lance_caso_o_ultimo_usario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(self.lance_do_usuario2)

        quantidade_de_lances_recebida = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebida)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_mesmo(self):
        """
        try:
            self.leilao.propoe(self.lance_do_usuario1)
            self.leilao.propoe(self.lance_do_usuario1)
            self.fail(msg='Não Lancou exeção')
        except ValueError:
            quantidade_de_lances_recebidos = len(self.leilao.lances)
            self.assertEqual(1, quantidade_de_lances_recebidos)
        """
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_usuario1)
            self.leilao.propoe(self.lance_do_usuario1)