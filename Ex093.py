jogador = dict()
jogos = []
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    jogos.append(int(input(f'Quantos gols na partida {i+1} ? ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogos)
print('=' * 30)
print(jogador)
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}')
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f' Totalizando {jogador["total"]} gols.')
