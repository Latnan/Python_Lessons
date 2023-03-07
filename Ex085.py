nums = [[], []]
valor = 0
for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print(f'Os números escolhidos foram: {nums}')
print(f'Os números pares foram: {nums[0]} e os ímpares foram: {nums[1]}')
