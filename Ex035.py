a = float(input('Digite um comprimento de reta: '))
b = float(input('Digite outro comprimento de reta: '))
c = float(input('Digite mais um comprimento de reta: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível fazer um triângulo com essas retas.')
else:
    print('Não é possível fazer um triângulo com essas retas.')
