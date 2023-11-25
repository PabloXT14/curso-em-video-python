# Exercício 26 - Primeira e última ocorrência de uma string (Aula 009)

'''
# Descrição: Faça um programa que leia uma frase pelo teclado e mostre:
[x] Quantas vezes aparece a letra 'A'
[x] Em que posição ela aparece a primeira vez.
[x] Em que posição ela aparece a última vez.
'''

# Resolução:

print('Primeira e última ocorrência de uma string')

print('-' * 80)

phrase = str(input('Digite uma frase: ')).strip().lower()

print('-' * 80)

count_a_letter = phrase.count('a')

if (count_a_letter > 0):
    # somamos um pois as posições começam em 0
    first_appearance_letter_a = phrase.find('a') + 1 
    last_appearance_letter_a = phrase.rfind('a') + 1

    print(f"Quantidade de vezes que aparece a letra 'A': {count_a_letter}")
    print(f'Posição em que ela aparece a primeira vez: {first_appearance_letter_a}')
    print(f'Posição em que ela aparece a última vez: {last_appearance_letter_a}')
else:
    print(f"Quantidade de vezes que aparece a letra 'A': {count_a_letter}")
