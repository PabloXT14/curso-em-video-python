# Exercício 52 - Números Primos (013)

'''
# Descrição:

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

# Resolução: 

print('# Números Primos')

print('-' * 70)

number = int(input('Digite um número inteiro: '))

print('-' * 70)

is_prime_number = True

'''
Explicando fórmula do range:
A escolha do intervalo para o loop `for` que verifica se um número é primo está relacionada à propriedade matemática dos números primos. A ideia é que você só precisa verificar divisores potenciais até a raiz quadrada do número em questão.

Se um número N não é primo, ele pode ser expresso como A × B = N, onde A e B são inteiros diferentes de 1 e N. Se ambos A e B fossem maiores que N, o produto A × B seria maior que N, o que é uma contradição.

Em outras palavras, "qualquer divisor do número maior que a sua raiz quadrada é múltiplo de um divisor menor já testado".

Assim, se não encontrarmos divisores até a raiz quadrada de N, não encontraremos depois. Por isso, podemos limitar a busca até N ** 1/2 ou N ** 0.5 para otimizar o algoritmo.

A adição de `+1` no final do intervalo é para garantir que a função `range` inclua a raiz quadrada de N. A função `range` gera números até, mas não incluindo, o valor final. Portanto, ao adicionar 1 à raiz quadrada, garantimos que ela também será incluída no intervalo de verificação.
'''

for i in range(2, int(number ** 0.5) + 1):
    if (number % i == 0):
        is_prime_number = False

if (is_prime_number):
    print(f'* O número {'\033[1;33m'}{number}{'\033[m'} é primo!')
else:
    print(f'* O número {'\033[1;33m'}{number}{'\033[m'} não é primo!')
