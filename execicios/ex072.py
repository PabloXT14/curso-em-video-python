# Exercício 72 - Número por Extenso (016)

'''
# Descrição:

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

# Resolução:

print('# Número por Extenso')

line_length = 100

print('-' * line_length)

numbers_by_extent = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

can_continue = True

while can_continue:

    while True:
        number = int(input('Digite um número inteiro (entre 0 e 20): '))

        if 0 <= number <= 20:
            break
        
        print('-' * line_length)

        print(f'{'\033[1;31m'}Entrada inválida. Por favor, digite um número dentro do intervalo mostrado.{'\033[m'}')

        print('-' * line_length)

    print('-' * line_length)

    number_name = numbers_by_extent[number].capitalize()

    print(f'* Número {number} por extenso: {'\033[1;33m'}{number_name}{'\033[m'}')

    print('-' * line_length)

    while True:
        answer = str(input('Deseja digitar outro número? (S/N): ')).strip().upper()

        if answer == 'S':
            break
        elif answer == 'N':
            can_continue = False
            break
    
    print('-' * line_length)
