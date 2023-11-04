# Exercício 11 (Aula 007)

# Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².

# Resolução

print('Calculo de tinta para pintar a parede')

print('Info: 1L de tinta pinta 2m²')

height = float(input('Digite a altura da parede (em metros): '))
width = float(input('Digite a largura da parede (em metros): '))

wall_area = height * width

base_area_per_liter_of_paint = 2

paint_liters_needed = round(wall_area / base_area_per_liter_of_paint, 2) 

print(f'Será necessário {paint_liters_needed}L de tinta para pintar essa parede.')
