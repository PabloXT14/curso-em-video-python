count = 0

# Loop clássico
'''
while count <= 10:
    print(count)
    count += 1

print('-' * 70)
'''

# Loop infinito
while True:
    print(count)
    count += 1

    # Condição para que o loop pare
    if count == 10:
        break
print('-' * 70)
