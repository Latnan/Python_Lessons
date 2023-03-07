lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? (s/n)')).strip().upper()[0]
    if resp in 'Nn':
        break
print('*' * 25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('*' * 25)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('*' * 25)
    option = int(input('Mostrar notas de qual estudante? (999 interrompe): '))
    if option == 999:
        print('Finalizado.')
        break
    if option <= len(lista) - 1:
        print(f'Notas de {lista[option][0]} são {lista[option][1]}')
print('*** Até a próxima! ***')
