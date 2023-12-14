# Exercício 65 - Maior e Menor valores (014)

'''
# Descrição:

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a 'média entre todos' os valores e qual foi o 'maior' e o 'menor' valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

# Resolução:

print('# Maior e Menores valores')

print('-' * 70)

count_numbers = 0
total_sum = 0

get_more_numbers = 'S'

while get_more_numbers == 'S':
    number = int(input('Digite um número inteiro: '))

    count_numbers += 1
    total_sum += number

    if (count_numbers == 1):
        higher_value = number
        lower_value = number
    
    if (number > higher_value):
        higher_value = number
    elif (number < lower_value):
        lower_value = number

    get_more_numbers = str(input('Deseja continuar digitando números? (S/N): ')).strip().upper()

    print('-' * 70)

average_values = total_sum / count_numbers

print(f'* Média: {'\033[1;33m'}{average_values:.1f}{'\033[m'}')
print(f'* Maior valor: {'\033[1;33m'}{higher_value}{'\033[m'}')
print(f'* Menor valor: {'\033[1;33m'}{lower_value}{'\033[m'}')
