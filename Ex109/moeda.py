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
