# Quantidade de Pares e Ímpares
answer = 'S'
even_amount = 0
odd_amount = 0

while answer == 'S':
    number = int(input('Digite um número: '))

    if (number % 2 == 0):
        even_amount += 1
    else:
        odd_amount += 1

    answer = str(input('Deseja continuar (S/N): ')).upper()

print('-' * 70)
print(f'* Quantidade de pares: {even_amount}')
print(f'* Quantidade de ímpares: {odd_amount}')
