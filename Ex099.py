from time import sleep


def maior(*num):
    cont = mai = 0
    print('*' * 40)
    print('Analisando os valores:')
    sleep(1)
    for v in num:
        print(f'{v} ', end='')
        if cont == 0:
            mai = v
        else:
            if v > mai:
                mai = v
        cont += 1
    sleep(1)
    print(f'\nForam informados {cont} valores.')
    print(f'E o maior valor foi {mai}')


maior(2, 3, 4, 5, 6, 7, 12, 99, 632)
