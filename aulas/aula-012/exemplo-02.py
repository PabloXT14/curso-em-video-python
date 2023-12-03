print('# Festa somente para adultos')

print('-' * 70)

age = int(input('Digite sua idade: '))

print('-' * 70)

if age < 18:
    print('* Você é menor de idade.')
    print('* Não pode entrar na festa.')
elif 18 <= age < 65:
    print('* Você é um adulto.')
    print('* Seja bem-vindo a festa.')
else:
    print('* Você é um idoso.')
    print('* Essa festa é muito agitada para você.')
