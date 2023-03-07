cont = num = sum = 0
while num != 999:
    num = int(input('Digite um número [digite 999 para parar]: '))
    print(num)
    if num == 999:
        cont += 0
        sum += 0
    else:
        cont += 1
        sum += num
print(f'Você digitou {cont} números.')
print(f'A soma dos números digitados foi {sum}')
