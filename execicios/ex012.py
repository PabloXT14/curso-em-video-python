# Exercício 12 (Aula 007)

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Resolução

print('Preço do produto com 5% off')

price = float(input('Digite o preço do produto e ganhe 5% de desconto: '))

percentage_discount = 5 / 100

discount_price = round(price * percentage_discount, 2)

final_price = round(price - discount_price, 2)

print(f'Desconto: R$ {discount_price}')
print(f'Preço final: R$ {final_price}')
