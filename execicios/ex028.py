# Exercício 28 - Jogo da Adivinhação v1.0 (Aula 010)

'''
# Descrição:

Escreva uma programa que faça o computador "pensar" em um número inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

# Resolução:

from random import randint

print('Jogo da Adivinhação v1.0')

start_range = 0
end_range = 5

computer_number = randint(start_range, end_range)

print('-' * 70)

user_guess = int(input(f'Tente adivinhar o número entre {start_range} e {end_range}: '))

print('-' * 70)

print(f'Número sorteado: {computer_number}')

if (user_guess == computer_number):
    print('Parabéns! Você acertou o número.')
else:
    print('Que pena! Não foi dessa vez, quem sabe da próxima.')
