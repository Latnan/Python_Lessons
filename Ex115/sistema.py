from PythonExercícios.Ex115.Arquivo import *

arq = 'exerciciopython.txt'

if not arq_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Listar conteúdo do arquivo
        ler_arquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa.
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema. Até logo!')
        break
    else:
        print('\033[31mERRO: por favor, digite uma opção válida.\033[m')
