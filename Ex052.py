num = int(input('Digite um número inteiro: '))
divisor = 0
for c in range(1, num + 1):
    if num % c == 0:
        divisor += 1
if divisor == 2:
    print(f'É primo pois só divide por {divisor} números, sendo 1 e {num}.')
else:
    print(f'Não é primo pois é possível dividir por mais {divisor - 2} números além de 1 e {num}.')
