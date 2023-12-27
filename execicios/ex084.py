# Exercício 84 - Lista Composta e Análise de Dados (018)

'''
# Descrição:

Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

# Resolução:

line_length = 71

print('# Lista Composta e Análise de Dados')

people = []
highest_weight = 0
lowest_weight = 0
heaviest_people = []
lighter_people = []

while True:
    print(f'{'-' * int((line_length - 10) / 2)} {len(people) + 1}ª PESSOA {'-' * int((line_length - 10) / 2)}')

    name = str(input('Nome: '))
    weight = float(input('Peso (kg): '))

    person = [name, weight]

    if len(people) == 0:
        highest_weight = weight
        lowest_weight = weight
    else:
        if weight > highest_weight:
            highest_weight = weight
        elif weight < lowest_weight:
            lowest_weight = weight

    people.append(person[:])

    person.clear()

    print('-' * line_length)

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()

        if answer in ('S', 'N'):
            break
        else:
            print('-' * line_length)

            print(f'{'\033[1;31m'}Opção inválida. Digite S para continuar ou N para sair.{'\033[m'}')
            
            print('-' * line_length)
    
    print('-' * line_length)
    
    if answer == 'N':
        break

for person in people:
     person_name = person[0]
     person_weight = person[1]

     if person_weight == highest_weight:
         heaviest_people.append(person_name)
     
     if person_weight == lowest_weight:
         lighter_people.append(person_name)


print(f'* Quantidade de pessoas cadastradas: {'\033[1;33m'}{len(people)}{'\033[m'}')
print(f'* Pessoas mais pesadas ({highest_weight:.2f} kg): {'\033[1;33m'}{", ".join(heaviest_people)}{'\033[m'}')
print(f'* Pessoas mais leves ({lowest_weight:.2f} kg): {'\033[1;33m'}{", ".join(lighter_people)}{'\033[m'}')
