# Exercício 25 - Procurando uma string dentro de outra (Aula 009)

'''
# Descrição: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

# Resolução:

print('Procurando uma string dentro de outra')

print('-' * 80)

name = input('Digite seu nome: ')

print('-' * 80)

name = name.lower()

has_silva = 'silva' in name

if (has_silva):
    print("Essa pessoa tem 'SILVA' no nome.")
else:
    print("Essa pessoa não tem 'SILVA' no nome.")
