# Exercício 37 - Conversor de Bases Numéricas (Aula 012)

'''
# Descrição: 

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 'base de conversão':

- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

# Resolução:

print('Conversor de Bases Numéricas')

print('-' * 70)

number = int(input('Digite um número inteiro: '))

print('-' * 70)

option = 0

while True:
    print('Escolha a base de conversão:')
    print('1 - Binário')
    print('2 - Octal')
    print('3 - Hexadecimal')

    option = int(input('Digite o número da sua opção desejada: '))

    print('-' * 70)

    if (option == 1) or (option == 2) or (option == 3):
        break


if (option == 1):
    binary_value = bin(number)
    print(f'* Valor em Binário: {binary_value}')
elif (option == 2):
    octal_value = oct(number)
    print(f'* Valor em Octal: {octal_value}')
else:
    hexadecimal_value = hex(number)
    print(f'* Valor em Hexadecimal: {hexadecimal_value}')
