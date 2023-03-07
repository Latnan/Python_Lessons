sum = 0
count = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 != 0:
        n = 0
    else:
        count += 1
        sum += n
print(f'A soma dos {count} números pares é {sum}.')
