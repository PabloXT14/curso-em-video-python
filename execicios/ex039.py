# Exercício 39 - Alistamento Militar (Aula 012)

'''
# Descrição: 

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele 'ainda vai se alistar' ao serviço militar.
- Se é a 'hora de se alistar'.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

* Obs: pegue o ano atual da máquina do usuário para comparar.
'''

# Resolução:

from datetime import datetime
from sys import exit

current_year = datetime.now().year

print('# Alistamento Militar')

print('-' * 70)

gender = ''

while True:
    print('Qual o seu sexo:')
    print('H - Homem')
    print('M - Mulher')

    gender = str(input('Digite a letra correspondente ao seu sexo: ')).lower()

    print('-' * 70)

    if (gender == 'h' or gender == 'm'):
        break
    else:
        print('Escolha inválida. Por favor digite uma das opções disponíveis.')

    print('-' * 70)

if (gender == 'm'):
    print(f'{'\033[1;33m'}* Você não precisa fazer o alistamento militar obrigatório.{'\033[m'}')
    exit()


birth_year = int(input('Digite o seu ano de nascimento: '))

print('-' * 70)


candidate_age = current_year - birth_year

minimum_age_enlistment = 18

if (candidate_age < minimum_age_enlistment):
    missing_years =  minimum_age_enlistment - candidate_age

    print('* Você ainda vai se alistar ao serviço militar.')
    print(f'* Falta(m) {'\033[1;33m'}{missing_years} ano(s){'\033[m'}.')
    print(f'* Seu alistamento será no ano: {'\033[1;33m'}{current_year + missing_years}{'\033[m'}')

elif (candidate_age == minimum_age_enlistment):
    print(f'{'\033[1;33m'}* É a hora de se alistar ao serviço militar.{'\033[m'}')
    print(f'{'\033[1;33m'}* Vá a uma junta militar o mais breve possível.{'\033[m'}')

else:
    past_years = candidate_age - minimum_age_enlistment

    print('* Já passou do tempo do alistamento.')
    print(f'* Passaram {'\033[1;33m'}{past_years} ano(s){'\033[m'}.')
    print(f'* Seu alistamento foi no ano: {'\033[1;33m'}{current_year - past_years}{'\033[m'}')
