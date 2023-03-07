nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo fica {nome.upper()}')
print(f'Seu nome em minúsculas fica {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')

