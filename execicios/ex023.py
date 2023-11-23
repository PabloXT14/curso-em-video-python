# Exercício 23 - Separando digitos de um número (Aula 009)

'''
# Descrição: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834

- Unidade: 4
- Dezena: 3
- Centena: 8
- Milhar: 1
'''

# Resolução:

print('Separando digitos de um número')

print('-' * 80)

while True:
    try:
        number = int(input('Digite um número (de 0 a 9999): '))

        if (number >= 0 and number <= 9999):
            break
    except:
        print('Entrada inválida.')
    
print('-' * 80)

str_number = str(number)
number_digits_amount = len(str_number)

unit = number % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousands = (number // 1000) % 10

print(f'- Unidade: {unit}')
print(f'- Dezena: {ten}')
print(f'- Centena: {hundred}')
print(f'- Milhar: {thousands}')
