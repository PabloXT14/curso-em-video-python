# Exercício 69 - Análise de dados do grupo (015)

'''
# Descrição:

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados
C) Quantas mulheres têm menos de 20 anos.
'''

# Resolução:

print('# Análise de dados do grupo')

count_people = 0
count_adults = 0
count_men = 0
count_women_under_twenty = 0

while True:
    print('-' * 70)

    count_people += 1

    print(f'{'\033[1;32m'}CADASTRAR {count_people}ª PESSOA{'\033[m'}')

    print('-' * 70)

    age = int(input('Idade: '))
    
    while True:
        gender = str(input('Sexo (M/F): ')).strip().upper()

        if (gender in 'MF'):
            break

    print('-' * 70)

    if age >= 18:
        count_adults += 1

    if gender == 'M':
        count_men += 1
    
    if (age < 18) and (gender == 'F'):
        count_women_under_twenty += 1

    while True:
        answer = str(input('Deseja continuar (S/N): ')).strip().upper()

        if (answer in 'SN'):
            break
    
    if answer == 'N':
        break

print('-' * 70)

print(f'* Pessoas cadastradas: {'\033[1;33m'}{count_people}{'\033[m'}')
print(f'* Adultos: {'\033[1;33m'}{count_adults}{'\033[m'}')
print(f'* Homens: {'\033[1;33m'}{count_men}{'\033[m'}')
print(f'* Mulheres menores de 20 anos: {'\033[1;33m'}{count_women_under_twenty}{'\033[m'}')
