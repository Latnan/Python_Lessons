nome_completo = str(input('Digite seu nome completo: ')).strip()
nome = nome_completo.split()
print(f'Olá {nome_completo}!\n'
      f'Seu primeiro nome é {nome[0]},\n'
      f'Seu último nome é {nome[-1]}.')
