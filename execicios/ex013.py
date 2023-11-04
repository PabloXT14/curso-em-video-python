# Exercício 13 (Aula 007)

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Resolução

print('Promoção Salarial (+15%)')

wage = float(input('Digite seu salario: '))

increase_percentage = 15 / 100

increase_value = round(wage * increase_percentage, 2)

final_wage = round(wage + increase_value, 2)

print(f'Valor de aumento: R$ {increase_value}')
print(f'Salário final: R$ {final_wage}')
