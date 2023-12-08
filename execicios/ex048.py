# Exercício 48 - Soma ímpares múltiplos de 3 (013)

'''
# Descrição:

Faça um programa que calcule a some entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

# Resolução:

print('# Soma ímpares múltiplos de 3')

print('-' * 70)

start_range = 1
end_range = 501

total_odd_sum = 0
numbers_per_line = 10
numbers_in_line = 0

print('* Números:')

for number in range(start_range, end_range):
    if (number % 2 != 0) and (number % 3 == 0):
        print(f'{number:3}', end=" ")
        total_odd_sum += number
        numbers_in_line += 1

        # Quebra de linha
        if numbers_in_line == numbers_per_line:
            print()
            numbers_in_line = 0

print()
print('-' * 70)

print(f'* Soma total dos números: {'\033[1;33m'}{total_odd_sum}{'\033[m'}')
