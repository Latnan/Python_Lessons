frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = '-'.join(palavras)
print(f'Você digitou a frase/palavra {junto}')
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo.')
