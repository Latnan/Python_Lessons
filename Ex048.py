sum = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        sum += c
print(f'A soma de todos os {count} números é {sum}.')
