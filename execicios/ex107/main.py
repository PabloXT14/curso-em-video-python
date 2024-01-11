import utils
from moeda import half, double, increase, decrease

line_length = 70

utils.header('Exercitando Módulos em Python')

price = float(input('Digite um preço (R$): '))

increase_percentage = 10 # 10%
decrease_percentage = 20 # 20%

print('-' * line_length)

print(f'* Metade de R${price:.2f}: {'\033[1;33m'}R${half(price):.2f}{'\033[m'}')
print(f'* Dobro de R${price:.2f}: {'\033[1;33m'}R${double(price):.2f}{'\033[m'}')
print(f'* Aumentando {increase_percentage}% (em R${price:.2f}) temos: {'\033[1;33m'}R${increase(price, increase_percentage):.2f}{'\033[m'}')
print(f'* Diminuindo {decrease_percentage}% (em R${price:.2f}) temos: {'\033[1;33m'}R${decrease(price, increase_percentage):.2f}{'\033[m'}')

print('-' * line_length)
