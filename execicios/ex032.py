# Exercício 32 - Ano Bissexto (Aula 010)

'''
# Descrição:

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

* Dica: Um ano bissexto é aquele que é divisível por 4, mas não por 100, a menos que seja divisível por 400

'''

# Resolução:

print('# Ano Bissexto')

print('-' * 70)

year = int(input('Digite o ano: '))

print('-' * 70)

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if (is_leap_year):
    print(f'O ano {year} é bissexto.')
else:
    print(f'O ano {year} não é bissexto.')
