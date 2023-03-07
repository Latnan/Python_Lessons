vel = float(input('A qual velocidade em km/h do carro? '))
if vel > 80:
    print(f'O veículo foi multado por excesso de velocidade. A multa é de R${(vel - 80) * 7:.2f}')
else:
    print(f'Tudo certo, patrão, tenha um bom dia!')