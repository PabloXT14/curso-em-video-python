# Exercício 35 - Analisando Triângulo v1.0 (Aula 010)

'''
# Descrição:

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

* Dica: em qualquer triângulo, a soma das medidas de dois lados é sempre maior que a medida do terceiro.
'''

# Resolução:

styles = {
    'reset': '\033[m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reverse': '\033[7m'
}

colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'gray': '\033[37m',
    'white': '\033[97m'
}

backgrounds = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'magenta': '\033[45m',
    'cyan': '\033[46m',
    'gray': '\033[47m',
    'white': '\033[107m'
}

print('# Analisando Triângulo v1.0')

print('-' * 70)

side_1 = float(input('Digite o valor do 1º lado do triângulo: '))
side_2 = float(input('Digite o valor do 2º lado do triângulo: '))
side_3 = float(input('Digite o valor do 3º lado do triângulo: '))

print('-' * 70)

is_triangle = False

if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_3 + side_2 > side_1):
    is_triangle = True

print(f'* Estes valores formam um triângulo: {styles["bold"]}{f'{colors["green"]}Sim' if is_triangle else f'{colors["red"]}Não'}{styles["reset"]}')