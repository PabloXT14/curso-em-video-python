import utils
from moeda import half, double, increase, decrease, currency

line_length = 70

utils.header('Exercitando Módulos em Python')

price = float(input('Digite um preço (R$): '))

increase_percentage = 10 # 10%
decrease_percentage = 20 # 20%

print('-' * line_length)

print(f'* Metade de {currency(price)}: {'\033[1;33m'}{currency(half(price))}{'\033[m'}')
print(f'* Dobro de {currency(price)}: {'\033[1;33m'}{currency(double(price))}{'\033[m'}')
print(f'* Aumentando {increase_percentage}% (em {currency(price)}) temos: {'\033[1;33m'}{currency(increase(price, increase_percentage))}{'\033[m'}')
print(f'* Diminuindo {decrease_percentage}% (em {currency(price)}) temos: {'\033[1;33m'}{currency(decrease(price, increase_percentage))}{'\033[m'}')

print('-' * line_length)
