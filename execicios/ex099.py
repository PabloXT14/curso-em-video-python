# Exercício 99 - Função que descobre o maior (020)

'''
# Descrição:

Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros de valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

# Resolução:

from time import sleep
from sys import __stdout__

line_length = 70

def header(text = '', text_color = '\033[1;36m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)


def higher(*numbers):
    higher_number = max(numbers)
    print('* Valores: ', end='')

    for number in numbers:
        __stdout__.flush() # Limpar buffer de memória
        sleep(0.5)
        print(f'{'\033[1;33m'}{number}{'\033[m'}', end=' | ')

    print() # Quebra de linha

    print(f'* Maior valor: {'\033[1;33m'}{higher_number}{'\033[m'}')
    
    sleep(0.5)


header('Função que descobre o maior')

higher(1, 2, 4, 5, 6, 7, 8, 9)

print('-' * line_length)

higher(10, 20, 30, 40, 50)

print('-' * line_length)

higher(-1, 3, 5, 8, 10)

print('-' * line_length)

higher(0)

print('-' * line_length)
