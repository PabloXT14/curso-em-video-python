# Exercício 38 - Comparando números  (Aula 012)

'''
# Descrição: 

Escreva um programa que leia 'dois números' inteiros e compare-os, mostrando na tela uma mensagem:

- O 'primeiro valor' é 'maior'
- O 'segundo valor' é 'maior'
- 'Não existe' valor maior, os dois são 'iguais' 
'''

# Resolução:

print('# Comparando números')

print('-' * 70)

number1 = int(input('Digite o 1º valor inteiro: '))
number2 = int(input('Digite o 2º valor inteiro: '))

print('-' * 70)

if (number1 > number2):
    print(f'* O {'\033[1;33m'}primeiro valor{'\033[m'} ({number1}) é {'\033[1;33m'}maior{'\033[m'}.')
elif (number2 > number1):
    print(f'* O {'\033[1;33m'}segundo valor{'\033[m'} ({number2}) é {'\033[1;33m'}maior{'\033[m'}.')
else:
    print(f'{'\033[1;33m'}Não existe{'\033[m'} valor {'\033[1;33m'}maior{'\033[m'}, os dois são {'\033[1;33m'}iguais{'\033[m'}.')
