# Exercício 92 - Cadastro de Trabalhador em Python (019)

'''
# Descrição:

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS (Carteira de Trabalho de Previdência Social) for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

* OBS: considere para ambos os sexos o mínimo de 35 anos de contribuição para a Previdência Social 
'''

# Resolução:

from datetime import datetime

line_length = 70

print('# Cadastro de Trabalhador em Python')

print('-' * line_length)

worker = {}
minimum_contribution_years = 35

worker['name'] = str(input('Digite o nome: ')).strip().title()
worker['birth_year'] = int(input('Digite o ano de nascimento: '))
worker['age'] = datetime.now().year - worker['birth_year']
worker['ctps'] = int(input('Digite o número da Carteira de Trabalho - CTPS (0 se não tem): '))

if worker['ctps'] != 0:
    worker['contract_year'] = int(input('Digite o ano de contratação: '))
    worker['salary'] = float(input('Digite o salário (R$): '))

    age_began_working = worker['contract_year'] - worker['birth_year']
    retirement_age = age_began_working + minimum_contribution_years
    worker['retirement_age'] = retirement_age

print('-' * line_length)

print(f'* Nome: {'\033[1;33m'}{worker["name"]}{'\033[m'}')
print(f'* Idade: {'\033[1;33m'}{worker["age"]}{'\033[m'}')

if worker['ctps'] == 0:
    print(f'* CTPS: {'\033[1;33m'}{'NÃO POSSUI'}{'\033[m'}')
else:
    print(f'* CTPS: {'\033[1;33m'}{worker["ctps"]}{'\033[m'}')
    print(f'* Ano da 1ª contratação: {'\033[1;33m'}{worker["contract_year"]}{'\033[m'}')
    print(f'* Salário: {'\033[1;33m'}R$ {worker["salary"]:.2f}{'\033[m'}')
    print(f'* Idade de aposentadoria: {'\033[1;33m'}{worker["retirement_age"]}{'\033[m'}')

print('-' * line_length)
