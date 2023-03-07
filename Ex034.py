salario = float(input('Qual o salário do funcionário? '))
if salario > 1250:
    print(f'O salário do funcionário receberá um aumento de 10% e passará para R${salario + (salario * 10 / 100):.2f}')
else:
    print(f'O salário do funcionário receberá um aumento de 15% e passará para R${salario + (salario * 15 / 100):.2f}')
