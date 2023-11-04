# Exercício 8 (Aula 007)

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

# Resolução

print('Conversor de metros em centímetros e milímetros')

meters_value = int(input('Digite um valor em metros: '))

centimeters_value = meters_value * 100

millimeters_value = meters_value * 1000

print(f'Valor em metros: {meters_value}m')
print(f'Valor em centímetros: {centimeters_value}cm')
print(f'Valor em milímetros: {millimeters_value}mm')
