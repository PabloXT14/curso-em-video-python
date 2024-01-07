# Exercício 104 - Validando entrada de dados em Python (021)

'''
# Descrição:

Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
n = lei_int('Digite um número: ')
'''

# Resolução:

line_length = 70

def header(text = '', text_color = '\033[1;32m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)

def read_int(message):

    while True:
        response = input(message)

        if response.isdigit():
            break
        else:
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada inválida! Digite um número inteiro.{'\033[m'}')
            print('-' * line_length)
    
    return response

header('Validando entrada de dados em Python')

number = read_int('Digite um número: ')

print('-' * line_length)

print(f'* Você digitou o número: {'\033[1;33m'}{number}{'\033[m'}')

print('-' * line_length)
