# Exercício 47 - Contagem de pares (013)

'''
# Descrição:

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# Resolução:

print('# Contagem de pares')

print('-' * 70)

numbers_per_line = 5
numbers_in_line = 0

# 1ª Solução (menos performance -> mais loops para percorrer)
'''
start_range = 1
end_range = 51 # Lembrando que o end/stop na função range() não é incluso, dai 51

number_caracteres_space = len(str(end_range))

for number in range(start_range, end_range):
    if (number % 2 == 0):
        print(f'{number:{number_caracteres_space}}', end=" ")

        numbers_in_line += 1

        # Quebrando linha
        if numbers_in_line == numbers_per_line:
            print()
            numbers_in_line = 0
'''

# 2ª Solução (mais performance -> menos iterações para o loop percorrer)

start_range = 2
end_range = 51

number_caracteres_space = len(str(end_range))

# pulando de 2 em 2 dois já sabemos que o primeiro é par e só dois números a frente será par novamente
for number in range(start_range, end_range, 2):
    print(f'{number:{number_caracteres_space}}', end=' ')
    numbers_in_line += 1

    # Quebrando linha
    if numbers_in_line == numbers_per_line:
        print()
        numbers_in_line = 0

print()
print('-' * 70)
