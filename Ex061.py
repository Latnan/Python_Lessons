n1 = int(input('Escolha um número: '))
rz = int(input('Escolha a razão da PA: '))
cont = 1
while cont <= 10:
    print(f'{n1}->', end='')
    n1 += rz
    cont += 1
print('Fim dos 10 primeiros valores da PA.')
