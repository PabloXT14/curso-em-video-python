# Escopo de Variáveis 

def test():
    # Para usar a variável z global no contexto local faça o seguinte
    global z

    x = 7
    z = 9


    print(f'No contexto local, n = {n}')
    print(f'No contexto local, x = {x}')
    print(f'No contexto local, z = {z}')
    pass
# Fluxo Principal
n = 2
z = 1

print(f'No contexto global, n = {n}')
test()
# print(f'No contexto global, x = {x}') # Erro (pois x está somente no escopo da função test())

print('-' * 70)

test()
print(f'No contexto global, z = {z}')