# Exercício 8 (Aula 007)

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros (e se quiser converta para as outras unidades de medidas de distâncias mais comuns).

# Resolução

print('Conversor de metros em centímetros e milímetros')

meters_value = round(float(input('Digite um valor em metros: '))) # round() sem um segundo parâmetro faz com que o valor passado não tenha casas depois da virgula

kilometer_value = meters_value / 1000
hectometer_value = meters_value / 100
decameter_value = meters_value / 10
# meter_value
decimeter_value = meters_value * 10
centimeters_value = meters_value * 100
millimeters_value = meters_value * 1000

print(f'Valor em quilometros: {kilometer_value}km')
print(f'Valor em hectometros: {hectometer_value}hm')
print(f'Valor em milímetros: {decameter_value}dam')
print(f'Valor em metros: {meters_value}m')
print(f'Valor em decímetros: {decimeter_value}dm')
print(f'Valor em centímetros: {centimeters_value}cm')
print(f'Valor em milímetros: {millimeters_value}')
