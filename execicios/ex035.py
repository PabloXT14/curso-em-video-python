# Exercício 35 - Analisando Triângulo v1.0 (Aula 010)

'''
# Descrição:

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

* Dica: em qualquer triângulo, a soma das medidas de dois lados é sempre maior que a medida do terceiro.
'''

# Resolução:

print('Analisando Triângulo v1.0')

print('-' * 70)

side_1 = float(input('Digite o valor do 1º lado do triângulo: '))
side_2 = float(input('Digite o valor do 2º lado do triângulo: '))
side_3 = float(input('Digite o valor do 3º lado do triângulo: '))

print('-' * 70)

is_triangle = False

if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_3 + side_2 > side_1):
    is_triangle = True

print(f'* Estes valores formam um triângulo: {'Sim' if is_triangle else 'Não'}')