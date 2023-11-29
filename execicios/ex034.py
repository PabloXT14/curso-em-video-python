# Exercício 34 - Aumentos multiplos (Aula 010)

'''
# Descrição:

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

Para inferiores ou iguais, o aumento é de 15%.
'''

# Resolução:

print('Aumentos multiplos')

print('-' * 70)

wage = float(input('Digite seu salário (R$): '))

print('-' * 70)

primary_salary_increase = 10/100
secondary_salary_increase = 15/100

fits_the_primary_increase = wage > 1250

new_wage = 0
increase_value = 0

if (fits_the_primary_increase):
    increase_value = wage * primary_salary_increase
    new_wage = wage + increase_value
else:
    increase_value = wage * secondary_salary_increase
    new_wage = wage + increase_value

print(f'* Antigo salário: R$ {wage:.2f}')
print(f'* Valor de aumento: R$ {increase_value:.2f}')
print(f'* Novo salário: R$ {new_wage:.2f}')
