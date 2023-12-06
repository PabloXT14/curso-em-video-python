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

purchase_price = float(input('Digite o valor das compras (em R$): '))

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

    if 1 <= payment_option <= 4:
        break
    else:
        print('Escolha inválida. Por favor digite uma das escolhas disponíveis.')

    print('-' * 70)

final_purchase_price = purchase_price
number_of_parcels = 0

if (payment_option == 1):
    final_purchase_price = purchase_price - (purchase_price * 0.1)
elif (payment_option == 2):
    final_purchase_price = purchase_price - (purchase_price * 0.05)
elif (payment_option == 3):
    number_of_parcels = 2
    final_purchase_price = purchase_price
    monthly_parcel = final_purchase_price / number_of_parcels

    print(f'* Sua compra será parcelada em {'\033[1;33m'}{number_of_parcels}x de R$ {monthly_parcel:.2f} (sem juros){'\033[m'}')
elif (payment_option == 4):
    number_of_parcels = int(input('Quantas parcelas: '))

    print('-' * 70)

    final_purchase_price = purchase_price + (purchase_price * 0.2)
    monthly_parcel = final_purchase_price / number_of_parcels

    print(f'* Sua compra será parcelada em {'\033[1;33m'}{number_of_parcels}x de R$ {monthly_parcel:.2f} (com juros){'\033[m'}')

print(f'* Valor final das compras: {'\033[1;33m'}R$ {final_purchase_price:.2f}{'\033[m'}')
