num = int(input('Digite um número: '))
count = num
fact = 1
print(f'Calculando o fatorial {num}! = ', end='')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    fact *= count
    count -= 1
print(f'{fact}')