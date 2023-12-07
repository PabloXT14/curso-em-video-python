# Exercício 18 - Seno, Cosseno e Tangente (Aula 008)

'''
# Descrição:

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

# Resolução
from math import sin, cos, tan, radians

print('# Seno, Cosseno e Tangente')

print('-' * 40)

angle = float(input('Digite o valor de um ângulo: '))

angle_radians = radians(angle)

angle_sin = round(sin(angle_radians), 2)
angle_cos = round(cos(angle_radians), 2)
angle_tan = round(tan(angle_radians), 2)

print('-' * 40)
print(f'Seno de {angle}° = {angle_sin}')
print(f'Cosseno de {angle}° = {angle_cos}')
print(f'Tangente de {angle}° = {angle_tan}')
print('-' * 40)
