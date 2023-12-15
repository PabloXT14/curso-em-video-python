# Exercício 61 - Progressão Aritmética v2.0 (014)

'''
# Descrição:

Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

# Resolução:

# Fórmula PA: An = A1 + (n - 1) * r

print('# Progressão Aritmética')

print('-' * 70)

first_term = int(input('Digite o primeiro termo da PA: '))
ratio = int(input('Digite a razão da PA: '))

print('-' * 70)

current_term = first_term
count = 1
terms_amount = 10

while count <= terms_amount:
    print(f'{current_term}', end='')
    print(' - ' if count < terms_amount else '', end='')

    current_term += ratio
    count += 1

print() # Quebre de linha para as próximas impressos no terminal