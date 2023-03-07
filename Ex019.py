import random
Aluno_1 = input('Primeiro aluno: ')
Aluno_2 = input('Segundo Aluno: ')
Aluno_3 = input('Terceiro Aluno: ')
Aluno_4 = input('Quarto Aluno: ')
lista = [Aluno_1, Aluno_2, Aluno_3, Aluno_4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')
