distancia = float(input('Qual a distância da viagem em Kms? '))
if distancia <= 200:
    print(f'O custo da sua viagem é de R${distancia * 0.5:.2f}')
else:
    print(f'O custo da sua viagem é de R${distancia * 0.45:.2f}')
