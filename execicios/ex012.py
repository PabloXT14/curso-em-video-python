# Exercício 12 - Calculando Descontos (Aula 007)

'''
# Descrição:

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

# Resolução

print('# Calculando Desconto')

print('Info: produtos com 5% off')

price = float(input('Digite o preço do produto R$ '))

percentage_discount = 5 / 100

discount_price = round(price * percentage_discount, 2)

final_price = round(price - discount_price, 2)

print('-' * 40)
print(f'Preço sem desconto: R$ {price}')
print(f'Desconto: R$ {discount_price}')
print(f'Preço final: R$ {final_price}')
print('-' * 40)
