# Exercício 7 (Aula 007)

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# Resolução

print('Cálculo de Média Escolar')

grade1 = int(input('Digite a 1ª nota: '))
grade2 = int(input('Digite a 2ª nota: '))

average_result = round((grade1 + grade2) / 2, 2)

print(f'Média: {average_result}')

# Outra solução
# average_result = (grade1 + grade2) / 2
# average_result_rounded = f'{average_result:.1f}'

# print(f'Média: {average_result_rounded}')
