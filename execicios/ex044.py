# Exercício 44 - Gerenciador de Pagamentos (Aula 012)

'''
# Descrição:

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até duas vezes no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros. 
'''

# Resolução:

print('# Gerenciador de Pagamentos')

print('-' * 70)

product_price = float(input('Digite o valor do produto (em R$): '))

print('-' * 70)

payment_option = 0

while True:
    payment_option = int(input("Escolha a forma de pagamento:\n"
                               "1 - À vista dinheiro/cheque(10% de desconto)\n"
                               "2 - À vista no cartão (5% de desconto)\n"
                               "3 - Em até duas vezes no cartão (preço normal)\n"
                               "4 - 3x ou mais no cartão (20% de juros)\n"
                               "Digite o número correspondente à forma de pagamento: "))

    print('-' * 70)

    if (payment_option == 1) or (payment_option == 2) or (payment_option == 3) or (payment_option == 4):
        break

final_product_price = product_price

if (payment_option == 1):
    final_product_price = product_price - (product_price * 0.1)
elif (payment_option == 2):
    final_product_price = product_price - (product_price * 0.05)
elif (payment_option == 3):
    final_product_price = product_price
else:
    final_product_price = product_price + (product_price * 0.2)

print(f'* Valor final do produto: {'\033[1;33m'}R$ {final_product_price:.2f}{'\033[m'}')
