# Exercício 22 - Analisador de Textos (Aula 009)

'''
# Descrição: Crie um programa que leia o nome completo de uma pessoa e mostre:
[x] O nome com todas as letras maiúsculas
[x] O nome com todas as letras minúsculas
[x] Quantas letras ao todo (sem considerar espaços)
[x] Quantas letras têm o primeiro nome 
'''

# Resolução:

print('Analisador de Textos')

print('-' * 80)

full_name = input('Digite seu nome completo: ')

print('-' * 80)

upper_name = full_name.upper()
lower_name = full_name.lower()
total_letters = len(full_name.replace(" ", "")) # outra solução: len(''.join(full_name.split()))

first_name = full_name.split()[0]
first_name_letters_amount = len(first_name)

print(f'Nome em maiúsculas: {upper_name}')
print(f'Nome em minúsculas: {lower_name}')
print(f'Total de letras (sem espaço): {total_letters}')
print(f'Quantidade de letras no 1º nome: {first_name_letters_amount}')
