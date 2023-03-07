n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}')
    elif opção == 2:
        print(f'A multiplicação de {n1} por {n2} é igual a {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        else:
            print(f'{n2} é maior que {n1}.')
    elif opção == 4:
        print('Escolha novos números:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('***' * 10)
print('Você saiu do programa. Até logo.')
