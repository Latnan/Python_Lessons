valor = float(input('Qual o preço do produto? R$'))
pagamento = int(input('Qual a forma de pagamento?\n'
                      'Digite:\n'
                      '(1) - À vista dinheiro/cheque\n'
                      '(2) - À vista no cartão\n'
                      '(3) - Parcelado em até 2x no cartão\n'
                      '(4) - Parcelado em 3x ou mais no cartão\n'
                      'Código: '))

if pagamento == 1:
    print(f'O valor a ser pago pelo produto é de R${valor - (valor * 10/100):.2f} (com desconto já aplicado de 10%).')
elif pagamento == 2:
    print(f'O valor a ser pago pelo produto é de R${valor - (valor * 5/100):.2f} (com desconto já aplicado de 5%).')
elif pagamento == 3:
    print(f'O valor a ser pago pelo produto é de R${valor:.2f} (sem descontos ou juros)\n'
          f'Cada parcela custará R${valor / 2:.2f}.')
elif pagamento == 4:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    print(f'O valor a ser pago pelo produto é de R${valor + (valor * 20/100):.2f} (com 20% de juros já aplicados)\n'
          f'Cada parcela custará R${(valor + (valor * 20/100)) / parcela:.2f}.')
else:
    print('Código inválido.')
