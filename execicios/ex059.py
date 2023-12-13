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

print('# Criando um Menu de Opções')

finish_program = False

while not finish_program:    
    print('-' * 70)

    number1 = float(input('Digite o 1º valor: '))
    number2 = float(input('Digite o 2º valor: '))

    print('-' * 70)

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
            print(f'{number1} > {number2}')
        elif (number2 > number1):
            print(f'{number2} > {number1}')
        else:
            print(f'{number1} = {number2}')
    elif (menu_option == 4):
        continue
    elif (menu_option == 5):
        finish_program = True
    else:
        print(f'{'\033[1;31m'}* Opção inválida. Por favor escolha um dos valores especificados.{'\033[m'}')
    