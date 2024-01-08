# Exercício 106 - Interactive Helping System in Python  (021)

'''
# Descrição:

Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
'''

# Resolução:
from time import sleep
from os import get_terminal_size

line_length = get_terminal_size().columns

def header(text = '', header_color = '\033[1;37;42m', line_symbol = '-'):
    print(header_color)

    print(' ' * line_length)
    print(f'{text.upper():^{line_length}}')
    print(' ' * line_length)

    print('\033[m')

header('Interactive Helping System in Python')

while True:
    data = input('Digite a função ou biblioteca (FIM para sair): ').strip()

    if data.upper() == 'FIM':
        header('Obrigado, volte sempre!')
        break

    header(f'Detalhes {data}...')

    sleep(0.5)

    print('\033[1;97;107m')
    help(data)
    print('\033[m',)
