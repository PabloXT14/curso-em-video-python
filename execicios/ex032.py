# Exercício 32 - Ano Bissexto (Aula 010)

'''
# Descrição:

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

* Dica: Um ano bissexto é aquele que é divisível por 4, mas não por 100, a menos que seja divisível por 400

'''

# Resolução:

from datetime import datetime

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

print('# Ano Bissexto')

print('-' * 80)

year = int(input("Digite ano que você que analisar (coloque '0' para analisar o ano atual): "))

print('-' * 80)

if (year == 0):
    year = datetime.now().year

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if (is_leap_year):
    print(f'* O ano {styles["bold"] + colors["magenta"]}{year}{styles["reset"]} é bissexto.')
else:
    print(f'* O ano {styles["bold"] + colors["yellow"]}{year}{styles["reset"]} não é bissexto.')
