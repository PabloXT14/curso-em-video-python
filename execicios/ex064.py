# Exercício 64 - Tratando vários valores v1.0 (014)

'''
# Descrição:

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag 999)
'''

# Resolução:

print('# Tratando vários valores v1.0')

print('-' * 70)

stop_flag = 999
count_numbers = 0
total_sum = 0

number = int(input('Digite um número inteiro (999 para encerrar): '))

print('-' * 70)

while number != stop_flag:
    count_numbers += 1
    total_sum += number

    number = int(input('Digite um número inteiro (999 para encerrar): '))

    print('-' * 70)

print(f'* Quantidade de números digitados: {'\033[1;33m'}{count_numbers}{'\033[m'}')
print(f'* Soma dos números digitados: {'\033[1;33m'}{total_sum}{'\033[m'}')
