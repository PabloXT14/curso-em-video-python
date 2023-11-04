# Exercício 10 (Aula 007)

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1,00 = R$3,27 

# Resolução

print('Conversão Real -> Dólar')

real_money = float(input('Digite um valor em reais (ex: 6.54): '))

dollar_real_exchange_value = 3.27

dollar_money = round(real_money / dollar_real_exchange_value, 2)

print(f'R${real_money} == US${dollar_money}')
