# Realizando operações aritméticas com dois números digitados

print('Realizando operações aritméticas com dois números digitados')

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

print(f'{n1} + {n2} == {n1 + n2}')
print(f'{n1} - {n2} == {n1 - n2}')
print(f'{n1} * {n2} == {n1 * n2}')
print(f'{n1} / {n2} == {(n1 / n2):.3f}') # :.3f -> para ter no máximo 3 casa decimais 
print(f'{n1} ** {n2} == {n1 ** n2}')
print(f'{n1} // {n2} == {n1 // n2}')
print(f'{n1} % {n2} == {n1 % n2}')

# Outras dicas de indentação
# \n -> para quebrar ou criar uma nova linha em uma string
# end=' ' -> para não quebrar linha de um print() para outro print(), mas precisa no final do parenteses de cada print()

print('Dicas de Indentação')

print('Linha 1 \nLinha 3')

print('Coluna 1', end=' ')
print('Coluna 2')