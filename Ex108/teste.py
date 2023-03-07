import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é R${moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é R${moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Diminuindo 10%, temos R${moeda.moeda(moeda.diminuir(preço, 10))}')