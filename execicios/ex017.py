# Exercício 17 (Aula 008)

# Descrição: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

# Resolução
import math

print('Catetos e Hipotenusa')

print('-' * 40)

cat_adj = float(input('Digite o valor do cateto adjacente: '))
cat_opo = float(input('Digite o valor do cateto oposto: '))

# Fórmula: hip² = cat² + cat² 

# 1ª Solução
hip = math.hypot(cat_adj, cat_opo)

print('-' * 40)
print(f'Hipotenusa: {hip:.2f}')

# 2ª Solução
'''
hip = math.sqrt(math.pow(cat_adj, 2) + math.pow(cat_opo, 2))

print('-' * 40)
print(f'Hipotenusa: {hip:.2f}')
'''

# 3ª Solução
'''
hip = (cat_opo ** 2 + cat_adj ** 2) ** (1/2)

print('-' * 40)
print(f'Hipotenusa: {hip:.2f}')
'''
