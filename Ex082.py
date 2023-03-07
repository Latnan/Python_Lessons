nums = []
evens = []
odds = []
while True:
    nums.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if r in 'Nn':
        break
for i in nums:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(f'Os números digitados foram: {nums}')
print(f'Os números pares são: {evens}')
print(f'E os números ímpares são: {odds}')
