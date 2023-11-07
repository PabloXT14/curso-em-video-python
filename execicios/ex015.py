# Exercício 15 (Aula 007)

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Resolução

print('Aluguel de Carros')

price_per_distance_traveled_in_real = 0.15
price_per_rented_day_in_real = 60

rented_days = int(input('Por quantos dias o carro foi alugado?: '))
distance_in_km = float(input('Quantos quilometros(km) o carro percorreu?: '))

total_distance_price = distance_in_km * price_per_distance_traveled_in_real
total_rented_days_price = rented_days * price_per_rented_day_in_real
total_price = total_distance_price + total_rented_days_price

print('-' * 40)
print(f'Valor total por km roda: R$ {total_distance_price:.2f}')
print(f'Valor total por dia alugado: R$ {total_rented_days_price:.2f}')
print(f'Total a pagar: R$ {total_price:.2f}')
print('-' * 40)
