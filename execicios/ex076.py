# Exercício 76 - Lista de Preços com Tupla (016)

'''
# Descrição:

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

# Resolução:

# 1ª Solução
line_length = 70

print('=' * line_length)

print(f'{'\033[1;33m'}{'LISTAGEM DE PREÇOS':^{line_length}}{'\033[m'}')

print('=' * line_length)

products = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

for i, product in enumerate(products):
    if i % 2 == 0:
        product_name = product
        print(f'{product_name:.<{line_length - 10}}', end=' ')
    else:
        product_price = product
        print(f'{'\033[1;33m'}R$ {product_price:>6.2f}{'\033[m'}')

print('=' * line_length)

# 2ª Solução
'''
# Criar uma tupla com nomes de produtos e preços
produtos_precos = (
    ("Produto1", 19.99),
    ("Produto2", 29.99),
    ("Produto3", 14.99),
    ("Produto4", 24.99),
    ("Produto5", 9.99)
)

# Mostrar uma listagem de preços organizada em forma tabular
print("{:<15} {:<10}".format("Produto", "Preço"))
print("-" * 25)

for produto, preco in produtos_precos:
    print("{:<15} R$ {:<10.2f}".format(produto, preco))
'''
