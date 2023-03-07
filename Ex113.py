def leia_int(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leia_float(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


num = leia_int('Digite um número inteiro: ')
num2 = leia_float('Digite um número real: ')
print(f'O número inteiro digitado foi {num} e o real foi {num2}')
