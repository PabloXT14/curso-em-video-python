# Exercício 41 - Classificando Atletas (Aula 012)

'''
# Descrição:

A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIN
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÉNIOR
- Acima: MASTER
'''

# Resolução:

from datetime import datetime

print('# Classificação de Atletas')

print('-' * 70)

birth_year = int(input('Digite seu ano de nascimento do atleta: '))

print('-' * 70)

current_year = datetime.now().year

user_age = current_year - birth_year

user_category = ''

if (user_age <= 9):
    user_category = 'MIRIN'
elif (user_age <= 14):
    user_category = 'INFANTIL'
elif (user_age <= 19):
    user_category = 'JUNIOR'
elif (user_age <= 20):
    user_category = 'SÉNIOR'
else:
    user_category = 'MASTER'

print(f'* A categoria do atleta é: {'\033[1;33m'}{user_category}{'\033[m'}')
