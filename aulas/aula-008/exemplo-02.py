from random import random, randint

print('Gerando números aleatórios')

random_num_1 = random() # gera um número randômico entre 0 e 1
random_num_2 = randint(1, 10) # gera um número randômico inteiro entre um intervalo especificado

print(f'1º Número: {random_num_1}')
print(f'2º Número: {random_num_2}')
