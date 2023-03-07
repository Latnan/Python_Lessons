tot18 = homem = wu20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        wu20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'> Total de pessoas com mais de 18 anos: {tot18}')
print(f'> Total de homens: {homem}')
print(f'> E o total de mulheres com menos de 20 anos é de: {wu20}')
print('Fim do programa.')
