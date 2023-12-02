# Exercício 34 - Aumentos multiplos (Aula 010)

'''
# Descrição:

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

Para inferiores ou iguais, o aumento é de 15%.
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
    'white': '\033[107m',
}

print('Aumentos multiplos')

print('-' * 70)

wage = float(input('Digite seu salário (R$): '))

print('-' * 70)

primary_salary_increase = 15/100
secondary_salary_increase = 10/100

fits_the_primary_increase = wage <= 1250

new_wage = 0
increase_value = 0

if (fits_the_primary_increase):
    increase_value = wage * primary_salary_increase
    new_wage = wage + increase_value
else:
    increase_value = wage * secondary_salary_increase
    new_wage = wage + increase_value

print(f'* Antigo salário: {styles["bold"] + colors["yellow"]}R$ {wage:.2f}{styles["reset"]}')
print(f'* Valor de aumento: {styles["bold"] + colors["yellow"]}R$ {increase_value:.2f}{styles["reset"]}')
print(f'* Novo salário: {styles["bold"] + colors["yellow"]}R$ {new_wage:.2f}{styles["reset"]}')
