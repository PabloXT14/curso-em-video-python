# Exercício 80 - Lista Ordenada sem Repetições (017)

'''
# Descrição:

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

# Resolução:

line_length = 70

print('# Lista Ordenada sem Repetições')

print('-' * line_length)

numbers_amount = 5
numbers_list = []

# 1ª Solução
for i in range(numbers_amount):
    number_typed = int(input(f'Digite o {i + 1}º valor: '))

    print('-' * line_length)

    if i == 0 or number_typed > numbers_list[-1]:
        numbers_list.append(number_typed)
        
        print(f'{'\033[1;33m'}Valor {number_typed} adicionado ao final da lista{'\033[m'}')
    else:
        # for i, number in enumerate(numbers_list):
        #     if number_typed <= number:
        #         numbers_list.insert(i, number_typed)

        #         print(f'{'\033[1;33m'}Valor {number_typed} adicionado na posição {i}{'\033[m'}')

        #         break
        
        # OR
        position = 0
        while position < len(numbers_list):
            if number_typed <= numbers_list[position]:
                numbers_list.insert(position, number_typed)
                print(f'{'\033[1;33m'}Valor {number_typed} adicionado na posição {position}{'\033[m'}')
                break
            position += 1

    print('-' * line_length)

print(f'* Valores em ordem: {'\033[1;33m'}{numbers_list}{'\033[m'}')


# 2ª Solução
'''
for i in range(numbers_amount):
    number_typed = int(input(f'Digite o {i + 1}º valor: '))

    print('-' * line_length)

    position = 0

    while position < len(numbers_list) and number_typed > numbers_list[position]:
        position += 1
    
    numbers_list.insert(position, number_typed)

    print(f'Valor {number_typed} adicionado na posição {position}')

    print('-' * line_length)

print(f'* Valores em ordem: {'\033[1;33m'}{numbers_list}{'\033[m'}')
'''
