# Exercício 67 - Tabuada v3.0 (015)

'''
# Descrição:

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

# Resolução:

print('# Tabuada v3.0')

count = 1

print('-' * 100)

while True:
    number = int(input('Digite um número para saber sua tabuada (número negativo para encerrar): '))

    if (number < 0):
        print('-' * 100)
        break

    print('-' * 100)

    while count <= 10:
        print(f'{number} x {count:^2} = {'\033[1;33m'}{number * count}{'\033[m'}')
        count += 1
    
    count = 1

    print('-' * 100)
