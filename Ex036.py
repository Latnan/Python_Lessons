casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
print(' ')
vpm = (casa / anos) / 12
porcento = (vpm*100) / salario
print('***'*8)
print(' ')
print('Para o empréstimo ser aceito, o valor mensal não deve exceder 30% do salário.')
print(' ')
print(f'O valor da prestação será de R${vpm:.2f}\n'
      f'Que corresponde a {porcento:.2f}% do salário.')
if vpm >= salario*30/100:
    print('Portanto, o empréstimo foi negado.')
else:
    print('Portanto, o empréstimo foi concedido.')
print(' ')
print('***'*8)
