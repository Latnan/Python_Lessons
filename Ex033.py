num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha outro número: '))
num3 = int(input('Escolha mais um número: '))
if num1 > num2 > num3:
    print(f'O maior número dentre os escolhidos foi {num1} e o menor foi {num3}.')
elif num1 > num3 > num2:
    print(f'O maior número escolhido foi {num1} e o menor foi {num2}.')
elif num2 > num1 > num3:
    print(f'O maior número escolhido foi {num2} e o menor foi {num3}')
elif num2 > num3 > num1:
    print(f'O maior número escolhido foi {num2} e o menor foi {num1}')
elif num3 > num2 > num1:
    print(f'O maior número escolhido foi {num3} e o menor foi {num1}')
else:
    print(f'O maior número escolhido foi {num3} e o menos foi {num2}')
