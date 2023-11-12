# Exercício 16 (Aula 008)

# Descrição: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 -> O número 6.127 tem a parte inteira 6. 

# Resolução
import math

print('Quebrando um número')

number = float(input('Digite um número inteiro qualquer: '))

decimal_part, integer_part = math.modf(number) 

print('-' * 20)
print(f'Parte inteira: {integer_part}')
print(f'Parte decimal: {round(decimal_part, 2)}')
print('-' * 20)
