# Exercício 47 - Contagem de pares (013)

'''
# Descrição:

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# Resolução:

print('# Contagem de pares')

print('-' * 70)

start_range = 1
end_range = 51 # Lembrando que o end/stop na função range() não é incluso, dai 51

number_caracteres_space = len(str(end_range))

for number in range(start_range, end_range):
    if (number % 2 == 0):
        print(f'{number:{number_caracteres_space}}', end=" ")
    
    # Quebrando linha
    if (number % 10 == 0):
        print()

print('-' * 70)
