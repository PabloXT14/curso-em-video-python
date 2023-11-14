# Exercício 19 (Aula 008)

# Descrição: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 

# Resolução
import random

print('Sorteando um item na lista')

print('-' * 40)

students = []

while True:
    current_name = input("Digite o nome do aluno (ou 'parar' para encerrar): ")

    if current_name.lower() == 'parar':
        break

    students.append(current_name)

chosen_student = random.choice(students)

print(f'Aluno sorteado: {chosen_student}')
print('-' * 40)
