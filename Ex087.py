matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = col = 0
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um número para [{line}, {column}]: '))
print('*' * 25)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
        if matrix[line][column] % 2 == 0:
            pares += matrix[line][column]
    print()
print('*' * 25)
print(f'A soma dos valores pares é {pares}.')
for line in range(0, 3):
    col += matrix[line][2]
print(f'A soma dos valores da terceira coluna é {col}.')
for column in range(0, 3):
    if column == 0:
        maior = matrix[1][column]
    elif matrix[1][column] > maior:
        maior = matrix[1][column]
print(f' O maior valor da segunda linha é {maior}.')
