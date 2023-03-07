import random
A1 = input('Primeiro aluno: ')
A2 = input('Segundo aluno: ')
A3 = input('Terceiro aluno: ')
A4 = input('Quarto aluno: ')
lista = [A1, A2, A3, A4]
random.shuffle(lista)
print(f'A ordem dos alunos escolhidos é:\n {lista}')