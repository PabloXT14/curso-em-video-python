# Criando um dicionário
person = { 
    'name': 'John',
    'age': 21,
    'gender': 'M'
}

line_length = 70

# Acessando Valores
print(f'O {person['name']} tem {person["age"]} anos.')

print('-' * line_length)

# Métodos úteis
print(f'KEYS: {person.keys()}')
print(f'VALUES: {person.values()}')
print(f'ITEMS: {person.items()}')

print('-' * line_length)

# Iterando sobre Chaves e Valores
for key in person.keys():
    print(key)

print('-' * line_length)

for value in person.values():
    print(value)

print('-' * line_length)

for key,value in person.items():
    print(f'{key}: {value}')

print('-' * line_length)

# Removendo Chaves e Valores
del person['gender']
print(person)

print('-' * line_length)

# Adicionando e atualizando valores
person['name'] = 'Leandro'
print(person['name']) # update

person['peso'] = 98.5 # create

print('-' * line_length)
