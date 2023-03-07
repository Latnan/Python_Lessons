tot = mil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Qual o nome do produto? ')).capitalize()
    preço = float(input('Quanto custa o produto? R$ '))
    tot += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa.')
print(f'> O total da compra foi de R${tot:.2f}')
print(f'> {mil} produto(s) custa(ram) mais de R$1000.')
print(f'> O produto mais barato foi {barato}, que custou R${menor:.2f}.')
