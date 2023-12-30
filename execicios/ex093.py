# Exercício 93 - Cadastro de Jogador de Futebol (019)

'''
# Descrição:

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
'''

# Resolução:

line_length = 70

print('# Cadastro de Jogador de Futebol')

print('-' * line_length)

soccer_player = {}

soccer_player['name'] = str(input('Digite o nome do jogador: ')).strip().title()
soccer_player['matches_quantity'] = int(input('Digite a quantidade de partidas jogadas: '))

soccer_player['goals_per_math'] = []

for i in range(0, soccer_player['matches_quantity']):
    goals_amount = int(input(f'Quantidade de gols da {i + 1}ª partida: '))
    soccer_player['goals_per_math'].append(goals_amount)

soccer_player['total_goals'] = sum(soccer_player['goals_per_math'])

print('-' * line_length)

print(f'* Nome do jogador: {'\033[1;33m'}{soccer_player['name']}{'\033[m'}')
print(f'* Quantidade de partidas jogadas: {'\033[1;33m'}{soccer_player['matches_quantity']}{'\033[m'}')
print(f'* Goals por partida:')

for i, match_goals in enumerate(soccer_player['goals_per_math']):
    print(' ' * 4, end='')
    print(f'* {i + 1}ª partida: {'\033[1;33m'}{match_goals} {'gols' if match_goals != 1 else 'gol'} {'\033[m'}')

print(f'* Total de gols: {'\033[1;33m'}{soccer_player["total_goals"]}{'\033[m'}')

print('-' * line_length)
