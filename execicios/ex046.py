# Exercício 46 - Contagem Regressiva (013)

'''
# Descrição:

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

# Resolução:

from time import sleep

print('# Contagem Regressiva')

print('-' * 70)

start_range = 10
end_range = 0

for time in range(start_range, end_range, -1):
    print(time)
    sleep(1)

print('-' * 70)

print('Estourar fogos 🎉🥳🎉🥳🚀')
