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

number = int(input('Digite um número: '))

print('-' * 70)

if (number >= 0):

    factorial_result = 1

    can_continue = True if (number > 0) else False

    print(f'{number}! = ', end='')

    while can_continue:
        if (number != 1):
            print(f'{number} x ', end='')
        else:
            print(f'{number} = ', end='')

        factorial_result *= number

        number -= 1

        if (number <= 0):
            can_continue = False

    print(f'{'\033[1;33m'}{factorial_result}{'\033[m'}')

else:
    print(f'{'\033[1;33m'}* Por favor, digite um número não negativo.{'\033[m'}')
