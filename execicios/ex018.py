# Exercício 18 (Aula 008)

# Descrição: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

# Resolução
import math

print('Seno, Cosseno e Tangente')

angle = float(input('Digite o valor de um ângulo: '))

angle_radians = math.radians(angle)

angle_sin = round(math.sin(angle_radians), 2)
angle_cos = round(math.cos(angle_radians), 2)
angle_tan = round(math.tan(angle_radians), 2)

print('-' * 40)
print(f'Seno de {angle}° = {angle_sin}')
print(f'Cosseno de {angle}° = {angle_cos}')
print(f'Tangente de {angle}° = {angle_tan}')
print('-' * 40)