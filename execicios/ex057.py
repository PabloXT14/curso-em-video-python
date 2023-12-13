# Exercício 57 - Validação de Dados (014)

'''
# Descrição:

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

# Resolução:

print('# Validação de Dados')

print('-' * 70)

answer = ''

while answer != 'M' and answer != 'F':
    answer = str(input('Digite o seu sexo (M/F): ')).strip().upper()

print('-' * 70)

print(f'* Sexo digitado: {answer}')
print('* Muito abrigado e tenha um ótimo dia!')
