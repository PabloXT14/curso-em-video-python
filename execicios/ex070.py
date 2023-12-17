# Exercício 70 - Estatísticas em produtos (015)

'''
# Descrição:

Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o nome do produto mais barato
'''

# Resolução:
print('-' * 70)

print(f'{' MERCADINHO DO ZÉ ':^70}')

count_products = 0
total_spent = 0
count_products_above_1000 = 0
cheapest_product_price = 0
cheapest_product_name = ''

while True:
    count_products += 1

    print('-' * 70)

    print(f'{'\033[1;32m'}COMPRAR {count_products}º PRODUTO{'\033[m'}')

    print('-' * 70)

    product_name = str(input('Nome: ')).strip().title()
    product_price = float(input('Preço (R$): '))

    print('-' * 70)

    total_spent += product_price

    if product_price > 1000:
        count_products_above_1000 += 1
    
    if (count_products == 1) or (product_price < cheapest_product_price):
        cheapest_product_price = product_price
        cheapest_product_name = product_name

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()

        if answer in 'SN':
            break
    
    if answer == 'N':
        break

print('-' * 70)

print(f'* Quantidade de produtos comprados: {'\033[1;33m'}{count_products}{'\033[m'}')
print(f'* Total gasto na compra: {'\033[1;33m'}R$ {total_spent:.2f}{'\033[m'}')
print(f'* Quantidade de produtos acima de R$ 1000,00: {'\033[1;33m'}{count_products_above_1000}{'\033[m'}')
print(f'* Produto mais barato: {'\033[1;33m'}{cheapest_product_name} (R$ {cheapest_product_price:.2f}){'\033[m'}')
