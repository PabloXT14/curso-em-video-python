# Exercício 54 - Grupo da Maioridade (013)

'''
# Descrição:

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

# Resolução:

from datetime import datetime

print('# Grupo de Maioridade')

current_year = datetime.now().year
age_of_majority = 18

people_amount = 7
minors_amount = 0
adults_amount = 0

print('-' * 70)

for i in range(0, people_amount):
    person_birth_year = int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))

    person_age = current_year - person_birth_year 

    if (person_age >= age_of_majority):
        adults_amount += 1
    else:
        minors_amount += 1
    
    print('-' * 70)

print('* Resultados:')
print(f'* Pessoas maiores de idade: {'\033[1;33m'}{adults_amount}{'\033[m'}')
print(f'* Pessoas menores de idade: {'\033[1;33m'}{minors_amount}{'\033[m'}')
