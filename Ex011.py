wid = float(input('Insira a largura da parede em metros: '))
hei = float(input('Insira a altura da parede em metros: '))
area = wid * hei
litros = area / 2
print(f'Sua parede tem a dimensão de {wid}x{hei} e sua área é de {area}m².')
print(f'Você precisará de cerca de {litros:.1f}L de tinta para pintar sua parede.')
