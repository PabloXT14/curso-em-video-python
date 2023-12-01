# Outras formas mais limpa de utilizar os códigos de cores no terminal 

print('-' * 70)

name = 'Pablo'

print(f'Olá, muito prazer em te conhecer {'\033[4;44m'}{name}{'\033[m'}')

print('-' * 70)

styles = {
    'reset': '\033[m', # or \033[0m
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reverse': '\033[7m'
}

colors = {
    'black': "\033[30m",
    'red': "\033[31m",
    'green': "\033[32m",
    'yellow': "\033[33m",
    'blue': "\033[34m",
    'magenta': "\033[35m",
    'cyan': "\033[36m",
    'gray': "\033[37m",
    'white': "\033[97m"
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

print(f'Olá, muito prazer em te conhecer {styles['reverse']}{colors['white']}{backgrounds['red']}{name}{styles['reset']}')