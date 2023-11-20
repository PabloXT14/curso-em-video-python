# Exercício 20 (Aula 008)

# Descrição: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

# Resolução

from random import sample, shuffle

print('Sorteando uma ordem na lista')

print('-' * 80)

students = []

while True:
    current_name = input("Digite o nome do aluno (ou 'parar' para encerrar): ")

    if current_name.lower() == 'parar':
        break

    students.append(current_name)

# 1ª Solução

students_reorganized = sample(students, len(students)) # Cria uma nova lista reorganizada de forma aleatória

print('-' * 80)

print('Ordem de apresentação:')

for index, student in enumerate(students_reorganized):
    print(f'{index + 1}º {student}')

print('-' * 80)

# 2ª Solução
'''
shuffle(students) # Reorganiza uma lista já existente de forma aleatória

print('-' * 80)

print('Ordem de apresentação:')

for index, student in enumerate(students):
    print(f'{index + 1}º {student}')

print('-' * 80)
'''
