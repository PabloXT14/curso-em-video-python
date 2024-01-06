# Exercício 103 - Ficha do Jogador (021)

'''
# Descrição:

Faça um programa que tenha uma função chamada 'ficha()', que receba dois 'parâmetros opcionais': o 'nome' de um jogador e quantos 'gols' ele marcou.

O programa deverá ser capaz de mostrar a 'ficha do jogador', mesmo que algum dado não tenha sido informado corretamente.
'''

# Resolução:

line_length = 70

def header(text = '', text_color = '\033[1;35m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)

def token(name, goals):
    token_length = 30

    if not name:
        name = '<desconhecido>'
    else:
        name = str(name).upper()

    if not goals:
        goals = 0
    else:
        goals = int(goals)

    print(f'+{'-' * int(token_length * 1/3)}-{'-' * int(token_length * 2/3)}+')

    print(f'|{'\033[1;32m'}{'FICHA':^{token_length + 1}}{'\033[m'}|')
    
    print(f'+{'-' * int(token_length * 1/3)}-{'-' * int(token_length * 2/3)}+')

    print(f'|{' NOME':{int(token_length * 1/3)}}|{'\033[1;33m'}{f' {name}':{int(token_length * 2/3)}}{'\033[m'}|')

    print(f'+{'-' * int(token_length * 1/3)}+{'-' * int(token_length * 2/3)}+')

    print(f'|{' GOLS':{int(token_length * 1/3)}}|{'\033[1;33m'}{f' {goals}':{int(token_length * 2/3)}}{'\033[m'}|')

    print(f'+{'-' * int(token_length * 1/3)}-{'-' * int(token_length * 2/3)}+')

header('Ficha do Jogador')

player_name = input("Digite o nome do jogador: ").strip()
goals_amount = input("Digite a quantidade de gols marcados: ").strip()

print('-' * line_length)

token(player_name, goals_amount)
