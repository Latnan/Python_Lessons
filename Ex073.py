tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR',
          'Atletico Mineiro', 'Botafogo', 'Sao Paulo', 'America-MG', 'Fortaleza', 'Santos', 'Goias', 'Bragantino',
          'Coritiba', 'Ceara', 'Atletico Goianiense', 'Cuiaba', 'Avai', 'Juventude')
print('*' * 30)
print(f'Os 5 primeiros times são: {tabela[0:5]}')
print('*' * 30)
print(f'Os 4 últimos times são: {tabela[-4:]}')
print('*' * 30)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('*' * 30)
print(f'O Flamengo está na posição #{tabela.index("Flamengo")+1}.')
print('*' * 30)
print('Fim do programa.')
