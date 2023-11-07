# Exercício 14 (Aula 007)

# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# Resolução

print('Conversor de Temperatura')

print('Celsius -> Fahrenheit')

celsius_temp = float(input('Digite uma temperatura em °C: '))

fahrenheit_temp = round((celsius_temp * 9/5) + 32, 2)

print('-' * 20)
print(f'{celsius_temp}°C = {fahrenheit_temp}°F')
print('-' * 20)
