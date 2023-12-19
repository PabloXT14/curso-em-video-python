# Exercício 74 - Maior e Menor Valores em Tupla (016)

'''
# Descrição:

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.
'''

# Resolução:
from random import randint

print('# Maior e Menor Valores em Tupla')

line_length = 70

print('-' * line_length)

start_range = 0
stop_range = 10

# 1ª Solução
'''
number1 = randint(start_range, stop_range)
number2 = randint(start_range, stop_range)
number3 = randint(start_range, stop_range)
number4 = randint(start_range, stop_range)
number5 = randint(start_range, stop_range)

numbers = (number1, number2, number3, number4, number5)

print(f'* Valores gerados: ', end='')

for i, number in enumerate(numbers):
    print(f'{'\033[1;33m'}{number}{'\033[m'}', end='')
    print(' - ' if i != len(numbers) - 1 else '', end='')

print()

print(f'* Maior valor: {'\033[1;33m'}{max(numbers)}{'\033[m'}')
print(f'* Menor valor: {'\033[1;33m'}{min(numbers)}{'\033[m'}')
'''

# 2ª Solução

random_numbers = tuple(randint(start_range, stop_range) for _ in range(5))

print('* Valores gerados: ', end='')

for i, number in enumerate(random_numbers):
    print(f'{'\033[1;33m'}{number}{'\033[m'}', end='')
    print(' - ' if i != len(random_numbers) - 1 else '', end='')

print()

lower_value = min(random_numbers)
higher_value = max(random_numbers)

print(f'* Menor valor: {'\033[1;33m'}{lower_value}{'\033[m'}')
print(f'* Maior valor: {'\033[1;33m'}{higher_value}{'\033[m'}')
