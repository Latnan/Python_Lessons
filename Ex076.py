lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.90,
         'Canetas', 22.30, 'Livro', 34.90)
print('*' * 39)
print(f'{"Lista de Preços:"}')
print('*' * 39)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>7.2f}')
print('*' * 39)
