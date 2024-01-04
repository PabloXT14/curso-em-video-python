# Exercício 100 - Função para sortear e somar (020)

'''
# Descrição:

Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''

# Resolução:

from random import randint
from time import sleep

line_length = 70
numbers = []

def header(text = '', text_color = '\033[1;35m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)


def raffle(numbers_list = []):
    amount_numbers = 5

    start_range = 0
    stop_range = 10

    print(f'* Números sorteados: ', end='')
    
    for i in range(0, amount_numbers):
        random_number = randint(start_range, stop_range)

        numbers_list.append(random_number)

        sleep(0.5)

        print(f'{'\033[1;33m'}{random_number}{'\033[m'}', end=' | ', flush=True) # flush=True -> Limpando buffer de memória
    print()


def even_sum(numbers_list = []):
    even_numbers = []

    for number in numbers_list:
        if number % 2 == 0:
            even_numbers.append(number)
    
    print('* Números pares: ', end='')

    for number in even_numbers:
        sleep(0.5)

        print(f'{'\033[1;33m'}{number}{'\033[m'}', end=' | ', flush=True)
    
    print()

    print(f'* Soma dos pares: {'\033[1;33m'}{sum(even_numbers)}{'\033[m'}')


header('Função para sortear e somar')

raffle(numbers)

print('-' * line_length)

even_sum(numbers)

print('-' * line_length)
