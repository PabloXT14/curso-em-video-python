# Exercício 73 - Tuplas com Times de Futebol (016)

'''
# Descrição:

Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense/Vasco.
'''

# Resolução:

import shutil 

print('# Tuplas com Times de Futebol')

terminal_size = shutil.get_terminal_size()

line_length = terminal_size.columns

print('-' * line_length)

teams = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atlético-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('* Lista de times:')
print(teams)

print('-' * line_length)

print('A) Os 5 primeiros colocados:')
print(teams[:5])

print('-' * line_length)

print('B) Os últimos 4 colocados:')
print(teams[-4:])

print('-' * line_length)

print('C) Times em ordem alfabética:')
print(sorted(teams))

print('-' * line_length)

searched_team = 'Vasco da Gama'
team_position = teams.index(searched_team) + 1
print(f'D) O time do(a) {searched_team} está na {team_position}ª posição na tabela.')
