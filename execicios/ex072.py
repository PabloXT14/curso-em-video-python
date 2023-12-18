# Exercício 72 - Número por Extenso (016)

'''
# Descrição:

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

# Resolução:

print('# Número por Extenso')

print('-' * 100)

numbers_by_extent = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    number = int(input('Digite um número inteiro (entre 0 e 20): '))

    if 0 <= number <= 20:
        break
    else:
        print('-' * 100)

        print(f'{'\033[1;31m'}Entrada inválida. Por favor, digite um número dentro do intervalo mostrado.{'\033[m'}')

        print('-' * 100)

print('-' * 100)

number_name = numbers_by_extent[number].capitalize()

print(f'* Número {number} por extenso: {'\033[1;33m'}{number_name}{'\033[m'}')
