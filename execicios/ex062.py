# Exercício 62 - Super Progressão Aritmética v3.0 (014)

'''
# Descrição:

Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''

# Resolução:

print('# Super Progressão Aritmética v3.0')

print('-' * 70)

first_term = int(input('Digite o primeiro termo da PA: '))
ratio = int(input('Digite a razão da PA: '))

print('-' * 70)

current_term = first_term
count = 1
terms_amount = 10
more_terms = True

while more_terms:
    if (count < terms_amount):
        print(f'{current_term}', end=' - ')
    else:
        print(f'{current_term}')

    current_term += ratio
    count += 1

    if (count > terms_amount):
        print('-' * 70)

        answer = int(input('Quer mostrar mais termos? Digite a quantidade (0 para encerrar): '))

        if (answer > 0):
            terms_amount += answer
        else:
            more_terms = False
        
        print('-' * 70)

print(f'* Total de termos mostrados: {'\033[1;33m'}{terms_amount}{'\033[m'}')
