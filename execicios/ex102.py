# Exercício 102 - Função para Fatorial (021)

'''
# Descrição:

Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o primeiro que indique o 'número' a calcular e o outro chamado 'show', que será um valor 'lógico' (opcional) indicando se será mostrado na tela o processo de cálculo do fatorial.
'''

# Resolução:

line_length = 70

def header(text = '', text_color = '\033[1;36m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)


def factorial(number, show = False):
    """
    Calcula o fatorial de um número e, opcionalmente, mostra o processo de cálculo.

    Parâmetros:
    - numero (int): O número para o qual o fatorial será calculado.
    - show (bool): Um valor lógico indicando se o processo de cálculo será mostrado (padrão é False)
    """
    count = number
    result = 1

    print(f'{number}! = ', end='')

    if show:
        while count >= 1:
            if count == 1:
              print(count, end=' = ')
            else:  
                print(count, end=' x ')
            result *= count
            count -= 1
    else:
        while count >= 1:
            result *= count
            count -= 1

    print(f'{'\033[1;33m'}{result}{'\033[m'}')

header('Cálculo Fatorial')

number = int(input('Digite um número para calcular o fatorial: '))
show = False

while True:
    answer = str(input('Deseja mostrar os processo do calculo? (S/N): ')).strip().upper()

    if answer in ('S', 'N'):
        show = True if answer == 'S' else False
        break
    else:
        print('-' * line_length)
        print(f'{'\033[1;31m'}Entrada inválida! Digite um dos valores possíveis.{'\033[m'}')
        print('-' * line_length)

print('-' * line_length)

factorial(number, show)

print('-' * line_length)
