somaid = 0
mediaid = 0
maioridhomem = 0
maisvelho = ''
mulher20 = 0
for ppl in range(1, 5):
    print(f'*** {ppl}ª PESSOA ***')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    somaid += idade
    if ppl == 1 and sexo == 'M':
        maioridhomem = idade
        maisvelho = nome
    if sexo and idade > maioridhomem:
        maioridhomem = idade
        nomevelho = nome
    if sexo and idade < 20:
        mulher20 += 1
mediaid = somaid / 4
print(f'A média de idade do grupo é de {mediaid} anos.')
print(f'O homem mais velho tem {maioridhomem} e se chama {maisvelho}.')
print(f'Temos {mulher20} mulher com menos de 20 anos.')