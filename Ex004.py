p = input('Digite qualquer coisa: ')
print('O tipo primitivo dessa coisa é ', type(p))
print('Só há espaços? ', p.isspace())
print('É um número? ', p.isnumeric())
print('É alfabético? ', p.isalpha())
print('É alfanumérico? ', p.isalnum())
print('Está em maiúsculas? ', p.isupper())
print('Está em minúsculas? ', p.islower())
print('Está em caps? ', p.istitle())