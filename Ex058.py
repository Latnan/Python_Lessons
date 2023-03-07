from random import randint
computador = randint(0, 10)
print('Pensei em um número de 0 a 10, tente sua sorte o adivinhando...')
acertou = False
contador = 0
while not acertou:
    jogador = int(input('Qual número eu pensei? '))
    contador += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print(f'Acertou! Você tentou {contador} vezes até conseguir.')
