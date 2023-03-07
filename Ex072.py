cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
        'vinte')
while True:
    num = int(input('Digite um número de 0 até 20: '))
    if num > 20:
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {cont[num]}.')

    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa.')
