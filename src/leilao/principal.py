from src.leilao.dominio import Usuario, Lance, Leilao

usuario1 = Usuario('Usuario1')
usuario2 = Usuario('Usuario2')

lance_do_usuario1 = Lance(usuario1, 100.0)
lance_do_usuario2 = Lance(usuario2, 100.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_usuario1)
leilao.lances.append(lance_do_usuario1)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')