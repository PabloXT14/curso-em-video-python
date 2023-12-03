name = str(input('Qual é seu nome?: ')).capitalize()

if name == 'Pablo':
    print('Que nome massa!')
elif name == 'Pedro' or name == 'Maria' or name == 'Enzo':
    print('Seu nome é bem popular no Brasil!')
elif name in 'Ana, Cláudia, Jessica, Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {name}!')
