# Exercício 17 (Aula 008)

# Descrição: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

# Resolução
import math

print('Catetos e Hipotenusa')

cat_adj = float(input('Digite o valor do cateto adjacente: '))
cat_opo = float(input('Digite o valor do cateto oposto: '))

# Fórmula: hip² = cat² + cat² 
hip = math.sqrt(math.pow(cat_adj, 2) + math.pow(cat_opo, 2))

print('-' * 20)
print(f'Hipotenusa: {hip}')
print('-' * 20)
