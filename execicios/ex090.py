# Exercício 90 - Dicionário em Python (019)

'''
# Descrição:

Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

# Resolução:

line_length = 70

print('# Dicionário em Python - Média Escola')

print('-' * line_length)

student = {}

student['name'] = str(input('Digite o nome do aluno: '))
student['average'] = float(input('Digite a média do aluno: '))

if student['average'] >= 7:
    student['status'] = 'aprovado'
    student['status_color'] = '\033[1;32m'
elif 5 <= student['average'] < 7:
    student['status'] = 'recuperação'
    student['status_color'] = '\033[1;33m'
else:
    student['status'] = 'reprovado'
    student['status_color'] = '\033[1;31m'

print('-' * line_length)

print(f'* Nome do aluno: {student["name"]}')
print(f'* Média: {student["average"]:.2f}')
print(f'* Situação: {student["status_color"]}{student["status"].upper()}{'\033[m'}')

print('-' * line_length)
