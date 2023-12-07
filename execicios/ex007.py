# Exercício 7 - Média Aritmética (Aula 007)

'''
# Descrição:

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

# Resolução

print('Cálculo de Média Escolar')

grade1 = float(input('Digite a 1ª nota: '))
grade2 = float(input('Digite a 2ª nota: '))

average_result = round((grade1 + grade2) / 2, 1)

print(f'Média: {average_result}')

# Outra solução
# average_result = (grade1 + grade2) / 2
# average_result_rounded = f'{average_result:.1f}'

# print(f'Média: {average_result_rounded}')
