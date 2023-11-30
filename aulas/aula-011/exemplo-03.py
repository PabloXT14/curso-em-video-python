# Outras formas mais limpa de utilizar os códigos de cores no terminal 

print('-' * 70)

name = 'Pablo'

print(f'Olá, muito prazer em te conhecer {'\033[4;44m'}{name}{'\033[m'}')

print('-' * 70)

colors = {
    'reset': '\033[m',
    'blue': '\033[34m',
    'yellow': '\033[33m',
    'negative': '\033[7;37m'
}

print(f'Olá, muito prazer em te conhecer {colors["negative"]}{name}{colors["reset"]}')