from random import randint
from time import sleep
from operator import itemgetter
dados = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6),
}
ranking = []
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'O {k} tirou {v} nos dados')
    sleep(1)
print('*' * 30)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('*' * 30)
print('Fim do jogo.')
