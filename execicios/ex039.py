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

current_year = datetime.now().year

print('# Alistamento Militar')

print('-' * 70)

birth_year = int(input('Digite o seu ano de nascimento: '))

print('-' * 70)


candidate_age = current_year - birth_year

minimum_age_enlistment = 18

if (candidate_age < minimum_age_enlistment):
    missing_years =  minimum_age_enlistment - candidate_age

    print('* Você ainda vai se alistar ao serviço militar.')
    print(f'* Faltam {'\033[1;33m'}{missing_years} ano(s){'\033[m'}.')
elif (candidate_age == minimum_age_enlistment):
    print(f'{'\033[1;33m'}* É a hora de se alistar ao serviço militar.{'\033[m'}')
else:
    past_years = candidate_age - minimum_age_enlistment

    print('* Já passou do tempo do alistamento.')
    print(f'* Passaram {'\033[1;33m'}{past_years} ano(s){'\033[m'}.')
