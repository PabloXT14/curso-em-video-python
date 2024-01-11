import utils
from moeda import half, double, increase, decrease, currency

line_length = 70

utils.header('Formatando Moedas em Python (v2.0)')

price = float(input('Digite um preço (R$): '))

increase_percentage = 10 # 10%
decrease_percentage = 20 # 20%

print('-' * line_length)

print(f'* Metade de {currency(price)}: {'\033[1;33m'}{half(price, price_format=True)}{'\033[m'}')
print(f'* Dobro de {currency(price)}: {'\033[1;33m'}{double(price, price_format=True)}{'\033[m'}')
print(f'* Aumentando {increase_percentage}% (em {currency(price)}) temos: {'\033[1;33m'}{increase(price, increase_percentage, price_format=True)}{'\033[m'}')
print(f'* Diminuindo {decrease_percentage}% (em {currency(price)}) temos: {'\033[1;33m'}{decrease(price, increase_percentage, price_format=True)}{'\033[m'}')

print('-' * line_length)
