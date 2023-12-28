# Exercício 87 - Mais sobre Matriz em Python (018)

'''
# Descrição:

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha
'''

# Resolução:

line_length = 70

print('# Mais sobre Matriz em Python')

print('-' * line_length)

matriz = list()
lines_amount = 3
columns_amount = 3

even_sum = 0
sum_column_3 = 0
higher_second_line = 0

for line in range(0, lines_amount):
    matriz.append([])

    for column in range(0, columns_amount):
        number = int(input(f'Digite o valor para a posição [{line}, {column}]: '))

        matriz[line].append(number)
    
print('-' * line_length)

for line_index, line_value in enumerate(matriz):
    for column_index, column_value in enumerate(line_value):
        number = column_value

        print(f'[{'\033[1;33m'}{number:^5}{'\033[m'}]', end='')

        if number % 2 == 0:
            even_sum += number

        if column_index == 2:
            sum_column_3 += number
        
        if line_index == 1 and higher_second_line == 0:
            higher_second_line = number
        elif line_index == 1 and number > higher_second_line:
            higher_second_line = number

    print()

print('-' * line_length)

print(f'* Soma dos valores pares: {'\033[1;33m'}{even_sum}{'\033[m'}')
print(f'* Soma dos valores da 3ª coluna: {'\033[1;33m'}{sum_column_3}{'\033[m'}')
print(f'* Maior valor da segunda linha: {'\033[1;33m'}{higher_second_line}{'\033[m'}')

print('-' * line_length)
