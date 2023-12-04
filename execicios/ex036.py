# Exercício 36 - Aprovando Empréstimo (Aula 012)

'''
# Descrição: 

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o 'valor da casa', o 'salário' do comprador e em 'quantos anos' ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negador.
'''

# Resolução:

from math import ceil

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


print('# Aprovando Empréstimo')

print('-' * 70)

home_value = float(input('Qual o valor da casa que pretende comprar? R$: '))
buyer_salary = float(input('Qual o valor do seu salário? R$: '))
years_to_pay = int(input('Em quantos anos pretende pagar o empréstimo?: '))

print('-' * 70)


monthly_payment = home_value / (years_to_pay * 12)

installment_limit = buyer_salary * (30/100)

is_installment_approved = monthly_payment <= installment_limit

if is_installment_approved:
    print(f'{styles["bold"] + colors["green"]}* EMPRÉSTIMO APROVADO!{styles["reset"]}')
    print(f'* Valor da prestação mensal: {styles["bold"] + colors["yellow"]}R$ {monthly_payment:.2f}{styles["reset"]}')
else:
    print(f'{styles["bold"] + colors["red"]}* EMPRÉSTIMO NEGADO!{styles["reset"]}')
    print(f'{styles["bold"] + colors["yellow"]}* Valor da prestação excede 30% do salário.{styles["reset"]}')
