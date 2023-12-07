# Explicando a função range()
'''
range(start, stop, step) gera uma sequência de números começando em start (início), indo até stop-1 (fim-1), com um step(passo) específico.

Se você fornecer apenas um argumento, ele será considerado como o fim, e o início será assumido como 0, e o passo será assumido como 1
'''

for i in range(6):
    print(f'Item: {i}')

print('-' * 70)

for i in range(0, 6):
    print(f'Aluno: {i}')

print('-' * 70)

for i in range(6, 0, -1): # o -1 indica que o indice (i) deve ir decrementando de 6 a 0 (com 0 não incluso)
    print(f'Pessoa: {i}')

print('-' * 70)

for i in range(0, 7, 2): # vai de 0 a 7 (com 7 não incluso) pulando de 2 em dois
    print(f'Carro: {i}')
