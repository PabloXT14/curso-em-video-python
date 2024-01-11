from utilidades_cev import moeda, utils, dado

line_length = 70

utils.header('Transformando módulos em pacotes')

price = dado.read_money('Digite um preço (R$): ')

increase_percentage = 35 # 35%
decrease_percentage = 22 # 22%

print('-' * line_length)

moeda.summary(price, increase_percentage, decrease_percentage)

print('-' * line_length)
