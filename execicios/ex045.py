# Exercício 45 - GAME: Pedra, Papel e Tesoura (Aula 012)

'''
# Descrição:

Crie um programa que faça o computador jogar Jokenpô com você.
'''

# Resolução:

from random import choice

print('# GAME: Pedra, Papel e Tesoura')

# Opções disponíveis para o computador
computer_options = ['Pedra', 'Papel', 'Tesoura']

# Escolha aleatória do computador
computer_choice = choice(computer_options)

print('-' * 70)

# Recebe a escolha do jogador
while True:
    print('Escolha sua opção de jogada:')
    print('1 - 💎 (pedra)')
    print('2 - 📃 (papel)')
    print('3 - ✂ (tesoura)')

    player_choice = int(input('Digite o número correspondente à sua escolha: '))

    print('-' * 70)

    if (player_choice == 1) or (player_choice == 2) or (player_choice == 3):
        break

# Converter a escolha do jogador em texto
choose_player_text = ''

if (player_choice == 1):
    choose_player_text = computer_options[0]
elif (player_choice == 2):
    choose_player_text = computer_options[1]
elif (player_choice == 3):
    choose_player_text = computer_options[2]
else:
    choose_player_text = 'Escolha inválida'

# Exibindo escolhas
print(f'* Você escolher: {choose_player_text}')
print(f'* Computador escolheu: {computer_choice}')

# Determinando vencedor
result = ''

if (choose_player_text == computer_choice):
    result = f'{'\033[1;33m'}Empate!{'\033[m'}'
elif (choose_player_text == 'Pedra' and computer_choice == 'Tesoura') or \
     (choose_player_text == 'Papel' and computer_choice == 'Pedra') or \
     (choose_player_text == 'Tesoura' and computer_choice == 'Papel'):
    result = f'{'\033[1;32m'}Você venceu!{'\033[m'}'
else:
    result = f'{'\033[1;31m'}Você perdeu!{'\033[m'}'

print(f'* {result}')
