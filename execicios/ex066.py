# Exercício 66 - Vários números com flag (015)

'''
# Descrição:

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''

# Resolução:

print('# Vários números com flag')

print('-' * 70)

stop_flag = 999
count = 0
total_sum = 0

while True:
    number = int(input(f'Digite um número inteiro ({stop_flag} para encerrar): '))

    if (number == stop_flag):
        break

    count += 1
    total_sum += number

print('-' * 70)

print(f'* Quantidade de números digitados: {'\033[1;33m'}{count}{'\033[m'}')
print(f'* Soma total: {'\033[1;33m'}{total_sum}{'\033[m'}')
