# Analisando String

print('Analisando String')

print('-' * 40)

phrase = 'Curso em Vídeo Python'

print(f'- Frase inicial: {phrase}')

print(f'- Comprimento da frase: {len(phrase)}')

print(f"- Contando quantas vezes o caracter 'o' aparece na frase inteira: {phrase.count('o')}")

print(f"- Contando quantas vezes o caracter 'o' aparece em uma parte especifica da frase: {phrase.count('o', 0,13)}")

print(f"- A partir de qual indice encontrou o texto 'deo': {phrase.find('deo')}")

print(f"- Tentando encontrar texto inexistente ('Android') na frase: {phrase.find('Android')}") # return -1

print(f"- Existe o texto 'Curso' na frase: {'Curso' in phrase}")
