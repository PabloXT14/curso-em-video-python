# Exercício 13 - Reajuste Salarial (Aula 007)

'''
# Descrição:

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

# Resolução

print('# Reajuste Salarial')

print('Info: aumento de 15% no salário')

wage = float(input('Digite seu salario R$: '))

increase_percentage = 15 / 100

increase_value = round(wage * increase_percentage, 2)

final_wage = round(wage + increase_value, 2)

print('-' * 40)
print(f'Salário antigo: R$ {wage}')
print(f'Valor de aumento: R$ {increase_value}')
print(f'Salário novo: R$ {final_wage}')
print('-' * 40)
