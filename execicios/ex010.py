# Exercício 10 (Aula 007)

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1,00 = R$3,27 

# Resolução

print('Conversão Real -> Dólar | Euro | Iene')

real_money = float(input('Digite quantos reais você tem na carteira, R$'))

real_dollar_exchange_value = 4.89
real_euro_exchange_value = 5.24
real_iene_exchange_value = 0.033

dollar_money = round(real_money / real_dollar_exchange_value, 2)
euro_money = round(real_money / real_euro_exchange_value, 2)
iene_money = round(real_money / real_iene_exchange_value, 2)

print(f'R${real_money} = US${dollar_money}')
print(f'R${real_money} = €{euro_money}')
print(f'R${real_money} = ¥{iene_money}')
