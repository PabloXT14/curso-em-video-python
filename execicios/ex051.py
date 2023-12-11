# Exercício 51 - Progressão Aritmética (013)

'''
# Descrição:

Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

# Resolução:

# Fórmula PA: An = A1 + (n - 1) * r

print('# Progressão Aritmética')

print('-' * 70)

first_term = int(input('Digite o primeiro termo da PA: '))
ratio = int(input('Digite a razão da PA: '))

print('-' * 70)

print('* 10 primeiros termos da PA:')

# 1ª Solução
'''
for i in range(1, 11):
    current_term = first_term + (i - 1) * ratio

    if (i % 10 != 0):
        print(current_term, end=' - ')
    else:
        print(current_term)
'''

# 2ª Solução
tenth_term = first_term + (10 - 1) * ratio

for i in range(first_term, tenth_term + ratio, ratio):
    if (i != tenth_term):
        print(i, end=' - ')
    else:
        print(i)
