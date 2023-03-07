from PythonExercícios.Ex112.utilidades import moeda
from PythonExercícios.Ex112.utilidades import dado

preço = dado.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preço, 30, 20)
