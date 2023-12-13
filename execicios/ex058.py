# Exercício 58 - Jogo da Adivinhação (014)

'''
# Descrição:

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

# Resolução:

from random import randint
from time import sleep

print(f'{'\033[1;33m'}# Jogo da Adivinhação{'\033[m'}')

print('-' * 70)

start_range = 0
end_range = 10

computer_number = randint(start_range, end_range)
user_guess = end_range + 1

count_guesses = 0
user_guessed_right = False

while not user_guessed_right:
    user_guess = int(input(f'Estou pensando em um número entre {start_range} e {end_range}, tente adivinhar qual é: '))

    count_guesses += 1

    print('-' * 70)

    print(f'{'\033[1;33m'}Processando...{'\033[m'}')
    sleep(2)

    print('-' * 70)

    if (user_guess != computer_number):
        print(f'{'\033[1;31m'}* Que pena! Este não foi o número sorteado, tente outra vez.{'\033[m'}')
    
        print('-' * 70)
    else:
        user_guessed_right = True

print(f'{'\033[1;32m'}* Parabéns! Você acertou o número.{'\033[m'}')
print(f'* Número sorteado: {'\033[1;33m'}{computer_number}{'\033[m'}')
print(f'* Número de palpites: {'\033[1;33m'}{count_guesses}{'\033[m'}')
