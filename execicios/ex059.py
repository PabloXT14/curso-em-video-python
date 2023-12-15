# Exercício 59 - Criando um Menu de Opções (014)

'''
# Descrição:

Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

Seu programa deverá realizar a opção solicitada em cada caso.
'''

# Resolução:
from time import sleep

print('# Criando um Menu de Opções')

print('-' * 70)

number1 = float(input('Digite o 1º valor: '))
number2 = float(input('Digite o 2º valor: '))

finish_program = False

while not finish_program:
    print('-' * 70)

    sleep(1)

    print('Menu:')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do programa')

    menu_option = int(input('Escola uma opção (1 a 5): '))

    print('-' * 70)

    if (menu_option == 1):
        result = number1 + number2
        print(f'{number1} + {number2} = {'\033[1;33m'}{result}{'\033[m'}')
    elif (menu_option == 2):
        result = number1 * number2
        print(f'{number1} x {number2} = {'\033[1;33m'}{result}{'\033[m'}')
    elif (menu_option == 3):
        if (number1 > number2):
            print(f'{'\033[1;33m'}{number1}{'\033[m'} > {number2}')
        elif (number2 > number1):
            print(f'{'\033[1;33m'}{number2}{'\033[m'} > {number1}')
        else:
            print(f'{'\033[1;33m'}{number1}{'\033[m'} = {'\033[1;33m'}{number2}{'\033[m'}')
    elif (menu_option == 4):
        number1 = float(input('Digite o 1º valor: '))
        number2 = float(input('Digite o 2º valor: '))
    elif (menu_option == 5):
        finish_program = True
    else:
        print(f'{'\033[1;31m'}* Opção inválida. Por favor escolha um dos valores especificados.{'\033[m'}')

print(f'{'\033[1;32m'}* Fim do programa! Volte sempre.{'\033[m'}')
