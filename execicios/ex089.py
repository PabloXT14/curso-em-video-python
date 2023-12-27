# Exercício 89 - Boletim com listas compostas (018)

'''
# Descrição:

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

# Resolução:

line_length = 70

print('-' * line_length)

print(f'{'\033[1;33m'}{'BOLETIM ESCOLAR':^{line_length}}{'\033[m'}')

count_students = 0
student_index = 0
students_list = []

# Cadastrando Estudantes
while True:
    count_students += 1

    print('-' * line_length)

    print(f'{'\033[1;33m'}{f'{count_students}º ALUNO':^{line_length}}{'\033[m'}')

    print('-' * line_length)

    name = str(input('Nome: '))
    grade1 = float(input('1ª Nota: '))
    grade2 = float(input('2ª Nota: '))

    students_list.append([name, [grade1, grade2]])

    print('-' * line_length)

    while True:
        can_continue = str(input('Deseja cadastras mas um aluno? (S/N): ')).strip().upper()

        if can_continue == 'S' or can_continue == 'N':
            break
    
    if can_continue == 'N':
        break

print('-' * line_length)

# Imprimindo Tabela de Médias
print(f'{'Nº':<{int(line_length * 1/5)}}', end='')
print(f'{'NOME':<{int(line_length * 3/5)}}', end='')
print(f'{'MÉDIA':<{int(line_length * 1/5)}}')

print('-' * line_length)

for i, student in enumerate(students_list):
    name = student[0]
    grade1 = student[1][0]
    grade2 = student[1][1]

    average = round((grade1 + grade2) / 2, 1)

    color_status = ''

    if average >= 7:
        color_status = '\033[1;32m'
    elif 5 <= average < 7:
        color_status = '\033[1;33m'
    else:
        color_status = '\033[1;31m' 

    print(f'{i:<{int(line_length * 1/5)}}', end='')
    print(f'{name:<{int(line_length * 3/5)}}', end='')
    print(f'{color_status}{average:<{int(line_length * 1/5)}}{'\033[m'}')

print('-' * line_length)

stop_flag = 999

# Mostrando Informações de um aluno específico
while True:
    student_number = int(input(f'Mostrar notas de qual aluno? ({stop_flag} interrompe): '))

    if student_number == stop_flag:
        print('-' * line_length)
        break

    if 0 <= student_number < len(students_list):
        name = students_list[student_number][0]
        grade1 = students_list[student_number][1][0]
        grade2 = students_list[student_number][1][1]

        print(f'* Nome: {'\033[1;33m'}{name}{'\033[m'}')
        print(f'* 1ª Nota: {'\033[1;33m'}{grade1}{'\033[m'}')
        print(f'* 2ª Nota: {'\033[1;33m'}{grade2}{'\033[m'}')
    else:
        print('-' * line_length)

        print(f'{'\033[1;31m'}Entrada inválida! Por favor, digite um código existente.{'\033[m'}')
    
    print('-' * line_length)
