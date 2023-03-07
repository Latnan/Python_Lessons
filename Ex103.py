def ficha(nome='<desconhecido>', gol=0):
    print('*' * 40)
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


# código principal
jogador = str(input('Qual o nome do jogador? '))
pontos = str(input('Quantos gols ele marcou? '))
if pontos.isnumeric():
    pontos = int(pontos)
else:
    pontos = 0
if jogador.strip() == '':
    ficha(gol=pontos)
else:
    ficha(jogador, pontos)
