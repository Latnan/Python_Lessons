nota1 = float(input('Qual a sua nota da primeira prova? '))
nota2 = float(input('Qual a sua nota da segunda prova? '))
media = (nota1 + nota2)/2
print(f'Sua média é de {media:.1f}.')
if media < 5.0:
    print('Reprovado, estude mais ano que vem. Otário.')
elif media < 6.9:
    print('Você está em recuperação, boa sorte.')
else:
    print('Parabéns mlk! Tá aprovado!')
