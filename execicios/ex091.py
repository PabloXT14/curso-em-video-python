# Exercício 91 - Jogo de Dados em Python (019)

'''
# Descrição:

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

# Resolução:

from random import randint
from time import sleep

line_length = 70

print('# Jogo de Dados em Python')

print('-' * line_length)

players_amount = 4
start_random_range = 1
stop_random_range = 6

# Dicionário para armazenar os resultados dos jogadores
players_results = {}

for player in range(0, players_amount):
    dice_result = randint(start_random_range, stop_random_range)
    players_results[f'Jogador {player + 1}'] = dice_result

# Exibindo resultados antes da ordenação
print(f'{'\033[1;35m'}{'VALORES SORTEADOS':^{line_length}}{'\033[m'}')

print('-' * line_length)

for player, result in players_results.items():
    sleep(1)
    print(f'* {player}: {'\033[1;33m'}{result}{'\033[m'}')

print('-' * line_length)

# Ordenando o dicionário pelos valores (resultado do dado) em ordem decrescente
'''
Neste exemplo, sorted() é usado com a função lambda como a chave de ordenação. O argumento item[1] no lambda representa o valor associado a cada chave no dicionário. Isso ordenará o dicionário pelos valores em ordem crescente.

Se você quiser ordenar em ordem decrescente, você pode adicionar o argumento reverse=True à função sorted()
'''
print(f'{'\033[1;35m'}{'RANKING DOS JOGADORES':^{line_length}}{'\033[m'}')

print('-' * line_length)

players_results_ordered = dict(sorted(players_results.items(), key=lambda item: item[1], reverse=True))

# Exibindo os resultados ordenados
for i, player in enumerate(players_results_ordered.items()):
    player_name, player_result = player
    sleep(1)
    print(f'{i + 1}º - {player_name} ({'\033[1;33m'}{player_result}{'\033[m'})')

print('-' * line_length)
