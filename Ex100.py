from random import randint
from time import sleep

numeros = []


def sorteia():
    print('Sorteando valores...')
    sleep(1)
    for i in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
    print(f'Os valores sorteados foram: \n{numeros}')


def somapar():
    sum = 0
    sleep(1)
    for n in numeros:
        if n % 2 == 0:
            sum += n
    print(f'A soma entre os valores pares sorteados é {sum}')


sorteia()
somapar()
