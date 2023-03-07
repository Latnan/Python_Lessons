from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - nascimento
if (date.today().year - nascimento) < 18:
    print(f'Você ainda vai se alistar ao serviço militar, faltam {18 - idade} ano(s) para chegar a hora.')
elif (date.today().year - nascimento) == 18:
    print('Já está na hora de se alistar ao serviço militar (boa sorte e faça uma tattoo).')
else:
    print(f'Parabéns, seu velho. Já passou {idade - 18} ano(s) desde seu alistamento.')
