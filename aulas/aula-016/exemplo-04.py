# Métodos comuns de Tupla

# sorted()
snacks = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(sorted(snacks))# imprimi a tupla em ordem sortida em ordem alfabética (mas não altera a tupla original)
print(snacks)

# count()
numbers = (3, 2, 1, 3, 5, 6)
print(f'Tamo da tupla: {numbers.count(3)}')

# index()
print(snacks.index('Suco'))
print(numbers.index(3, 1)) # imprimindo o índice a partir de uma determinada posição
