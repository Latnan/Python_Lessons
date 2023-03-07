n1 = int(input('Escolha um número para ver a progressão aritmética dele: '))
n2 = int(input('Escolha a razão da PA: '))
dec = n1 + (10 - 1) * n2
for c in range(n1, dec + n2, n2):
    print(f'{c}', end=", ")
print('Fim.')
