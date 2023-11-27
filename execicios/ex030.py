# Exercício 30 - Par ou ímpar (Aula 010)

'''
# Descrição:

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

# Resolução:

print('# Par ou Ímpar')

print('-' * 70)

number = int(input('Digite um número inteiro: '))

print('-' * 70)

print(f'* Resultado: {'PAR' if (number % 2 == 0) else 'ÍMPAR'}')
