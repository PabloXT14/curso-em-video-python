# Exercício 79 - Valores Únicos em uma Lista (017)

'''
# Descrição:

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

# Resolução:

line_length = 70

print('# Valores Únicos em uma Lista')

print('-' * line_length)

unique_numbers = []

while True:
    number = int(input('Digite um valor: '))

    print('-' * line_length)

    if number in unique_numbers:
        print(f'{'\033[1;33m'}Este valor já existe na lista! Então não vou adicionar...{'\033[m'}')
    else:
        unique_numbers.append(number)
        print(f'{'\033[1;32m'}Valor adicionado com sucesso!{'\033[m'}')
    
    print('-' * line_length)

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()

        if answer in 'SN':
            break

    print('-' * line_length)

    if answer == 'N':
        break

unique_numbers = sorted(unique_numbers)

print(f'* Valores digitados: {'\033[1;33m'}{unique_numbers}{'\033[m'}')
