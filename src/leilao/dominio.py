from src.leilao.exececoes import LanceInvalido


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
        if not self._valor_eh_valido(valor):
            raise LanceInvalido('Não pode propor um lance com o valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        if self.lance_eh_valido(lance):
            if not self._tem_lance():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def _tem_lance(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuario não pode dar dois lances seguidos')

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')

    def lance_eh_valido(self, lance):
        return not self._tem_lance() or \
               (self._usuarios_diferentes(lance) and self._valor_maior_que_lance_anterior(lance))


class Avaliador:

    def __init__(self):
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor

            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
