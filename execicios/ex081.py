# Exercício 81 - Extraindo dados de uma Lista (017)

'''
# Descrição:

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digita e está ou não na lista.
'''

# Resolução:

line_length = 70

print('# Extraindo dados de uma Lista')

print('-' * line_length)

numbers_list = []
number_searched = 5

while True:
    number = int(input('Digite um valor: '))

    numbers_list.append(number)

    print('-' * line_length)

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()

        if answer in 'SN':
            break
    
    if answer == 'N':
        break

    print('-' * line_length)

print('-' * line_length)

numbers_list.sort(reverse=True) # Colocando lista em ordem decrescente

print(f'A) Quantidade de números digitados: {'\033[1;33m'}{len(numbers_list)}{'\033[m'}')
print(f'B) Lista em ordem decrescente: {'\033[1;33m'}{numbers_list}{'\033[m'}')
print(f'C) O valor {number_searched} está na lista: {'\033[1;33m'}{f'Sim (posição {numbers_list.index(number_searched) + 1})' if number_searched in numbers_list else 'Não'}{'\033[m'}')
