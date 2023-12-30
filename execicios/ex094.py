# Exercício 94 - Unindo dicionários em listas (019)

'''
# Descrição:

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoas em um dicionário e todos os dados em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''

# Resolução:

line_length = 70

print('# Unindo Dicionários em Lista')

people = []
person = {}

sum_ages = 0

women = []
above_average_age = []

while True:
    print('-' * line_length)

    print(f'{'\033[1;32m'}{f'{len(people) + 1}ª PESSOA':^{line_length}}{'\033[m'}')

    print('-' * line_length)

    person['name'] = str(input('Nome: ')).strip().title()

    while True:
        gender = str(input('Sexo (M/F): ')).strip().upper()

        if gender in ('M', 'F'):
            break
        else:
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada inválida! Digite (M) para masculino ou (F) feminino. {'\033[m'}')
            print('-' * line_length)
    
    person['gender'] = gender

    person['age'] = int(input('Idade: '))

    sum_ages += person['age']

    people.append(person.copy())
    person.clear()

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()

        if answer in ('S', 'N'):
            break
        else:
            print(f'{'\033[1;31m'}Entrada inválida! Digite (S) para Sim ou (N) para Não. {'\033[m'}')
    
    if (answer == 'N'):
        break

print('-' * line_length)

average_age = int(sum_ages / len(people))

for person in people:
    if person['gender'] == 'F':
        women.append(person['name'])
    
    if person['age'] > average_age:
        above_average_age.append(person['name'])

print(f'* Quantidade de pessoas cadastradas: {'\033[1;33m'}{len(people)}{'\033[m'}')
print(f'* Média de idade do grupo: {'\033[1;33m'}{average_age}{'\033[m'}')
print(f'* Lista de mulheres: {'\033[1;33m'}{', '.join(women)}{'\033[m'}')
print(f'* Lista de pessoas com idade acima da média: {'\033[1;33m'}{', '.join(above_average_age)}{'\033[m'}')

print('-' * line_length)
