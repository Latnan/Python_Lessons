while True:
    num = int(input('Escolha um número para ver sua tabuada: '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} * {i} = {num*i}')
print('Fim do programa.')
