numbers = [2, 5, 9, 1]

# Modificando elemento
numbers[2] = 3

# Adicionando elemento no final
numbers.append(7)

# Organizando elementos
numbers.sort()
numbers.sort(reverse=True)

# Adicionando elemento em uma posição específica
numbers.insert(2, 2)

# Removendo elemento do final
numbers.pop()

# Removendo elemento em um índice especifico
numbers.pop(0)

# Removendo o primeiro elemento pelo valor
numbers.remove(2)

if 4 in numbers: # usando in com remove para evitar erro
    numbers.remove(4)
else:
    print('* Não achei o número 4.')

print(f'* Lista: {numbers}')
print(f'* Tamanho da lista: {len(numbers)}')
