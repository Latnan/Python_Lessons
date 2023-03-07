def leiaint(a):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaint('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')
