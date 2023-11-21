# Junção e Divisão de Strings

print('Junção e Divisão de Strings')

print('-' * 80)

phrase = 'Curso em Vídeo Python'

print(f'- Frase inicial: {phrase}')

print(f'- Dividindo a frase nos espaços em branco e colocando cada item/palavra em um Array: {phrase.split()}')

print(f"- Juntando itens de um Array em uma string, dividindo cada item por um traço: {'-'.join(phrase.split())}")
