from random import randint
from time import sleep
computador = randint(0, 5) #Número escolhido pelo computador
print('-*-' * 20)
print('Pensei em um número de 0 a 5, tente sua sorte o adivinhando...')
print('-*-' * 20)
jogador = int(input('Qual número eu pensei? ')) #Tentativa do jogador
print('Hmmm... será que você conseguiu?')
sleep(5)
if jogador == computador:
    print('Parabéns! Você deu sorte!')
else:
    print(f'Humanos são tão inferiores, se fodeo, {computador} era o número que eu pensei e você chutou {jogador}')
