# Exercício 113 - Funções aprofundadas em Python  (023)

'''
# Descrição:

Reescreva a função 'leia_int()' que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função 'leia_float()' com a mesma funcionalidade. 
'''

# Resolução:

line_length = 70

def header(text = '', text_color = '\033[1;32m', line_length = 70, line_symbol = '-'):
    line = line_symbol * line_length
    header_content = f'{text_color}{text.upper():^{line_length}}{'\033[m'}'

    print(line)
    print(header_content)
    print(line)


def read_int(message = ''):
    while True:
        try:
            number = int(input(message))
        except (ValueError, TypeError):
            print('-' * line_length)
            print(f'{'\033[1;31m'}Erro: por favor, digite um número inteiro válido.{'\033[m'}')
            print('-' * line_length)
        except KeyboardInterrupt:
            print()
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada de dados interrompida pelo usuário.{'\033[m'}')
            print('-' * line_length)
            return
        else:
            return number


def read_float(message = ''):
    while True:
        try:
            number = float(input(message))
        except (ValueError, TypeError):
            print('-' * line_length)
            print(f'{'\033[1;31m'}Erro: por favor, digite um número real válido.{'\033[m'}')
            print('-' * line_length)
        except KeyboardInterrupt:
            print()
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada de dados interrompida pelo usuário.{'\033[m'}')
            print('-' * line_length)
            return
        else:
            return number

header('Validando Entrada de Dados 2')

int_number = read_int('Digite um número inteiro: ')
float_number = read_float('Digite um número real: ')

print('-' * line_length)

print(f'* Nº inteiro digitado: {'\033[1;33m'}{int_number}{'\033[m'}')
print(f'* Nº real digitado: {'\033[1;33m'}{float_number}{'\033[m'}')

print('-' * line_length)
