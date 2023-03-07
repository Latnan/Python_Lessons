exp = str(input('Digite uma expressão matemática: '))
paren = []
for c in exp:
    if c == '(':
        paren.append('(')
    elif c == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
if len(paren) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
