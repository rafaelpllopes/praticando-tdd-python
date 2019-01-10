from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

usuario1 = Usuario('Usuario1')
usuario2 = Usuario('Usuario2')

lance_do_usuario1 = Lance(usuario1, 100.0)
lance_do_usuario2 = Lance(usuario2, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_usuario1)
leilao.lances.append(lance_do_usuario2)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance de {avaliador.maior_lance}')