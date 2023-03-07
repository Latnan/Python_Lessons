def notas(*nota, situ=False):
    """
    -> Função para analisar notas e situações de uma turma.
    :param nota: notas dos alunos (aceita mais de uma).
    :param situ: valor opcional. Caso "True", demonstra a situação da turma num geral.
    :return: dicionário com informações sobre as notas e(ou) a situação da turma.
    """
    turma = dict()
    turma['contagem'] = len(nota)
    turma['maior'] = max(nota)
    turma['menor'] = min(nota)
    turma['media'] = sum(nota)/len(nota)
    if situ:
        if turma['media'] >= 7:
            turma['situação'] = 'Boa'
        elif turma['media'] >= 5:
            turma['situação'] = 'Razoável'
        else:
            turma['situação'] = 'Ruim'
    return turma


resp = notas()
print(resp)
help(notas)
