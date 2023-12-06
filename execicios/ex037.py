# Exercício 37 - Conversor de Bases Numéricas (Aula 012)

'''
# Descrição: 

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 'base de conversão':

- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

# Resolução:

'''
# Explicando Conceitos
O [2:] é uma notação de fatiamento (slicing) de texto (string) em Python. Quando você converte um número para binário, octal ou hexadecimal usando as funções embutidas bin, oct ou hex, o resultado é uma string que inclui um prefixo indicando a base.

Por exemplo:

Binário: 0b (prefixo)
Octal: 0o (prefixo)
Hexadecimal: 0x (prefixo)
O [2:] é usado para remover esse prefixo e obter apenas a parte significativa do número. Por exemplo, se o número binário gerado for 0b1101, usar [2:] resultará em 1101, que é a representação binária sem o prefixo 0b
'''

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

    if 1 <= int(option) <= 3:
        break
    else:
        print('Escolha inválida. Por favor digite uma das opções disponíveis.')
    
    print('-' * 70)


if (option == 1):
    binary_value = bin(number)[2:]
    print(f'* Valor em Binário: {'\033[1;33m'}{binary_value}{'\033[m'}')
elif (option == 2):
    octal_value = oct(number)[2:]
    print(f'* Valor em Octal: {'\033[1;33m'}{octal_value}{'\033[m'}')
else:
    hexadecimal_value = hex(number)[2:]
    print(f'* Valor em Hexadecimal: {'\033[1;33m'}{hexadecimal_value}{'\033[m'}')
