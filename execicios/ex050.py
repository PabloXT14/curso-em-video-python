# Exercício 50 - Soma dos pares (013)

'''
# Descrição:

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

# Resolução:

print('# Soma dos pares')

print('-' * 70)

# 1ª Solução:

even_sum = 0

for i in range(6):
    current_number = int(input('Digite um número inteiro: '))

    if (current_number % 2 == 0):
        even_sum += current_number
    
    print('-' * 70)

print(f'Soma dos pares: {'\033[1;33m'}{even_sum}{'\033[m'}')

# 2ª Solução
'''
even_numbers = []

for i in range(1, 7):
    current_number = int(input(f'Digite o {i}º número: '))

    if (current_number % 2 == 0):
        even_numbers.append(current_number)

    print('-' * 70)


total_even_sum = sum(even_numbers)

print(f'Soma dos pares: {'\033[1;33m'}{total_even_sum}{'\033[m'}')
'''
