matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um número para [{line}, {column}]: '))
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print()
