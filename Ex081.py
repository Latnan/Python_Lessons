nums = []
while True:
    nums.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Você digitou {len(nums)} números.')
nums.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são {nums}')
if 5 in nums:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não está presente na lista.')
