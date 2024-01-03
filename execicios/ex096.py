# Exercício 96 - Função que calcula área (020)

'''
# Descrição:

Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

# Resolução:

line_length = 70

def header(line_symbol = '-', text = 'header', text_color = '\033[1;32m'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)

def area(width, length):
    result = width * length

    print(f'A área do terreno de {width}m x {length}m = {result}m²')


header(text='Função que calcula área')

width = float(input('Digite a largura do terreno (metros): '))
length = float(input('Digite o comprimento do terreno (metros): '))

width = round(width, 1)
length = round(length, 1)

print('-' * line_length)

area(width, length)

print('-' * line_length)
