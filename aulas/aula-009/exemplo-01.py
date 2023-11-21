# Fatiando uma String

print('Fatiando Strings')

print('-' * 40)

phrase = 'Curso em Vídeo Python'

print(f'- Frase inicial: {phrase}')

print(f'- Fatiando uma letra: {phrase[9]}') # entre colchetes é o indice do caracter na string (obs: começa do indice 0 da esquerda para a direita)

print(f'- Fatiando um conjunto de letras: {phrase[9:13]}') # pega do caracter de indice 9 até o caracter de indice 13 (onde o 13 não é incluido)

print(f'- Fatiando um pedaço pulando de 2 em 2: {phrase[9:21:2]}') # pega do indice 9 até o 21 pulando de 2 em 2

print(f'- Fatiando sem indice inicial: {phrase[:5]}') # quando se omite o indie inicial (deixando só os :) será pego/considerado a partir do caracter de indice 0, indo até o indice 5 (mas lembrando não incluindo o segundo indice como já dito anteriormente)

print(f'- Fatiando sem indice final: {phrase[15:]}') # vai fatiar do indice indicado até o indice final da string

print(f'- Fatiando de 3 em 3 até o final: {phrase[9::3]}') # vai ir do indice 9 até o final da string, pulando de 3 em 3

print(f'- Fatiando de 2 em 2 do inicio até um limite: {phrase[:5:2]}')
