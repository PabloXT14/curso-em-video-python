# Exercício 31 - Custo da viagem (Aula 010)

'''
# Descrição:

Desenvolva um programa que pergunte a distância da viagem em Km. Calcule o preço da passagem, cobrando:
- R$ 0,50 por Km para viagens de até 200km.
- R$ 0,45 para viagens mais longas (+200km).
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

print('# Custo da viagem')

print('-' * 70)

trip_distance = float(input('Qual a distância da viagem em Km: '))

print('-' * 70)

fits_primary_pricing = trip_distance <= 200

primary_distance_pricing = 0.50
secondary_distance_pricing = 0.45

ticket_price = 0

if (fits_primary_pricing):
    ticket_price = trip_distance * primary_distance_pricing

    print(f'* Valor por Km: {colors["yellow"]}R$ {primary_distance_pricing:.2f}{styles["reset"]}')
else:
    ticket_price = trip_distance * secondary_distance_pricing

    print(f'* Valor por Km: {colors["yellow"]}R$ {secondary_distance_pricing:.2f}{styles["reset"]}')

print(f'* Preço da passagem: {colors["yellow"]}R$ {ticket_price:.2f}{styles["reset"]}')
