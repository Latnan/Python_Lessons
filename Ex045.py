from random import randint

item = ('Pedra', 'Papel', 'Tesoura')
print('**' * 15)
jogador = int(input('(0) - Pedra\n'
                    '(1) - Papel\n'
                    '(2) - Tesoura\n'
                    'Escolha um: '))
jogada = item[jogador]
computador = randint(0, 2)
print(f'Sua jogada foi {jogada}')
print(f'O computador jogou {item[computador]}')
if jogador == 0:
    if computador == 0:
        print('Empate!')
    elif computador == 1:
        print('Derrota!')
    elif computador == 2:
        print('Vitória!')
    else:
        print('INVÁLIDO')
elif jogador == 1:
    if computador == 0:
        print('Vitória!')
    elif computador == 1:
        print('Empate!')
    elif computador == 2:
        print('Derrota!')
    else:
        print('INVÁLIDO')
elif jogador == 2:
    if computador == 0:
        print('Derrota!')
    elif computador == 1:
        print('Vitória!')
    elif computador == 2:
        print('Empate!')
    else:
        print('INVÁLIDO')
else:
    print('INVÁLIDO')
print('**' * 15)
