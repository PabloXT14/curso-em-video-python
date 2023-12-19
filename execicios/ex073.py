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

print('# Tuplas com Times de Futebol')

print('-' * 100)

brazilian_table = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atlético-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('A) Os 5 primeiros colocados:')
print(brazilian_table[:5])

print('-' * 100)

print('B) Os últimos 4 colocados:')
print(brazilian_table[-4:])

print('-' * 100)

print('C) Times em ordem alfabética:')
print(sorted(brazilian_table))

print('-' * 100)

searched_team = 'Vasco da Gama'
position = brazilian_table.index(searched_team) + 1
print(f'D) O time da(o) {searched_team} está na posição {position} na tabela.')
