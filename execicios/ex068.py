# Exercício 68 - Jogo do Par ou Ímpar (015)

'''
# Descrição:

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

# Resolução:

from random import randint

print('# Jogo do Par ou Ímpar')

winning_record = 0

print('-' * 70)

while True:
    player_number = int(input('Digite um número inteiro: '))

    print('-' * 70)

    while True:
        player_choice = str(input('Escolha par (P) ou ímpar (I): ')).strip().upper()

        if (player_choice == 'P' or player_choice == 'I'):
            break

    print('-' * 70)

    computer_number = randint(1, 10)

    result = player_number + computer_number
    is_even = result % 2 == 0

    if (is_even and player_choice == 'P') or (is_even == False and player_choice == 'I'):
        print(f'{'\033[1;32m'}* PARABÉNS VOCÊ GANHOU!{'\033[m'}')
        print(f'* Você jogou {player_number} e o computador {computer_number} = {result} ({'PAR' if is_even else 'ÍMPAR'})')
    else:
        print(f'{'\033[1;31m'}* QUE PENA, VOCÊ PERDEU!{'\033[m'}')
        print(f'* Você jogou {player_number} e o computador {computer_number} = {result} ({'PAR' if is_even else 'ÍMPAR'})')
        break
    
    winning_record += 1
    print('-' * 70)

print('-' * 70)

print(f'* Total de vitórias consecutivas: {'\033[1;33m'}{winning_record}{'\033[m'}')
