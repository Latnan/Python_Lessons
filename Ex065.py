resp = ''
cont = num = mean = sum = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    sum += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
print(f'Você digitou {cont} números e a média foi {sum / cont}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
print('Fim do programa.')
