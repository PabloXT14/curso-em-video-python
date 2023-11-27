# Exercício 29 - Radar Eletronico (Aula 010)

'''
# Descrição:

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

# Resolução:

print('# Radar Eletronico')

print('-' * 70)

car_speed = float(input('A qual velocidade o carro estava (Km/h): '))

print('-' * 70)

limit_speed = 80

is_above_speed_limit = car_speed > limit_speed

fine_per_kilometer = 7

if (is_above_speed_limit):
    speed_exceeded = round(car_speed - limit_speed)

    fine_value = fine_per_kilometer * speed_exceeded

    print('* Você ultrapassou o limite de 80km/h e foi MULTADO!')
    print(f'* Quilometros excedidos: {speed_exceeded}(Km/h)')
    print(f'* Valor da multa: R$ {fine_value:.2f}')
else:
    print('* Você está dentro do limite de velocidade (80Km/h). Dirija com segurança')
