# Exercício 83 - Validando Expressões Matemáticas (017)

'''
# Descrição:

Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

# Resolução:

line_length = 70

print('# Validando Expressões Matemáticas')

print('-' * line_length)

math_expression = str(input('Digite a expressão: '))

print('-' * line_length)

parenthesis_list = []

# Balanceando parênteses
for char in math_expression:
    if char == '(':
        parenthesis_list.append(char)
    elif char == ')':
        if '(' in parenthesis_list:
            parenthesis_list.pop() # Apaga a última abertura de parênteses registrada na lista para balancear com o parênteses de fechando que foi encontrado
        else:
            continue
        

is_expression_valid = len(parenthesis_list) == 0 # Se a lista "parenthesis_list" estiver vazia, os parênteses estão balanceados

if is_expression_valid:
    print(f'{'\033[1;32m'}* Sua expressão está correta!{'\033[m'}')
else:
    print(f'{'\033[1;31m'}* Sua expressão está errada!{'\033[m'}')
