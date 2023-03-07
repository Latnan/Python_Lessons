from random import randint
lista = []
jogos = []
plays = int((input('Quantos jogos você quer sortear? ')))
tot = 1
while tot <= plays:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
'''print('*' * 3, f'Seus números sorteados são: {jogos}.', '*' * 3)'''
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
