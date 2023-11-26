# Condição Composta

# Exemplo 1
'''
print('-' * 40)

age = int(input('Digite sua idade: '))

if age < 12:
    print('Você é uma criança.')
elif 12 <= age < 18:
    print('Você é um adolescente.')
elif  18 <= age < 60:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')

print('-' * 40)
'''

# Exemplo 2

print('-' * 70)

garde_1 = float(input('Digite sua primeira nota: '))
grade_2 = float(input('Digite sua segunda nota: '))

average = round((garde_1 + grade_2) / 2, 1)

print(f'A sua média foi: {average}')

# if average >= 6:
#     print('PARABÉNS, você tirou uma boa nota.')
# else:
#     print('ESTUDE MAIS, da próxima vez você consegue.')

# (if simplificado/"ternário")
# obs: em python não existe if ternário, a estrutura a seguir é uma espécie rudimentar de if ternário que possui em outras linguagens.
print('PARABÉNS, você tirou uma boa nota.' if average >= 6 else 'ESTUDE MAIS, da próxima vez você consegue.')

print('-' * 70)
