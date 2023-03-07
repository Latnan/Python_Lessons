n1 = int(input('Escolha um número: '))
rz = int(input('Escolha a razão da PA: '))
cont = 1
total = 0
add = 10
while add != 0:
    total = total + add
    while cont <= total:
        print(f'{n1} -> ', end='')
        n1 += rz
        cont += 1
    print('Interrompido.')
    add = int(input('Quantos números a mais você quer mostrar? '))
print(f'Fim da PA.')
