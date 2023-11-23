# Exercício 27 - Primeiro e último nome de uma pessoa (Aula 009)

'''
# Descrição: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
Ex: Ana Maria de Souza
- Primeiro: Ana
- Último: Souza
'''

# Resolução:

print('Primeiro e último nome de uma pessoa')

print('-' * 80)

name = input('Digite seu nome: ')

print('-' * 80)

names_array = name.strip().split(' ')

first_name = names_array[0]
last_name = names_array[len(names_array) - 1] # ou somente -1 pois referencia o primeiro item de um array de tras para a frente

print(f'- Primeiro nome: {first_name.capitalize()}')
print(f'- Último nome: {last_name.capitalize()}')
