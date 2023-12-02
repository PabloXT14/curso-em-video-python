# Exercício 33 - Maior e menor valores (Aula 010)

'''
# Descrição:

Faça um programa que leia três números e mostre qual é o 'maior' e qual é o 'menor'.
'''

# Resolução:

styles = {
    'reset': '\033[m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reverse': '\033[7m'
}

colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'gray': '\033[37m',
    'white': '\033[97m'
}

backgrounds = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'magenta': '\033[45m',
    'cyan': '\033[46m',
    'gray': '\033[47m',
    'white': '\033[107m'
}

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

print(f'* O maior número é: {styles["bold"] + colors["green"]}{highest_number}{styles["reset"]}')
print(f'* O menor número é: {styles["bold"] + colors["red"]}{lowest_number}{styles["reset"]}')
