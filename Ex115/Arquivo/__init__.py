from PythonExercícios.Ex115.Interface import *


def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileNotFoundError:
        print('Houve um erro ao tentar criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split('; ')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
