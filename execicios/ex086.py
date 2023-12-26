# Exercício 86 - Matriz em Python (018)

'''
# Descrição:

Crie um programa que crie uma matriz de 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
'''

# Resolução:

line_length = 70

print('# Matriz em Python')

print('-' * line_length)

matriz = list()
lines_amount = 3
columns_amount = 3

for line in range(0, lines_amount):
    matriz.append([])

    for column in range(0, columns_amount):
        number = int(input(f'Digite um valor para a posição [{line}, {column}]: '))
    
        matriz[line].append(number)

print('-' * line_length)

for line in matriz:
    for column in line:
        number = column

        print(f'[{'\033[1;33m'}{number:^5}{'\033[m'}]', end='')

    print()
