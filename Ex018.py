from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo desejado: '))
seno = sin(radians(angulo))
print(f'O ângulo {angulo} tem o seno de {seno:.2f}.')
cosseno = cos(radians(angulo))
print(f'O ângulo {angulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')
