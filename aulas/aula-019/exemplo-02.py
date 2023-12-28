line_length = 100
brasil = []

estado1 = { 'uf': 'Rio de Janeiro', 'sigla': 'RJ' }
estado2 = { 'uf': 'São Paulo', 'sigla': 'SP' }

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

print('-' * line_length)

print(brasil[0])
print(brasil[1])

print('-' * line_length)

print(brasil[0]['uf']) # Rio de Janeiro
print(brasil[1]['sigla']) # SP

print('-' * line_length)
