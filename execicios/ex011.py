# Exercício 11 - Pintando Parede (Aula 007)

'''
# Descrição:

Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

# Resolução

print('# Pintando Parede')

print('Info: 1L da nossa tinta pinta 2m²')

width = float(input('Digite a largura da parede (em metros): '))
height = float(input('Digite a altura da parede (em metros): '))

wall_area = height * width

base_area_per_liter_of_paint = 2

paint_liters_needed = round(wall_area / base_area_per_liter_of_paint, 2) 

print('-' * 40)
print(f'* Dimensões da parede: {width}m x {height}')
print(f'* Área da parede: {wall_area}m²')
print(f'* Litros de tinta necessários: {paint_liters_needed}L')
print('-' * 40)
