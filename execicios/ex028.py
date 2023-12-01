# Exercício 28 - Jogo da Adivinhação v1.0 (Aula 010)

'''
# Descrição:

Escreva uma programa que faça o computador "pensar" em um número inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

# Resolução:

from random import randint
from time import sleep

colors = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m'
}

styles = {
    'reset': '\033[m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reverse': '\033[7m'
}

print(f'{colors["yellow"]}{'-' * 70}{styles["reset"]}')

print(f'{colors["blue"]}# Jogo da Adivinhação v1.0{styles["reset"]}')

start_range = 0
end_range = 5

computer_number = randint(start_range, end_range)

print(f'{colors["yellow"]}{'-' * 70}{styles["reset"]}')

user_guess = int(input(f'Estou pensando em um número entre {start_range} e {end_range} tente adivinhar qual é: '))

print('-' * 70)

print(f'{colors["yellow"]}Processando...{styles["reset"]}')
sleep(3)

print('-' * 70)

print(f'* Número sorteado: {computer_number}')

if (user_guess == computer_number):
    print(f'{colors["green"]}* Parabéns! Você acertou o número.{styles["reset"]}')
else:
    print(f'{colors["red"]}* Que pena! Não foi dessa vez, quem sabe da próxima.{styles["reset"]}')
