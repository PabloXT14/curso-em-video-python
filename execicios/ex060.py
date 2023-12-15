# Exercício 60 - Cálculo do Fatorial (014)

'''
# Descrição:

Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
'''

# Resolução:

print('# Cálculo do Fatorial')

print('-' * 70)

number = int(input('Digite um número para calcular seu fatorial: '))

print('-' * 70)

# 1ª Solução
if (number >= 0):

    factorial_result = 1

    can_continue = True if (number > 1) else False

    print(f'{number}! = ', end='')

    while can_continue:
        print(f'{number}', end='')
        print(' x ' if number > 1 else ' = ', end='')

        factorial_result *= number

        number -= 1

        if (number <= 0):
            can_continue = False

    print(f'{'\033[1;33m'}{factorial_result}{'\033[m'}')

else:
    print(f'{'\033[1;33m'}* Por favor, digite um número não negativo.{'\033[m'}')
    

# 2ª Solução
'''
if (number >= 0):
    print(f'{number}! = ', end='')

    factorial_result = 1

    if (number > 1):
        for i in range(number, 0, -1):
            factorial_result *= i

            print(f'{i}', end='')
            print(' x ' if i > 1 else ' = ', end='')
    
    print(f'{'\033[1;33m'}{factorial_result}{'\033[m'}')
else:
    print(f'{'\033[1;33m'}* Por favor, digite um número não negativo.{'\033[m'}')
'''

    
# 3ª Solução
'''
from math import factorial

if (number >= 0):
    factorial_result = factorial(number) 

    print(f'* O fatorial de {number} é: {'\033[1;33m'}{factorial_result}{'\033[m'}')
else:
    print(f'{'\033[1;33m'}* Por favor, digite um número não negativo.{'\033[m'}')
'''
