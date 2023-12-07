# Exercício 6 - Dobro, Triplo, Raiz Quadrada (Aula 007)

'''
# Descrição:

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 
'''

# Resolução

print('Saiba o dobre, triplo e raiz quadrada de um número')

number = int(input('Digite um número: '))

print(f'Dobro de {number} == {number * 2}')
print(f'Triplo de {number} == {number * 3}')
print(f'Raiz quadrada de {number} == {number**(1/2):.2f}')
