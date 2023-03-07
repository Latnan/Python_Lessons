m1 = float(input('Insira o comprimento do segmento de reta #1: '))
m2 = float(input('Insira o comprimento do segmento de reta #2: '))
m3 = float(input('Insira o comprimento do segmento de reta #3: '))
tipo = ''
if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    if m1 == m2 and m1 == m3:
        tipo += 'equilátero'
    elif m1 == m2 and m1 != m3 or m1 == m3 and m1 != m2:
        tipo += 'isósceles'
    else:
        tipo += 'escaleno'
    print(f'É possível fazer um triângulo do tipo {tipo} com essas retas.')
else:
    print('Não é possível fazer um triângulo com essas retas.')
