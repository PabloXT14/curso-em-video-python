# Exercício 56 - Analisador completo (013)

'''
# Descrição:

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''

# Resolução:

print('# Analisador Completo')

people_amount = 4

ages_sum = 0
average_age = 0
oldest_man_name = ''
oldest_man_age = 0
count_women_under_20 = 0

print('-' * 70)

for i in range(0, people_amount):
    print(f'* Digite os dados da pessoa {i + 1}:')

    person_name = str(input('Nome: '))
    person_age = int(input('Idade: '))
    person_gender = str(input('Sexo (M/F): ')).upper()

    # Atualiza a soma das idades
    ages_sum += person_age

    # Verifica se é um homem e se é o mais avelho até agora
    if (person_gender == 'M' and person_age > oldest_man_age):
        oldest_man_age = person_age
        oldest_man_name = person_name.capitalize()
    
    # Verifica se é mulher com menos de 20 anos
    if (person_gender == 'F' and person_age < 20):
        count_women_under_20 += 1

    print('-' * 70)

# Idade média
average_age = int(ages_sum / people_amount)

print('* Resultados:')
print(f'* Média de idade do grupo: {'\033[1;33m'}{average_age} anos{'\033[m'}')
print(f'* Homem mais velho: {'\033[1;33m'}{oldest_man_name} com {oldest_man_age} anos{'\033[m'}')
print(f'* Mulheres com menos de 20 anos: {'\033[1;33m'}{count_women_under_20}{'\033[m'}')
