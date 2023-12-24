person = list()

person.append('Gustavo')
person.append(40)

people = list()

people.append(person[:]) # Sem os o símbolo de [:] acabe tendo uma ligação entre as duas lista de desta forma qualquer alteração que realizarmos posteriormente vai se refletir na lista anterior

person[0] = 'Maria'
person[1] = 22

people.append(person[:])

print(people)
