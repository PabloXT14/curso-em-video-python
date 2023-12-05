# Exercício 42 - Analisando Triângulos v2.0 (Aula 012)

'''
# Descrição:

Refaça o 'Desafio 035' dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''

# Resolução:

print('# Analisando Triângulos v2.0')

print('-' * 70)

side_1 = float(input('Digite o valor do 1º lado do triângulo: '))
side_2 = float(input('Digite o valor do 2º lado do triângulo: '))
side_3 = float(input('Digite o valor do 3º lado do triângulo: '))

print('-' * 70)

is_triangle = (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1)
triangle_type = ''

if (is_triangle):
    if (side_1 == side_2 == side_3):
        triangle_type = 'Equilátero'
    elif (side_1 == side_2) or (side_2 == side_3) or (side_1 == side_3):
        triangle_type = 'Isósceles'
    else:
        triangle_type = 'Escaleno' 

    print(f'* Estes valores formam um triângulo: {'\033[1;33m'}{triangle_type}{'\033[m'}')
else:
    print(f'{'\033[1;33m'}* Estes valores não formam um triângulo.{'\033[m'}')

    
