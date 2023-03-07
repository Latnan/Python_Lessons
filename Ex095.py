time = []
jogos = []
jogador = dict()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogos.clear()
    for i in range(0, partidas):
        jogos.append(int(input(f'Quantos gols na partida {i+1} ? ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? (S/N) ')).upper()[0]
        if resp in 'SN':
            break
        print('Inválido. Digite apenas S ou N.')
    if resp == 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Inválido. Não existe jogador com o código {busca}.')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols.')
    print('=' * 50)
print(f' >>Fim do programa.<<')
