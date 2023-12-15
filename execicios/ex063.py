# Exercício 63 - Sequência de Fibonacci v1.0 (014)

'''
# Descrição:

Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5
'''

# Resolução:

# Fórmula de Fibonacci: Fn = F(n-1) + F(n-2) onde F1 = 0 e F2 = 1

print('# Sequência de Fibonacci v1.0')

print('-' * 70)

terms_amount = int(input('Digite quantos termos você quer mostrar: '))

print('-' * 70)

# 1ª Solução
count_term = 1
current_term = 0

penultimate_term = 1
last_term = 1

while count_term <= terms_amount:
    # Calculando termo atual da sequência
    if (count_term == 1):
        current_term = 0
    else:
        new_term_value = current_term + last_term

        penultimate_term = last_term
        last_term = current_term
        current_term = new_term_value

    # Lógica para apresentar termos em linha
    print(current_term, end='')
    print(' - ' if count_term < terms_amount else '', end='')

    count_term += 1

# Lógica quebra de linha e mensagem de alerta
if (terms_amount < 0):
    print(f'{'\033[1;33m'}* Por favor, digite um número inteiro positivo.{'\033[m'}')
elif (terms_amount >= 0):
    print()

print('-' * 70)

# 2ª Solução
'''
# Inicialização dos primeiros termos da Sequência de Fibonacci
fibonacci = [0, 1]
if (terms_amount > 2):
    print(f'{fibonacci[0]} - {fibonacci[1]}', end=' - ')
elif (terms_amount == 2):
    print(f'{fibonacci[0]} - {fibonacci[1]}')
elif (terms_amount == 1):
    print(fibonacci[0])
elif (terms_amount == 0):
    print()
else:
    print(f'{'\033[1;33m'}* Por favor, digite um número inteiro positivo.{'\033[m'}')

# Loop para gerar e mostrar os n primeiros termos
i = 2
while i < terms_amount:
    new_term = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(new_term) 
    i += 1

    # Mostra os termos gerados
    if i != terms_amount:
        print(f'{new_term}', end=' - ')
    else:
        print(new_term)

# Fazendo uma quebra de linha no final para outros prints
print('-' * 70)
'''
