import random
cont = 0
while True:
    jogador = int(input('Escolha um número: '))
    computador = random.randint(0, 10)
    result = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você escolheu {jogador}. O computador escolheu {computador}. O total é de {result}.')
    if tipo == 'P':
        if result % 2 == 0:
            print('Você venceu da máquina.')
            cont += 1
        else:
            print('Você perdeu pro computador.')
            break
    elif tipo == 'I':
        if result % 2 != 0:
            print('Você venceu da máquina.')
            cont += 1
        else:
            print('Você perdeu pro computador.')
            break
    print('Mais uma!')
print(f'Fim de jogo. Você venceu {cont} vezes seguidas.')