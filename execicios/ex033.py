# Exercício 33 - Maior e menor valores (Aula 010)

'''
# Descrição:

Faça um programa que leia três números e mostre qual é o 'maior' e qual é o 'menor'.
'''

# Resolução:

print('# Maior e menor valores')

print('-' * 70)

# 1ª Solução
'''
numbers = []

while True:
    number = float(input(f'Digite o {len(numbers) + 1}º número: '))

    numbers.append(number)

    if (len(numbers) >= 3):
        break

highest_number = numbers[0]
lowest_number = numbers[0]

for number in numbers:
    if (number > highest_number):
        highest_number = number

    if (number < lowest_number):
        lowest_number = number

'''

# 2ª Solução

number_1 = float(input('Digite o 1º número: '))
number_2 = float(input('Digite o 2º número: '))
number_3 = float(input('Digite o 3º número: '))

highest_number = number_1
lowest_number = number_1

if (number_2 > highest_number):
    highest_number = number_2
elif (number_2 < lowest_number):
    lowest_number = number_2

if (number_3 > highest_number):
    highest_number = number_3
elif (number_3 < lowest_number):
    lowest_number = number_3

print('-' * 70)

print(f'* O maior número é: {highest_number}')
print(f'* O menor número é: {lowest_number}')
