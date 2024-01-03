# Exercício 97 - Um print especial (020)

'''
# Descrição:

Faça um programa que tenha uma função chamada escreva(), que receberá um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 

escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~
'''

# Resolução:

line_length = 70

def header(line_symbol = '-', text = '', text_color = '\033[1;32m'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)

def write(text = '', line_symbol = '~'):
    extra_size = 4
    text_size = len(text) + extra_size
    print(line_symbol * text_size)
    print(f'{text:^{text_size}}')
    print(line_symbol * text_size)

header(text='Um print especial')

text = str(input('Digite um texto qualquer: '))

write(text)
