# Exercício 30 - Par ou ímpar (Aula 010)

'''
# Descrição:

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
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

print('# Par ou Ímpar')

print('-' * 70)

number = int(input('Digite um número inteiro: '))

print('-' * 70)

print(f'* Resultado: {colors["cyan"]}{'PAR' if (number % 2 == 0) else 'ÍMPAR'}{styles["reset"]}')
