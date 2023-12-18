# Apagando da memória 
# OBS: este é um recurso do python que pode ser utilizado com outras estruturas de armazenamento de dados.

pessoa = ('John Doe', 21, 'M', 75.45)

del(pessoa[0]) # imprime erro, pois não podemos deletar um dado interno de uma tupla

del(pessoa)

print(pessoa) # imprime erro pois apagamos a tupla
