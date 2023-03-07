nums = []
while True:
    n = int(input('Digite um número: '))
    if n not in nums:
        nums.append(n)
        print(f'{n} adicionado com sucesso à lista.')
    else:
        print('O número já havia sido adicionado.')
    r = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Você digitou os números {nums}.')
