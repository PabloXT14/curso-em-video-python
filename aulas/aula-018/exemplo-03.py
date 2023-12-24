people = list()
person = list()

total_young = 0
total_adult = 0

for i in range(0, 3):
    name  = str(input(f'Digite o nome da pessoa {i + 1}: '))
    age = int(input(f'Digite a idade da pessoa {i + 1}: '))

    person.append(name)
    person.append(age)

    people.append(person[:])
    person.clear()

    print('-' * 70)

for person in people:
    if person[1] >= 18:
        print(f'{person[0]} é maior de idade.')
        total_adult += 1
    else:
        print(f'{person[0]} é menor de idade.')
        total_young += 1

print('-' * 70)

print(f'* Quantidade de maiores de idade: {total_adult}')
print(f'* Quantidade de menores de idade: {total_young}')
