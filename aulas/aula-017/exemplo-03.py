list1 = [1, 2, 3]

# Cópias ligadas 
# list2 = list1 # Cria uma cópia ligada uma a outra
# list2[2] = 9 # Altera as duas listas

# Cópias não ligadas
list2 = list1[:] # Faz um fatiamento da lista inteira no início ao fim
list2[2] = 0 # Altera somente a lista 2

print(f'* Lista 1: {list1}')
print(f'* Lista 2: {list2}')
