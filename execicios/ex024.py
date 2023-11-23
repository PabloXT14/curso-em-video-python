# Exercício 24 - Verificando as primeiras letras de um texto (Aula 009)

'''
# Descrição: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

# Resolução:

print('Verificando as primeiras letras de um texto')

print('-' * 80)

city_name = input('Digite o nome de uma cidade: ')

print('-' * 80)

city_name = city_name.lower()

if (city_name.startswith('santo')):
    print("O nome da cidade começa com 'SANTO'.")
else:
    print("O nome da cidade não começa com 'SANTO'.")
