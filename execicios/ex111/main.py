from utilidades_cev import moeda, utils

line_length = 70

utils.header('Transformando módulos em pacotes')

price = float(input('Digite um preço (R$): '))

increase_percentage = 10 # 10%
decrease_percentage = 20 # 20%

print('-' * line_length)

moeda.summary(price, increase_percentage, decrease_percentage)

print('-' * line_length)
