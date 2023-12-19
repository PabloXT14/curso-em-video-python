# Exercício 75 - Análise de Dados em uma Tupla (016)

'''
# Descrição:

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) quais foram os números pares.
'''

# Resolução:

print('# Análise de Dados em uma Tupla')

line_length = 70

print('-' * line_length)

# 1ª Forma de preencher a tuplas
'''
number1 = int(input('Digite o 1ª número: '))
print('-' * line_length)
number2 = int(input('Digite o 2ª número: '))
print('-' * line_length)
number3 = int(input('Digite o 3ª número: '))
print('-' * line_length)
number4 = int(input('Digite o 4ª número: '))

numbers = (number1, number2, number3, number4)
'''

# 2ª Forma de preencher a tuplas
numbers = tuple(
    int(input(f'Digite o {i + 1}º valor: ')) for i in range(4)
)

occurrences_9 = numbers.count(9)
position_3 = numbers.index(3) + 1 if 3 in numbers else None

print('-' * line_length)

print(f'A) Quantidade de vezes que o valor 9 apareceu: {'\033[1;33m'}{occurrences_9}{'\033[m'}')
print(f'B) Posição do primeiro valor 3: {'\033[1;33m'}{position_3}{'\033[m'}')

print('C) Números pares digitados: ', end='')

for i, number in enumerate(numbers):
    if number % 2 == 0:
        print(f'{'\033[1;33m'}{number}{'\033[m'}', end=' ')

print() # Quebra linha para próximos valores
