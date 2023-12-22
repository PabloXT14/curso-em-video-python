# Exercício 82 - Dividindo valores em várias Listas (017)

'''
# Descrição:

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdos das três listas geradas.
'''

# Resolução:

line_length = 70

print('# Dividindo valores em várias Listas')

print('-' * line_length)

numbers = []

while True:
    number = int(input('Digite um valor: '))

    numbers.append(number)

    print('-' * line_length)

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()

        if answer in 'SN':
            break
    
    print('-' * line_length)

    if answer == 'N':
        break

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'* Lista original: {'\033[1;33m'}{numbers}{'\033[m'}')
print(f'* Números pares: {'\033[1;33m'}{even_numbers}{'\033[m'}')
print(f'* Número ímpares: {'\033[1;33m'}{odd_numbers}{'\033[m'}')
