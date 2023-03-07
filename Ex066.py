cont = sum = 0
while True:
    num = int(input('Digite um número: (Se digitar 999 o programa encerrará.) '))
    if num == 999:
        break
    cont += 1
    sum += num
print(f'Foram digitados {cont} números e a soma desses números é {sum}.')
print('Fim do programa.')
