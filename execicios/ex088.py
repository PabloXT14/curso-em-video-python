# Exercício 88 - Palpites para a Mega Sena (018)

'''
# Descrição:

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 
'''

# Resolução:

from random import randint
from time import sleep

line_length = 70

print('-' * line_length)

print(f'{'\033[1;32m'}{'MEGA SENA':^{line_length}}{'\033[m'}')

print('-' * line_length)

amount_of_games_guesses = int(input('Digite quantos jogos deseja gerar: '))

numbers_per_game = 6
start_random_range = 1
stop_random_range = 60

game_guesses_list = []

print('-' * line_length)

print(f'{'\033[1;32m'}{'SORTEANDO JOGOS':^{line_length}}{'\033[m'}')

print('-' * line_length)

for i in range(0, amount_of_games_guesses):
    game_guesses_list.append([])

    for j in range(0, numbers_per_game):
        random_number = randint(start_random_range, stop_random_range)

        while random_number in game_guesses_list[i]:
            random_number = randint(start_random_range, stop_random_range)

        game_guesses_list[i].append(random_number)
    
    sleep(1)
    game_guesses_list[i].sort()
    print(f'* Jogo {i + 1} - {'\033[1;33m'}{game_guesses_list[i]}{'\033[m'}')

print('-' * line_length)

print(f'{'\033[1;32m'}{'BOA SORTE!':^{line_length}}{'\033[m'}')

print('-' * line_length)
