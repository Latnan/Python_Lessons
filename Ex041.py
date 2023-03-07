from datetime import date
nascimento = int(input('Qual seu ano de nascimento? '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos, portanto sua categoria é: ')
if idade <= 9:
    print('Categoria Mirim.')
elif idade <= 14:
    print('Categoria Infantil.')
elif idade <= 19:
    print('Categoria Junior.')
elif idade <= 20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')
