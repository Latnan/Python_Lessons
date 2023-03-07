from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasce = int(input(f'Ano de nascimento de {trabalhador["nome"]}: '))
trabalhador['idade'] = datetime.now().year - nasce
trabalhador['ctps'] = int(input(f'Carteira de trabalho (0 se não tiver): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input(f'Ano de contratação: '))
    trabalhador['salário'] = int(input(f'Salário: '))
    trabalhador['aposentar'] = (trabalhador['contratação'] + 35) - datetime.now().year
print('*' * 30)
for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}')
