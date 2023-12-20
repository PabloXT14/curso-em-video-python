# Exercício 77 - Contando Vogais em Tupla (016)

'''
# Descrição:

Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

# Resolução:

line_length = 70

print('=' * line_length)

print(f'{'CONTANDO VOGAIS EM TUPLA':^{line_length}}')

print('=' * line_length)

words = (
    'aprender',
    'programar',
    'linguagem',
    'python',
    'gratis',
    'estudar',
    'praticar',
    'trabalhar',
    'mercado',
    'programador',
    'futuro'
)

print(f'{'PALAVRA':<{int(line_length / 2)}}{'VOGAIS':<{int(line_length / 2)}}')

print('-' * line_length)

# Iterando palavras da tupla
for word in words:
    print(f'{word.capitalize():<{int(line_length / 2)}}', end='')

    # Iterando as letras da palavra
    for letter in word.lower():
        # Imprimindo somente as letras que são vogais
        if (letter in 'aeiou'):
            print(letter, end=' ')

    print() # Quebra de linha

print('-' * 70)
