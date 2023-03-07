def aumentar(preço=0, taxa=0, formato=False):
    calc = preço + (preço * taxa / 100)
    return calc if formato is False else moeda(calc)


def diminuir(preço=0, taxa=0, formato=False):
    calc = preço - (preço * taxa / 100)
    return calc if formato is False else moeda(calc)


def dobro(preço=0, formato=False):
    calc = preço * 2
    return calc if not formato else moeda(calc)


def metade(preço=0, formato=False):
    calc = preço / 2
    return calc if not formato else moeda(calc)


def moeda(preço=0, valor='R$'):
    return f'{valor}{preço:.2f}'.replace('.', ',').format(float(preço))


def resumo(preço=0, taxaaumento=10, taxareducao=10):
    print('-' * 30)
    print(f'Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaaumento}% de aumento: \t{aumentar(preço, taxaaumento, True)}')
    print(f'{taxareducao}% de redução: \t{diminuir(preço, taxareducao, True)}')
    print('-' * 30)