# Exercício 95 - Aprimorando os Dicionários (019)

'''
# Descrição:

Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

# Resolução:

line_length = 70

print('# Aprimorando os Dicionários')

players = []
current_player = {}

# Pegando dados dos jogadores
while True:
    print('-' * line_length)

    print(f'{'\033[1;32m'}{f'{len(players) + 1}º JOGADOR':^{line_length}}{'\033[m'}')

    print('-' * line_length)

    current_player['name'] = str(input('Digite o nome do jogador: ')).strip().title()
    current_player['matches_quantity'] = int(input('Digite a quantidade de partidas jogadas: '))

    current_player['goals_per_match'] = []

    print('Digite a quantidade de gols por partida:')

    for i in range(0, current_player['matches_quantity']):
        print(' ' * 4, end='') # Espaçamento

        goals_amount = int(input(f'{i + 1}ª partida: '))
        current_player['goals_per_match'].append(goals_amount)
    
    current_player['total_goals'] = sum(current_player['goals_per_match'])

    players.append(current_player.copy())
    current_player.clear()

    while True:
        print('-' * line_length)
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()
        
        if answer in ('S', 'N'):
            break
        else:
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada inválida! Digite (S) para Sim ou (N) para Não.{'\033[m'}')
    
    if answer == 'N':
        break

print('=' * line_length)

# Imprimindo dados dos jogadores em formato de tabela
print(f'{'COD.':^{int(line_length * 1/8)}}', end='')
print(f'{'NOME':<{int(line_length * 3/8)}}', end='')
print(f'{'GOLS':<{int(line_length * 3/8)}}', end='')
print(f'{'TOTAL':^{int(line_length * 1/8)}}')

print('-' * line_length)

for i, player in enumerate(players):
    player_code = i

    print(f'{'\033[1;33m'}{player_code:^{int(line_length * 1/8)}}{'\033[m'}', end='')

    print(f'{player['name']:<{int(line_length * 3/8)}}', end='')

    print(f'{f'{player['goals_per_match']}':<{int(line_length * 3/8)}}', end='')

    print(f'{player['total_goals']:^{int(line_length * 1/8)}}', end='')

    print()

print('=' * line_length)

# Mostrando informações de um jogador específico
stop_flag = -1

while True:
    player_code = int(input(f'Digite o código do jogador para ver mais detalhes ({stop_flag} encerrar): '))

    print('-' * line_length)

    if player_code == stop_flag:
        break

    if 0 <= player_code < len(players):
        print(f'* Nome do jogador: {'\033[1;33m'}{players[player_code]['name']}{'\033[m'}')
        print('* Gols por partida:')

        for i, match_goals in enumerate(players[player_code]['goals_per_match']):
            print(' ' * 4, end='') # Espaçamento
            print(f'* {i + 1}ª partida: {'\033[1;33m'}{match_goals} {'gols' if match_goals != 1 else 'gol'}{'\033[m'}')
        
        print(f'* Total de gols: {'\033[1;33m'}{players[player_code]['total_goals']}{'\033[m'}')
    else:
        print(f'{'\033[1;31m'}Código inválido! Digite um código existente.{'\033[m'}')
    
    print('-' * line_length)
