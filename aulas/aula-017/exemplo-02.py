values = []

for i in range(0, 5):
    values.append(int(input(f'Digite o {i + 1}º valor inteiro: ')))

print('-' * 70)

# Iterando a Lista
for i, value in enumerate(values):
    print(f'posição[{i}] = {value}')
