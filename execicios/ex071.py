# Exercício 71 - Simulador de caixa eletronico (015)

'''
# Descrição:

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa irá informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
'''

# Resolução:
print('=' * 70)

print(f'{'BANCO DEV':^70}')

print('=' * 70)

withdrawal_amount = int(input('Digite o valor inteiro de quanto deseja sacar (R$): '))

print('=' * 70)

bills_50 = bills_20 = bills_10 = bills_1 = 0


# 1ª Solução
while True:
    if (withdrawal_amount >= 50):
        withdrawal_amount -= 50
        bills_50 += 1
    elif (withdrawal_amount >= 20):
        withdrawal_amount -= 20
        bills_20 += 1
    elif (withdrawal_amount >= 10):
        withdrawal_amount -= 10
        bills_10 += 1
    elif (withdrawal_amount >= 1):
        withdrawal_amount -= 1
        bills_1 += 1
    else:
        break

print('* Quantidade de cédulas:')

if bills_50 > 0:
    print(f'* Cédulas de R$ 50: {'\033[1;33m'}{bills_50}{'\033[m'}')

if bills_20 > 0:
    print(f'* Cédulas de R$ 20: {'\033[1;33m'}{bills_20}{'\033[m'}')

if bills_10 > 0:
    print(f'* Cédulas de R$ 10: {'\033[1;33m'}{bills_10}{'\033[m'}')

if bills_1 > 0:
    print(f'* Cédulas de R$ 1: {'\033[1;33m'}{bills_1}{'\033[m'}')


# 2ª Solução
'''
print('* Quantidade de cédulas:')

if (withdrawal_amount >= 50):
    bills_50 = withdrawal_amount // 50
    withdrawal_amount %= 50
    print(f'* Cédulas de R$ 50: {'\033[1;33m'}{bills_50}{'\033[m'}')

if (withdrawal_amount >= 20):
    bills_20 = withdrawal_amount // 20
    withdrawal_amount %= 20
    print(f'* Cédulas de R$ 20: {'\033[1;33m'}{bills_20}{'\033[m'}')

if (withdrawal_amount >= 10):
    bills_10 = withdrawal_amount // 10
    withdrawal_amount %= 10
    print(f'* Cédulas de R$ 10: {'\033[1;33m'}{bills_10}{'\033[m'}')

if (withdrawal_amount >= 1):
    bills_1 = withdrawal_amount // 1
    withdrawal_amount %= 1
    print(f'* Cédulas de R$ 1: {'\033[1;33m'}{bills_1}{'\033[m'}')
'''

print('=' * 70)

print('Volte sempre ao BANCO DEV! Tenha um bom dia!')