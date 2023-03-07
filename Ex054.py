from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for ppl in range(1, 8):
    nasc = int(input(f'Em que ano a {ppl}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo são {totmaior} maiores de idade.')
print(f'Ao todo são {totmenor} menores de idade.')
