line_length = 100
estado = dict()
brasil = list()

for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))

    print('-' * line_length)

    # Todos os dicionários na lista vão ficar com o mesmo valor da última iteração for
    # brasil.append(estado) 

    # Gera uma cópia do estado, desta forma os itens na lista terão o valor diferente
    brasil.append(estado.copy()) 

for estado in brasil:
    for key, value in estado.items():
        print(f'* {key}: {value}')

    print('-' * line_length)
