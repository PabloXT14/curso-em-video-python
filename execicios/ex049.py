# Exercício 49 - Tabuada v2.0 (013)

'''
# Descrição:

Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

# Resolução:

print('# Tabuada v2.0')

print('-' * 70)

number = int(input('Digite um número para saber a sua tabuada: '))

print('-' * 70)

for i in range(1, 11):
    result = number * i
    print(f'{number} x {i:^2} = {'\033[1;33m'}{result}{'\033[m'}')
