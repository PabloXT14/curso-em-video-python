# Exercício 101 - Função para votação (021)

'''
# Descrição:

Crie um programa que tenha uma função chamada voto(), que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

* OBS:
- Obrigatório a partir dos 18 anos
- Facultativo para jovens de 16 e 17 anos e idosos acima de 70 anos: 
'''

# Resolução:

from datetime import datetime

line_length = 70

def header(text = '', text_color = '\033[1;32m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)

def vote(birth_year):
    person_status = ''

    person_age = int(datetime.now().year - birth_year)

    if person_age < 16:
        person_status = f'{'\033[1;31m'}VOTO NEGADO{'\033[m'}'
    elif (16 < person_age <= 17) or (person_age > 70):
        person_status = f'{'\033[1;33m'}VOTO OPCIONAL{'\033[m'}'
    else:
        person_status = f'{'\033[1;32m'}VOTO OBRIGATÓRIO{'\033[m'}'
    
    return f'* Condição de voto para {person_age} anos: {person_status}'

header('Status Eleitoral')

birth_year = int(input('Digite o ano de nascimento: '))

print('-' * line_length)

result = vote(birth_year)

print(result)

print('-' * line_length)
