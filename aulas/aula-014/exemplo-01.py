# Comparando for e while

# Utiliza-se o for quando sabemos o limite ou número exato de repetições (iterações) que o nosso código deve ter
for i in range(1, 10):
    print(i)
print('Fim')

print('-' * 70)

# No caso do while podemos utilizá-lo tanto quando sabemos o número exato de iterações, e quando não sabemos o número exato de iterações
answer = 'S'
while answer == 'S':
    n = int(input('Digite um valor: '))
    answer = str(input('Deseja continuar (S/N): ')).upper()

print('Fim')

'''
# Conclusão:

No final das contas, tudo vai depender da situação e escolha sua de qual estrutura de repetição irá utilizar. Vale ressaltar, que uma estrutura não é mais rápida que a outra, mas em alguns casos no qual não se sabe o número exato de repetições, a estrutura while se adapta melhor. 
'''