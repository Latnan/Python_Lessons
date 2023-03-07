def escreva(txt):
    esp = len(txt) + 6
    print('*' * esp)
    print(f'   {txt}')
    print('*' * esp)


mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
