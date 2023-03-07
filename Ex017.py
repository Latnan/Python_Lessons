import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa entre {co} e {ca} deve medir {hi:.2f}')


#Resolução sem import math
#co = float(input('Comprimento do cateto oposto: '))
#a = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa entre {co} e {ca} deve medir {hi:.3}')
