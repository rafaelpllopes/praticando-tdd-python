import sys

class Usuario:

    def __init__(self, nome, carteira=0):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor: float):
        if valor > self.__carteira:
            raise  ValueError('Não pode propor um lance com o valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
           raise ValueError('Erro ao propor lance')

class Avaliador:

    def __init__(self):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor

            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
