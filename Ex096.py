def área(length, width):
    area = (length * width)
    print(f'A área de um terreno com {length:.1f}x{width:.1f} é de {area:.2f}m².')


print(f'{"Calculadora de área"}')
print('-' * 40)
comp = float(input('Qual o comprimento do terreno? (em metros) '))
larg = float(input('Qual a largura do terreno? (em metros) '))

área(comp, larg)
