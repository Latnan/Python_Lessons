from datetime import date
ano = int(input('Escolha um ano para analisar. Digite 0 para o ano atual.'))
if ano == 0:
    ano = date.today().year
elif ano % 400 == 0:
    print('É ano bissexto!')
elif ano % 4 == 0 and ano % 100 != 0:
    print('É ano bissexto!')
else:
    print('Não é ano bissexto.')
