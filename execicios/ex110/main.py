import utils
from moeda import summary

line_length = 70

utils.header('Reduzindo ainda mais o programa')

price = float(input('Digite um preço (R$): '))

increase_percentage = 10 # 10%
decrease_percentage = 20 # 20%

print('-' * line_length)

summary(price, increase_percentage, decrease_percentage)

print('-' * line_length)
