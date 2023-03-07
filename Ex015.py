kms = float(input('Insira a quilometragem percorrida: '))
dias = int(input('Insira a quantidade de dias de uso: '))
custo_dias = dias*60
custo_kms = kms*0.15
custo_total = custo_dias + custo_kms
print(f'O custo total da viagem é de R${custo_total:.2f}, sendo:\n'
      f' R${custo_dias:.2f} o preço das diárias e\n'
      f' R${custo_kms:.2f} o custo por Kms percorridos.')
