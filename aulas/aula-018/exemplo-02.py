people = [['John', 19], ['Ane', 33], ['Josh', 13], ['Mary', 45]]

print(people) # Saída: [['John', 19], ['Ane', 33], ['Josh', 13], ['Mary', 45]]
print(people[0]) # Saída: ['John', 19]
print(people[1][0]) # Saída: Ane

print('-' * 70)

# Iterando sobre a lista aninhada
print(f'| {'NOME':^10} | {'IDADE':^10} |')
for person in people:
    print(f'| {person[0]:^10} | {person[1]:^10} |')
