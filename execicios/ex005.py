# Exercício 5 - Antecessor e Sucessor (Aula 007)

'''
# Descrição:

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. 
'''

# Resolução

number = int(input('Digite um número inteiro: '))

print(f'Antecessor: {number - 1}')
print(f'Sucessor: {number + 1}')
print(f'{number - 1} < {number} < {number + 1}')
