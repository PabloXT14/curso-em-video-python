# Exercício 98 - Função de Contador (020)

'''
# Descrição:

Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada

# Atenção:

Se o seu código está parando de executar quando você usa a função sleep dentro de um loop for dentro de uma função, pode ser que o programa esteja esperando que o loop termine antes de continuar a execução. Para resolver isso, você pode tentar usar a função flush para limpar o buffer de saída antes de chamar a função sleep
'''

# Resolução:

from time import sleep
from sys import __stdout__
from os import get_terminal_size

line_length = get_terminal_size().columns

def header(text = '', text_color = '\033[1;33m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)

def counter(start, stop, step = 1):
    if step == 0:
        step = 1

    print(f'Contagem de {start} até {stop}, de {step} em {step} = ', end='')
    
    if (start > stop) and step > 0:
        step *= -1

    if step > 0:
        stop += 1
    else:
        stop -= 1

    for i in range(start, stop, step):
        __stdout__.flush()
        sleep(0.5)
        print(f'{'\033[1;33m'}{i}{'\033[m'}', end=' | ')
    print()

header('Função de Contador')

counter(1, 10)

print('-' * line_length)

counter(10, 0, 2)

print('-' * line_length)

print('Agora é sua vez de personalizar a contagem!')

start = int(input('Início: '))
stop = int(input('Fim: '))
step = int(input('Passo: '))

print('-' * line_length)

counter(start, stop, step)

print('-' * line_length)
