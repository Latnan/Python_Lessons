numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
num = str(numero)
print(f'Numero escolhido: {num}\n'
      f' Unidade: {u}\n'
      f' Dezena: {d}\n'
      f' Centena: {c}\n'
      f' Milhar: {m}\n')
