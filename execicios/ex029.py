# Exercício 29 - Radar Eletronico (Aula 010)

'''
# Descrição:

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
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

print('# Radar Eletronico')

print('-' * 80)

car_speed = float(input('A qual velocidade o carro estava (Km/h): '))

print('-' * 80)

limit_speed = 80

is_above_speed_limit = car_speed > limit_speed

fine_per_kilometer = 7

if (is_above_speed_limit):
    speed_exceeded = round(car_speed - limit_speed)

    fine_value = fine_per_kilometer * speed_exceeded

    print(f'{styles["bold"] + colors["red"]}* MULTADO! Você ultrapassou o limite de 80km/h{styles["reset"]}')
    print(f'* Quilometros excedidos: {speed_exceeded}Km/h')
    print(f'* Valor da multa: {colors["yellow"]}R$ {fine_value:.2f}{styles["reset"]}')
else:
    print(f'{styles["bold"] + colors["green"]}* Você está dentro do limite de velocidade (80Km/h). Dirija com segurança{styles["reset"]}')
