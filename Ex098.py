from time import sleep


def contador(ini, fim, p):
    print('*' * 30)
    if p == 0:
        p = 1
        print('Não existe passo 0, escolhemos 1 no lugar.')
        for i in range(ini, fim+1, p):
            print(f'{i} ', end='')
            sleep(0.5)
    elif ini < fim:
        print(f'Contagem de {ini} até {fim} de {p} em {p}')
        for i in range(ini, fim+1, p):
            print(f'{i} ', end='')
            sleep(0.5)
    else:
        print(f'Contagem de {ini} até {fim} de {p} em {p}')
        for i in range(ini, fim, p*-1):
            print(f'{i} ', end='')
            sleep(0.5)
    print('Fim!')


def linha():
    print('*' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Escolha sua própria contagem:')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
s = int(input('Passo: '))
contador(n1, n2, s)
