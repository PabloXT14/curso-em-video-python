# Exercício 40 - Aquele clássico da Média (Aula 012)

'''
# Descrição:

Crie um programa que leia duas notas de um aluno e calcule sue média, mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

'''

# Resolução:

print('# Média Escolar')

print('-' * 70)

garde_1 = float(input('Digite a 1ª nota: '))
grade_2 = float(input('Digite a 2ª nota: '))

print('-' * 70)

average = round((garde_1 + grade_2) / 2, 1)

print(f'* Média final: {'\033[1;33m'}{average}{'\033[m'}')

if (average < 5.0):
    print(f'* Situação: {'\033[1;31m'}REPROVADO{'\033[m'}')
elif (5.0 <= average <= 6.9):
    print(f'* Situação: {'\033[1;33m'}RECUPERAÇÃO{'\033[m'}')
else:
    print(f'* Situação: {'\033[1;32m'}APROVADO{'\033[m'}')
