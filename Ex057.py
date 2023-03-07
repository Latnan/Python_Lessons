sexo = str(input('Com qual sexo você se identifica? [M/F/Nb]')).strip().upper()[0]
while sexo not in 'MmFfNb':
    sexo = str(input('Resposta inválida. Por favor, informe seu sexo [M/F/Nb]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')
