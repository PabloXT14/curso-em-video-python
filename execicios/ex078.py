# Exercício 78 - Maior e Menor valores na Lista (017)

'''
# Descrição:

Faça um programa que leia 5 valores numéricos guarde em uma lista.

No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.
'''

# Resolução:

line_length = 70

print('# Maior e Menores Valores na Lista')

print('-' * line_length)

numbers = []

for i in range(0, 5):
    number = float(input(f'Digite o {i + 1}º valor: '))

    numbers.append(number)

print('-' * line_length)

highest_value = max(numbers)
lowest_value = min(numbers)
highest_position = numbers.index(highest_value) + 1
lowest_position = numbers.index(lowest_value) + 1

print(f'* Lista de números: {'\033[1;33m'}{numbers}{'\033[m'}')
print(f'* Maior valor: {'\033[1;33m'}{highest_value} (posição {highest_position}){'\033[m'}')
print(f'* Menor valor: {'\033[1;33m'}{lowest_value} (posição {lowest_position}){'\033[m'}')
