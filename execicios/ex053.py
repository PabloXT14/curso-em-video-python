# Exercício 53 - Detector de Palíndromo (013)

'''
# Descrição:

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

# Resolução:

print('# Detector de Palíndromo')

print('-' * 70)

phrase = str(input('Digite uma frase: '))

phrase_without_space = phrase.replace(' ', '').lower()

print('-' * 70)

# 1ª Solução
'''
is_palindrome = True

phrase_length = len(phrase_without_space)

for i in range(0, phrase_length):
    if (phrase_without_space[i] != phrase_without_space[phrase_length - i - 1]):
        is_palindrome = False
        break

if (is_palindrome):
    print(f'{'\033[1;32m'}* A frase é um palíndromo. {'\033[m'}')
else:
    print(f'{'\033[1;31m'}* A frase não é um palíndromo. {'\033[m'}')
'''

# 2ª Solução

is_palindrome = phrase_without_space == phrase_without_space[::-1] # o -1 neste caso indica indo de de 1 em 1 começam do fim da phrase

if (is_palindrome):
    print(f'{'\033[1;32m'}* A frase é um palíndromo. {'\033[m'}')
else:
    print(f'{'\033[1;31m'}* A frase não é um palíndromo. {'\033[m'}')
