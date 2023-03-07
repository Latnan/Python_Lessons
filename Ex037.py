num = int(input('Digite um número inteiro qualquer: '))
print('Escolha uma base numérica para converter: \n'
      '[1] - Binário\n'
      '[2] - Octal\n'
      '[3] - Hexadecimal\n')
escolha = int(input('Você escolheu: '))
if escolha == 1:
    print(f'{escolha} convertido para Binário é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{escolha} convertido para Octal é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{escolha} convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida.')
