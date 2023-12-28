# Exercício 85 - Lista com Pares e Ímpares (018)

'''
# Descrição:

Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

# Resolução:

line_length = 70

print('# Lista com Pares e Ímpares')

print('-' * line_length)

numbers = [[], []]
numbers_amount = 7

for i in range(0, numbers_amount):
    number = int(input(f'Digite o {i + 1}º valor: '))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

print('-' * line_length)

even_numbers = numbers[0][:]
odd_numbers = numbers[1][:]

even_numbers.sort()
odd_numbers.sort()

print(f'* Números pares: {'\033[1;33m'}{even_numbers}{'\033[m'}')
print(f'* Números ímpares: {'\033[1;33m'}{odd_numbers}{'\033[m'}')
