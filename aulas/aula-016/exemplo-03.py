# Iterando a tupla
snacks = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Iterando com for
for food in snacks:
    print(f'* {food}')

print('-' * 70)

for i in range(0, len(snacks)):
    print(f'* {snacks[i]}')

print('-' * 70)

for index, food in enumerate(snacks):
    print(f'{index} - {food}')
