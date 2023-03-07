num = int(input('Quantos números você deseja mostrar? '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='')
cont = 3
while cont <= num:
    n3 = n1 + n2
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' -> Fim da sequência de Fibonacci.')
